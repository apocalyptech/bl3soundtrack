#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
import re
import sys
import enum
import math
import argparse

group_re = re.compile('^-(?P<type>[A-Z])(?P<num>\d+)(?P<rest>.*?)$')

class BaseDef:
    """
    Class to hold "common" arguments between Files and Groups.  This is possibly
    a little bit improper -- `subsong` for instance only really makes sense for
    Files, and `layer_channels` only really makes sense for Groups.  They're
    similar enough, though, that it doesn't seem worth it to duplicate processing
    (or try to figure out a clean way of isolating those File-or-Group-specific
    vars).  So, we're just processing everything identically.
    """

    def __init__(self):

        self.ignore_loops = False
        self.length = None
        self.length_no_fade = None
        self.pad_beginning = None
        self.pad_end = None
        self.trim_beginning = None
        self.trim_end = None
        self.volume = None
        self.volume_pct = None
        self.loop = False
        self.loop_end = False
        self.num_loops = None
        self.full_loop = False
        self.force_full_loop = False
        self.fade_period = None
        self.fade_delay = None
        self.comments = None

        # Some presumably file-specific stuff
        self.subsong = None

        # Some presumably group-specific stuff
        self.layer_channels = False

    def set_volume(self, volume):
        self.volume_pct = None
        self.volume = volume

    def set_volume_pct(self, volume_pct):
        self.volume_pct = volume_pct
        self.volume = None

    def _copy_to(self, new_obj):
        """
        Copies ourself to a new object
        """
        new_obj.ignore_loops = self.ignore_loops
        new_obj.length = self.length
        new_obj.length_no_fade = self.length_no_fade
        new_obj.pad_beginning = self.pad_beginning
        new_obj.pad_end = self.pad_end
        new_obj.trim_beginning = self.trim_beginning
        new_obj.trim_end = self.trim_end
        new_obj.volume = self.volume
        new_obj.volume_pct = self.volume_pct
        new_obj.loop = self.loop
        new_obj.loop_end = self.loop_end
        new_obj.num_loops = self.num_loops
        new_obj.full_loop = self.full_loop
        new_obj.force_full_loop = self.force_full_loop
        new_obj.fade_period = self.fade_period
        new_obj.fade_delay = self.fade_delay
        new_obj.comments = self.comments
        new_obj.subsong = self.subsong
        new_obj.layer_channels = self.layer_channels

    def parse_args(self, args):
        """
        This is pretty un-pythonic, but we may need to process
        more than one arg at a time, so it seemed the way to go.
        """

        i = 0
        while i < len(args):
            if args[i] == '#i':
                self.ignore_loops = True
            elif args[i] == '#b':
                self.length = float(args[i+1])
                i += 1
            elif args[i] == '#B':
                self.length_no_fade = float(args[i+1])
                i += 1
            elif args[i] == '#p':
                self.pad_beginning = float(args[i+1])
                i += 1
            elif args[i] == '#P':
                self.pad_end = float(args[i+1])
                i += 1
            elif args[i] == '#r':
                self.trim_beginning = float(args[i+1])
                i += 1
            elif args[i] == '#R':
                self.trim_end = float(args[i+1])
                i += 1
            elif args[i] == '#v':
                if args[i+1][-2:].lower() == 'db':
                    self.set_volume(float(args[i+1][:-2]))
                else:
                    self.set_volume_pct(float(args[i+1]))
                i += 1
            elif args[i] == '#l':
                self.num_loops = float(args[i+1])
                i += 1
            elif args[i] == '#e':
                self.full_loop = True
            elif args[i] == '#E':
                self.force_full_loop = True
            elif args[i] == '#f':
                self.fade_period = float(args[i+1])
                i += 1
            elif args[i] == '#d':
                self.fade_delay = float(args[i+1])
                i += 1
            elif args[i] == '#@loop':
                self.loop = True
            elif args[i] == '#@loop-end':
                self.loop_end = True
            elif args[i] == '#@layer-v':
                self.layer_channels = True
            elif args[i].startswith('#s'):
                self.subsong = int(args[i][2:])
            elif args[i].startswith('##'):
                # Double hashes *seem* to be the Actual Comments when on file/group lines,
                # though in some cases they seem like they might be processed somehow
                # too?  Like when a File references a .bnk, there's a .wem path listed
                # in the "comments" here.  We see "##loop" quite frequently, but I'm
                # pretty sure that *those*, at least, are just comments, since there are
                # other looping parameters elsewhere.  Anyway, I don't really care
                # enough to try and figure it out for sure, so we'll just assume that
                # they're comments and be done with it.
                self.comments = ' '.join(args[i:])
                i = len(args)
            else:
                raise Exception('Unknown file argument: {}'.format(args[i]))
            i += 1

    def _report_float(self, value):
        """
        How to report values when writing our TXTPs.  Basically, str() nearly
        always does what we want, but for very small values it starts reporting
        in scientific notation, which we don't want.  Honestly it's a bit
        ridiculous to be bothering with this for such small values, but this
        behavior ends up reporting basically identically to the wwiser-generated
        values, when we re-write, so this is what I'm doing for now.
        """
        basic = str(value)
        if 'e-' in basic:
            return '{:0.10f}'.format(value)
        elif '.' not in basic:
            return '{}.0'.format(basic)
        else:
            return basic

    def report_args(self):
        """
        Return our arguments as a list of text to be space-separated when writing
        out a new TXTP.  These aren't always the same order that wwiser puts 'em
        in, but they're often pretty close.  (The wwiser ordering doesn't *always*
        seem to be entirely consistent either; it might depend on how the BNK
        is set up.)
        """
        report = []
        if self.subsong is not None:
            report.append('#s{}'.format(self.subsong))
        if self.ignore_loops:
            report.append('#i')
        if self.pad_beginning is not None:
            report.append('#p')
            report.append(self._report_float(self.pad_beginning))
        if self.length is not None:
            report.append('#b')
            report.append(self._report_float(self.length))
        if self.trim_beginning is not None:
            report.append('#r')
            report.append(self._report_float(self.trim_beginning))
        if self.pad_end is not None:
            report.append('#P')
            report.append(self._report_float(self.pad_end))
        if self.length_no_fade is not None:
            report.append('#B')
            report.append(self._report_float(self.length_no_fade))
        if self.trim_end is not None:
            report.append('#R')
            report.append(self._report_float(self.trim_end))
        if self.full_loop:
            report.append('#e')
        if self.force_full_loop:
            report.append('#E')
        if self.num_loops is not None:
            # Default num_loops is 2, btw
            report.append('#l')
            report.append(str(self.num_loops))
        if self.fade_period is not None:
            # Default fade_period is 10, btw
            report.append('#f')
            report.append(str(self.fade_period))
        if self.fade_delay is not None:
            # Default fade_delay is 0, btw
            report.append('#d')
            report.append(str(self.fade_delay))
        if self.volume is not None:
            report.append('#v')
            report.append('{}dB'.format(self.volume))
        elif self.volume_pct is not None:
            report.append('#v')
            report.append(str(self.volume_pct))
        if self.layer_channels:
            report.append('#@layer-v')
        if self.loop:
            report.append('#@loop')
        if self.loop_end:
            report.append('#@loop-end')
        if self.comments is not None:
            report.append(self.comments)
        return report

    def remove_length(self):
        """
        Removes the "length" parameter.  Pretty specific-purpose, to
        support a mode on leadin soundtracks.
        """
        self.length = None

class File(BaseDef):
    """
    Info about a file (.wem or .bnk, though we don't explicitly enforce that here)
    """

    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.silent = False

    @staticmethod
    def from_txtp(parts):
        """
        Creates a new File object from txtp definitions.  `parts` should
        be the full txtp line, split by whitespace into a list.
        """

        # First parse our silentness
        if parts[0] == '?':
            filename = parts[0][1:]
            silent = True
        else:
            filename = parts[0]
            silent = False

        # Create a new object
        new_file = File(filename)
        new_file.silent = silent

        # Parse args
        new_file.parse_args(parts[1:])

        # Return the new obj
        return new_file

    def __repr__(self):
        return 'File<{}>'.format(self.filename)

    def copy(self):
        """
        Returns a copy of ourself
        """
        new_file = File(self.filename)
        new_file.silent = self.silent
        self._copy_to(new_file)
        return new_file

    def to_string(self, cur_indent=0):
        """
        Outputs ourself in txtp format.
        """
        if self.silent:
            report = ['?{}'.format(self.filename)]
        else:
            report = [self.filename]
        report.extend(self.report_args())
        return '{}{}'.format(
                ' '*cur_indent,
                ' '.join(report),
                )

class GroupType(enum.Enum):
    SEGMENT = 'S'
    LAYER = 'L'
    RANDOM = 'R'

class Group(BaseDef):
    """
    Info about a Group
    """

    def __init__(self, group_type, initial_contents=None):
        super().__init__()
        self.group_type = group_type
        if self.group_type == GroupType.RANDOM:
            # Default to actually-random
            self.random_selection = 0
        else:
            self.random_selection = None
        if initial_contents is None:
            self.contents = []
        else:
            self.contents = initial_contents

    def copy(self):
        """
        Returns a copy of ourself
        """
        new_group = Group(self.group_type, initial_contents=[])
        new_group.random_selection = self.random_selection
        self._copy_to(new_group)
        for content in self.contents:
            new_group.contents.append(content.copy())
        return new_group

    def remove_length(self):
        """
        Recursively removes the "length" parameter.  Pretty specific-purpose, to
        support a mode on leadin soundtracks.
        """
        super().remove_length()
        for content in self.contents:
            content.remove_length()

    @staticmethod
    def from_txtp(stack, parts):
        """
        Parses txtp data for groups.  `stack` should be the current stack of
        txtp components; this will pop items off the end to use as contents,
        based on the number of items reported in the definition.  `parts`
        should be the complete txtp line, split by whitespace into a list.
        """

        global group_re

        # First pull the basic group info out
        assert(parts[0] == 'group')
        assert(parts[1] == '=')
        match = group_re.match(parts[2])
        if not match:
            raise Exception('Unknown group parameters: {}'.format(parts[2]))
        group_type = match.group('type')
        group_num = int(match.group('num'))
        group_rest = match.group('rest')

        # Create the new group, pulling the appropriate number of items off the stack.
        new_group = Group(GroupType(group_type), stack[-group_num:])
        del stack[-group_num:]

        # Extra config for Random layers.  Valid values are:
        #   -: Basically turns Random into Serial
        #   0: Actually Randomize
        #   n: The specific element in here
        if new_group.group_type == GroupType.RANDOM:
            assert(group_rest[0] == '>')
            new_group.random_selection = group_rest[1:]

        # Parse args
        # more than one arg at a time, so it seemed the way to go.
        new_group.parse_args(parts[3:])

        # Now return the new object
        return new_group

    def __repr__(self):
        return 'Group<{},{}>'.format(
                self.group_type,
                len(self.contents),
                )

    def to_string(self, cur_indent=0):
        """
        Outputs ourself in txtp format.
        """
        lines = []
        for content in self.contents:
            lines.append(content.to_string(cur_indent+1))

        report = ['group', '=']
        report.append('-{}{}'.format(
            self.group_type.value,
            len(self.contents)
            ))
        if self.group_type == GroupType.RANDOM:
            report[-1] = '{}>{}'.format(
                    report[-1],
                    self.random_selection,
                    )
        report.extend(self.report_args())
        lines.append('{}{}'.format(
            ' '*cur_indent,
            ' '.join(report),
            ))
        return "\n".join(lines)

class Txtp:
    """
    Our representation of a TXTP object.  This whole app is only really geared to the
    wwiser-generated TXTP files from BL3 data, and may not survive contact with other
    TXTPs out there -- for instance, we assume whitespace between args (which might
    not actually be required), we assume that there's only a single "top-level"
    element (which might not be the case), and we're only supporting the subset of
    options which show up in the BL3 data.  Comments are assumed to always be at
    the end of the file, after all other directives have been processed.
    """

    def __init__(self, initial_root=None, comments=None):
        self.root = initial_root
        if comments is None:
            self.comments = []
        else:
            self.comments = comments

    def to_string(self, do_comments=False):
        """
        Ourself as a text string
        """
        parts = [self.root.to_string()]
        if do_comments and self.comments:
            parts.append('')
            parts.append('')
            parts.append('')
            parts.extend(self.comments)
        # Make sure there's a newline at the end
        parts.append('')
        return "\n".join(parts)

    @staticmethod
    def from_file(filename):
        """
        Loads a TXTP file from the given `filename`
        """
        stack = []
        comments = []
        with open(filename) as df:
            for line in df:
                line = line.strip()
                if line == '':
                    continue
                if line[0] == '#':
                    comments.append(line)
                    continue
                parts = line.split()
                if parts[0].endswith('.wem') or parts[0].endswith('.bnk') or parts[0][0] == '?':
                    stack.append(File.from_txtp(parts))
                elif parts[0] == 'group':
                    stack.append(Group.from_txtp(stack, parts))
                else:
                    raise Exception('Unknown line: {}'.format(line))
        assert(len(stack) == 1)
        return Txtp(initial_root=stack[0], comments=comments)

def do_transforms(node, volume_nodes, is_root=False):
    """
    Does our standard set of post-extraction transforms on the given node.
    Will recurse into contents, if the node happens to be a group.
    `volume_nodes` is a list of nodes in the structure which have a
    volume defined.  If `is_root` is `True`, this node will not be
    added to `volume_nodes` even if it has a volume component.
    """

    # Make a note if we have volume info
    if not is_root and (node.volume is not None or node.volume_pct is not None):
        volume_nodes.append(node)

    # Make sure we're not set to loop
    node.loop = False
    node.loop_end = False

    # If we're a random group, Actually Randomize.
    if type(node) == Group and node.group_type == GroupType.RANDOM and node.random_selection != '-':
        node.random_selection = 0

    # Now recurse, if we're a group
    if type(node) == Group:
        for inner in node.contents:
            do_transforms(inner, volume_nodes)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            description='Performs various actions on TXTP files',
            )

    action = parser.add_mutually_exclusive_group(required=True)

    action.add_argument('-o', '--output',
            type=str,
            help='Output our parsed version of the specified file',
            )

    action.add_argument('-s', '--split',
            type=str,
            help="""Split the the segmented file into multiple txtp files.
                Will write to numbered files starting with 1.txtp""",
            )

    action.add_argument('-c', '--check',
            action='store_true',
            help='Check all TXTP files in the cur directory for parseability',
            )

    action.add_argument('--find-leadins',
            action='store_true',
            help="""Report on files in the current dir which have what appear to
                be 'leadin' intro segments.""",
            )

    action.add_argument('--do-transforms',
            action='store_true',
            help="""Do the transforms I like to do on freshly-extracted music.
                Namely: adjust volumes to try and avoid super-quiet music,
                set random groups to actually randomize, and remove loop
                parameters.""",
            )

    action.add_argument('--soundtrack',
            type=str,
            help="""Attempt to process files in the current dir into a soundtrack track.
                Loops through as many variants as possible, per part.
                String should be the output filename""",
            )

    action.add_argument('--soundtrack-simple',
            type=str,
            help="""Attempt to process files in the current dir into a soundtrack track.
                Just picks a single variant for each part.
                String should be the output filename""",
            )

    action.add_argument('--soundtrack-leadin',
            type=str,
            help="""Attempt to process files in the current dir into a soundtrack track.
                Handles soundtracks which have a "lead-in" at the beginning, and processes
                similarly to the non-simple soundtrack version.
                String should be the output filename""",
            )

    action.add_argument('--gen-leadin-randoms',
            action='store_true',
            help="""Given a collection of leadin-based TXTPs, generate a set of leadin+body
                TXTPs for each random possibility (not, like, permutations, but just N
                files where N is the max randomization for a single group).""",
            )

    # Non-action args follow

    parser.add_argument('-i', '--include-comments',
            action='store_true',
            help="Include TXTP comments in output, if present",
            )

    parser.add_argument('--lowest-random',
            action='store_true',
            help="""When in simple soundtrack mode, choose the lowest random element,
                rather than the highest (for some collections, this might lead to
                more "exciting" tracks).""",
            )

    parser.add_argument('--schema',
            type=str,
            help="""Comma-separated segment list to use in soundtrack-leadin mode.
                Has no effect in other modes.  Without this option, a hardcoded list
                will be used instead, which is unlikely to make sense (or even work)
                with arbitrary music sets.""",
            )

    parser.add_argument('-n', '--nofade',
            dest='fadeout',
            action='store_false',
            help="""When processing soundtracks, don't fade out -- instead, allow the
                full end-of-track to play.""",
            )

    parser.add_argument('--nopad',
            dest='padding',
            action='store_false',
            help="""Don't add 2 seconds of padding at the end of soundtrack processing
                Currently does not apply to leadin soundtracks.""",
            )

    parser.add_argument('--random-count',
            type=int,
            help='In basic soundtrack mode, override our detected min. random count.',
            )

    args = parser.parse_args()

    if args.check:

        # Check all .txtp in the current dir to make sure we can load
        # (and then render) each one.
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp'):
                print(filename)
                txtp = Txtp.from_file(filename)
                txtp.to_string(args.include_comments)

    elif args.split:

        # Split top-level "segment" groups apart into separate .txtp
        # (will effectively be a noop for layer/random groups, or for
        # TXTPs with just a file at the top level)
        txtp = Txtp.from_file(args.split)
        if type(txtp.root) == Group and (txtp.root.group_type == GroupType.SEGMENT or
                (txtp.root.group_type == GroupType.RANDOM and txtp.root.random_selection == '-')):
            for idx, part in enumerate(txtp.root.contents):

                # If the main layer has a volume but this part doesn't,
                # go ahead and assign it.  (Don't bother with percentage volumes
                # in here; they don't show up in the files we care about.)
                if txtp.root.volume is not None and part.volume is None:
                    part.volume = txtp.root.volume

                # (this is fixed now!  Leaving in here for reference though)
                # vgm123 can't seem to cope with a file whose top-level
                # element is a Layer group (Random seems fine, File seems
                # fine, and Segment seems fine, and both Audacious and
                # vgmstream_cli don't mind at all).  Anyway, if this part
                # is a Layer group, wrap it up in a Segment group.
                # https://github.com/vgmstream/vgmstream/issues/901
                #if type(part) == Group and part.group_type == GroupType.LAYER:
                #    part = Group(GroupType.SEGMENT, [part])

                # Write out
                filename = '{}.txtp'.format(idx+1)
                new_txtp = Txtp(part)
                with open(filename, 'w') as odf:
                    odf.write(new_txtp.to_string(args.include_comments))
                print('Wrote segment to: {}'.format(filename))
        else:
            with open('1.txtp', 'w') as odf:
                odf.write(txtp.to_string())
            print('Single segment written to: 1.txtp')

    elif args.output:

        # Just output our own representation of the file, for spot checks.
        txtp = Txtp.from_file(args.output)
        print(txtp.to_string(args.include_comments))

    elif args.find_leadins:

        # Finding files which might have leadin-type intros
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp'):
                txtp = Txtp.from_file(filename)
                if type(txtp.root) == Group and txtp.root.group_type == GroupType.SEGMENT:
                    if len(txtp.root.contents) > 1:
                        files = [set(), set()]
                        comps = [None, None]
                        for idx in 0, 1:
                            inner = txtp.root.contents[idx]
                            if type(inner) == Group and inner.group_type == GroupType.LAYER:
                                for real_inner in inner.contents:
                                    if type(real_inner) == File:
                                        files[idx].add(real_inner.filename)
                                        if idx == 0 and real_inner.trim_end is not None:
                                            comps[idx] = real_inner.trim_end
                                        elif idx == 1 and real_inner.trim_beginning is not None:
                                            comps[idx] = real_inner.trim_beginning
                        if files[0] == files[1] and comps[0] != comps[1]:
                            print(filename)

    elif args.do_transforms:

        # My usual suite of post-extraction transforms (will always write out
        # comments)
        deleted = 0
        normalized = 0
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp'):
                if '=Off' in filename:
                    # Delete anything with =Off in the title.  For the set of files
                    # I care about, these are completely pointless.
                    os.unlink(filename)
                    deleted += 1
                else:
                    # Otherwise, run through our normalizations.  This might not
                    # actually make changes to every file, but we're blindly writing
                    # out the updates anyway.
                    txtp = Txtp.from_file(filename)
                    volume_nodes = []

                    # Do transforms, though we have to gather some volume info
                    # for the whole tree until we do that.
                    do_transforms(txtp.root, volume_nodes, is_root=True)

                    # Volume updates -- always set the root if it's set there;
                    # set inner nodes if there's only a single one
                    if txtp.root.volume is None:
                        if len(volume_nodes) == 1:
                            volume_nodes[0].set_volume(0)
                    else:
                        txtp.root.set_volume(0)

                    # Now write out.
                    with open(filename, 'w') as odf:
                        odf.write(txtp.to_string(True))
                    normalized += 1

        print('Deleted {} files, Normalized {} files'.format(deleted, normalized))

    elif args.soundtrack:

        # Attempt to make a soundtrack out of these
        min_random = 9999
        rand_hist = {}
        parts = []
        filenames = []
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp'):
                txtp = Txtp.from_file(filename)
                assert(type(txtp.root) == Group)
                assert(txtp.root.group_type == GroupType.LAYER)
                parts.append(txtp.root)
                filenames.append(filename)
                for layer in txtp.root.contents:
                    if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                        this_random = len(layer.contents)
                        min_random = min(min_random, this_random)
                        if this_random in rand_hist:
                            rand_hist[this_random] += 1
                        else:
                            rand_hist[this_random] = 1

        # Report on what we found out randomwise
        print('Got min. random count of {}'.format(min_random))
        for rand_num, count in sorted(rand_hist.items()):
            print(' - {}-Random Sections: {}'.format(rand_num, count))
        if args.random_count is not None:
            print('Overriding random count to: {}'.format(args.random_count))
            min_random = args.random_count

        # Now create a new TXTP and output
        new_root = Group(GroupType.SEGMENT)
        new_txtp = Txtp(new_root)
        # Duplicate each part `min_random` times, selecting random elements
        # from the bottom up (since that *seems* to maybe increase in
        # excitement each time?).  On the *first* pass, always choose the
        # bottom-most layer.  We're actually going to level up the
        # "excitement" in chunks, so we loop through all parts, *then*
        # jump up the excitement level and loop through 'em all again.
        for rand_idx in range(min_random, 0, -1):
            for part_idx, part in enumerate(parts):
                new_part = part.copy()
                new_root.contents.append(new_part)
                for layer in new_part.contents:
                    if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                        this_count = len(layer.contents)
                        if rand_idx == min_random:
                            layer.random_selection = len(layer.contents)
                        else:
                            layer.random_selection = min(rand_idx, len(layer.contents))

                # If we're the very last one, do a fadeout or a stop, depending.
                if rand_idx == 1 and part_idx == (len(parts)-1):
                    if args.fadeout:
                        # Leave the default fade_period as 10, I guess
                        new_part.loop = True
                        new_part.num_loops = 1
                        new_part.fade_period = 10
                    else:
                        # "Hard" stop, but let the entire .wem play.
                        new_part.remove_length()

        # Add a couple seconds of silence at the end
        if args.padding:
            new_root.pad_end = 2
        new_root.ignore_loops = True

        # May as well comment that we generated it
        if args.fadeout:
            extra = ''
        else:
            extra = ' (without fadeouts)'
        if not args.padding:
            extra = '{} (without padding)'.format(extra)
        if args.random_count is not None:
            extra = '{} (with forced random count {})'.format(extra, args.random_count)
        new_txtp.comments.append('# Generated by txtp_process.py, in soundtrack mode{}, from the following:'.format(extra))
        new_txtp.comments.append('#')
        for filename in filenames:
            new_txtp.comments.append('#  - {}'.format(filename))
        new_txtp.comments.append('#')

        # Now write it out
        with open(args.soundtrack, 'w') as odf:
            odf.write(new_txtp.to_string(do_comments=True))
        print('Wrote to: {}; {} parts'.format(args.soundtrack, len(new_root.contents)))

    elif args.soundtrack_simple:

        # Attempt to make a soundtrack out of these
        # This variant doesn't futz around with looping over random selections;
        # just hardcodes a single one and concats.

        # Create a new TXTP and output
        new_root = Group(GroupType.SEGMENT)
        new_txtp = Txtp(new_root)

        # Loop over files
        filenames = []
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp'):
                txtp = Txtp.from_file(filename)
                assert(type(txtp.root) == Group)
                assert(txtp.root.group_type == GroupType.LAYER)
                filenames.append(filename)
                new_part = txtp.root.copy()
                new_root.contents.append(new_part)
                for layer in new_part.contents:
                    if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                        if args.lowest_random:
                            layer.random_selection = 1
                        else:
                            layer.random_selection = len(layer.contents)

        # Process the ending
        if args.fadeout:
            # Fade out with a loop (though we're only looping once)
            new_part.loop = True
            new_part.num_loops = 1
            new_part.fade_period = 10
        else:
            # "Hard" stop, but let the entire .wem play
            new_part.remove_length()

        # Add a couple seconds of silence at the end
        if args.padding:
            new_root.pad_end = 2
        new_root.ignore_loops = True

        # May as well comment that we generated it
        if args.lowest_random:
            extra = ' (with --lowest-random)'
        else:
            extra = ''
        if not args.fadeout:
            extra = '{} (without fadeouts)'.format(extra)
        if not args.padding:
            extra = '{} (without padding)'.format(extra)
        new_txtp.comments.append('# Generated by txtp_process.py, in simple soundtrack mode{}, from the following:'.format(extra))
        new_txtp.comments.append('#')
        for filename in filenames:
            new_txtp.comments.append('#  - {}'.format(filename))
        new_txtp.comments.append('#')


        # Now write it out
        with open(args.soundtrack_simple, 'w') as odf:
            odf.write(new_txtp.to_string(do_comments=True))
        print('Wrote to: {}; {} parts'.format(args.soundtrack_simple, len(new_root.contents)))

    elif args.soundtrack_leadin:

        # Constructing soundtracks with "leadin"-based audio files.  This is more
        # complex than other methods because we've got to mix in the leadins when
        # "looping" the segments.  So we've got some class-based shenanigans to
        # help abstract that out.
        #
        # This makes all sorts of assumptions about the structure of our input
        # TXTP files, but it works fine for the small pool of audio sources that
        # I'm interested, so it's Good Enough For Me.

        class Choice:

            def __init__(self, leadin, body, cue, section, part, num):
                self.leadin = leadin
                self.body = body
                self.cue = cue
                self.section = section
                self.part = part
                self.num = num
                self.name = None

                self.leadin_length = self._find_length(self.leadin)
                self.body_length = self._find_length(self.body)

            def __lt__(self, other):
                if self.section < other.section:
                    return True
                if self.part < other.part:
                    return True
                return self.num < other.num

            def _find_length(self, component):
                if type(component) == File:
                    if component.length is not None:
                        return component.length
                else:
                    for item in component.contents:
                        rv = self._find_length(item)
                        if rv is not None:
                            return rv
                return None

            @staticmethod
            def _set_random(component, rand_val, max_random):
                for layer in component.contents:
                    if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                        layer.random_selection = math.floor((rand_val/max_random)*len(layer.contents))+1

            @staticmethod
            def from_orig(leadin_in, body_in, rand_val, max_random, cue, section, part):
                leadin = leadin_in.copy()
                body = body_in.copy()
                Choice._set_random(leadin, rand_val, max_random),
                Choice._set_random(body, rand_val, max_random),
                return Choice(leadin, body,
                        cue, section, part, rand_val+1,
                        )

        class Mix:

            def __init__(self):
                self.choices = {}
                self.sections = {}

            def add_choice(self, choice):
                name = 's{}p{}n{}'.format(
                        choice.section,
                        choice.part,
                        choice.num,
                        )
                choice.name = name
                self.choices[name] = choice

                # may as well do this kind of thing too
                if choice.section not in self.sections:
                    self.sections[choice.section] = {}
                if choice.part not in self.sections[choice.section]:
                    self.sections[choice.section][choice.part] = {}
                self.sections[choice.section][choice.part][choice.num] = choice

            def __getitem__(self, key):
                return self.choices[key]

            def combine_leadin(self, body_choice, leadin_choice):

                group = Group(GroupType.LAYER)
                group.layer_channels = True
                group.contents.append(body_choice.body.copy())
                group.contents.append(leadin_choice.leadin.copy())
                group.contents[1].pad_beginning = body_choice.body_length - (2*leadin_choice.leadin_length)
                return group

            def create_chain(self, itemnames, fadeout=True):

                root = Group(GroupType.SEGMENT)
                txtp = Txtp(root)
                
                total_items = len(itemnames)
                for item_idx, itemname in enumerate(itemnames):

                    choice = self.choices[itemname]

                    # If we're the first item, use the unaltered lead-in
                    if item_idx == 0:
                        root.contents.append(choice.leadin.copy())

                    if item_idx+1 < total_items:
                        # If we're not the *last* item, mix in the next track's
                        # lead-in.
                        root.contents.append(self.combine_leadin(choice, self.choices[itemnames[item_idx+1]]))
                    else:
                        # This is the last track; handle the ending.
                        if fadeout:
                            # Mix with our own leadin, loop once, and fade out over half the
                            # length of the segment.
                            root.contents.append(self.combine_leadin(choice, choice))
                            root.contents[-1].loop = True
                            root.contents[-1].num_loops = 1
                            root.contents[-1].fade_period = choice.body_length/2

                        else:
                            # Let the whole part play out; these tracks seem to have an extra ending
                            # tacked on there which sounds pretty good when left in.
                            ending = choice.body.copy()
                            ending.remove_length()
                            root.contents.append(ending)

                # Add some padding, and make sure that we don't try to loop anything else.
                # (The ignore_loops here doesn't matter unless `fadeout` is specified, but it won't hurt.)
                root.pad_end = 2
                root.ignore_loops = True

                # Return
                return txtp

        # Mus_Prologue_Play (Mus_System_Sections=Mus_Section_01)(Mus_System_Parts=Mus_Part_04) {s} {r}.txtp
        file_re = re.compile("""^
                (?P<cue>\S+)\s+
                \(Mus_System_Sections=Mus_Section_(?P<section>\d+)\)
                \(Mus_System_Parts=Mus_Part_(?P<part>\d+)\)
                .*\.txtp$""", re.VERBOSE)

        # Load in all the matching .txtps in our dir
        mix = Mix()
        found_cue = None
        found_filenames = set()
        for filename in sorted(os.listdir('.')):
            if match := file_re.match(filename):
                cue = match.group('cue')
                if found_cue is None:
                    found_cue = cue
                else:
                    assert(found_cue == cue)
                section = int(match.group('section'))
                part = int(match.group('part'))

                # Load the file and do some initial assertations
                txtp = Txtp.from_file(filename)
                assert(type(txtp.root) == Group)
                assert(txtp.root.group_type == GroupType.SEGMENT)
                assert(len(txtp.root.contents) == 2)
                for content in txtp.root.contents:
                    assert(type(content) == Group)
                    assert(content.group_type == GroupType.LAYER)
                assert(len(txtp.root.contents[0].contents) == len(txtp.root.contents[1].contents))
                found_filenames.add(filename)

                # We're going to make an extra implicit assumption here that that the
                # max. random characteristics of both the leadin and body are the same.
                leadin = txtp.root.contents[0]
                body = txtp.root.contents[1]

                # First figure out the max. random count for this part
                max_random = 0
                for layer in body.contents:
                    if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                        max_random = max(max_random, len(layer.contents))

                # Now generate N random Choices for this
                if max_random == 0:
                    # This happens in Motorcade section 0, at least.  c'est la vie
                    mix.add_choice(Choice.from_orig(leadin, body,
                        0, 1,
                        cue, section, part))
                else:
                    for rand_val in range(max_random):
                        mix.add_choice(Choice.from_orig(leadin, body,
                            rand_val, max_random,
                            cue, section, part))

        # Report on what we found
        print('Processing for cue: {}'.format(found_cue))
        for section, parts in sorted(mix.sections.items()):
            print('> Section {}'.format(section))
            for part, randoms in sorted(parts.items()):
                print('  - Part {} ({:0.1f}s): {}'.format(
                    part,
                    list(randoms.values())[0].body_length,
                    ', '.join([r.name for r in sorted(randoms.values())]),
                    ))

        # Figure out which choices we've made
        if args.schema:
            chain = [s.strip() for s in args.schema.split(',')]
        else:
            chain = [
                    # used for Mus_Prologue_Play section 1 (the random nums themselves chosen basically at random)
                    #'s1p0n2', 's1p0n1',
                    #'s1p1n2', 's1p1n5',
                    #'s1p2n3', 's1p2n6',
                    #'s1p3n6', 's1p3n8',
                    #'s1p4n3', 's1p4n9',
                    #'s1p5n3', 's1p5n2',

                    # used for Mus_Prologue_Play section 3 (omitting part 2 entirely; it stands out too much)
                    #'s3p0n2', 's3p1n2', 's3p3n2', 's3p4n2', 's3p5n2', 's3p6n2',
                    #'s3p0n1', 's3p1n1', 's3p3n1', 's3p4n1', 's3p5n1', 's3p6n1',

                    # used for Mus_Motorcade_Start section 0
                    #'s0p1n1', 's0p2n1', 's0p3n1', 's0p4n1', 's0p5n1', 's0p6n1', 's0p7n1', 's0p8n1', 's0p9n1', 's0p10n1',

                    # used for Mus_Motorcade_Start sections 1+2+3 (they work quite well together)
                    's1p0n1', 's1p1n1', 's1p2n1', 's1p3n1', 's1p4n1', 's1p5n1', 's1p6n1', 's1p7n1',
                    's2p0n1', 's2p1n1', 's2p2n1', 's2p3n1', 's2p4n1',
                    's3p0n1', 's3p1n1', 's3p2n1', 's3p3n1', 's3p4n1',
                    ]
        print('Using parts: {}'.format(', '.join(chain)))

        # Finally, generate.
        txtp = mix.create_chain(chain, args.fadeout)

        # Add some comments
        if args.fadeout:
            extra = ''
        else:
            extra = ' (without fadeouts)'
        txtp.comments.append('# Generated by txtp_process.py, in leadin soundtrack mode{}, from the following:'.format(extra))
        txtp.comments.append('#')
        for filename in sorted(found_filenames):
            txtp.comments.append('#  - {}'.format(filename))
        txtp.comments.append('#')
        txtp.comments.append('# Using the following schema:')
        txtp.comments.append('#')
        txtp.comments.append('#    {}'.format(','.join(chain)))
        txtp.comments.append('#')

        # Write to disk
        with open(args.soundtrack_leadin, 'w') as odf:
            odf.write(txtp.to_string(do_comments=True))
        print('Wrote to: {}, with {} parts'.format(args.soundtrack_leadin, len(chain)))

    elif args.gen_leadin_randoms:

        # Explode our "leadin"-based tracks' random components into constituent parts
        found = 0
        written = 0
        for filename in sorted(os.listdir('.')):
            if filename.endswith('.txtp') and '-body-' not in filename and '-leadin-' not in filename:
                txtp = Txtp.from_file(filename)
                assert(type(txtp.root) == Group)
                assert(txtp.root.group_type == GroupType.SEGMENT)
                assert(len(txtp.root.contents) == 2)
                for content in txtp.root.contents:
                    assert(type(content) == Group)
                    assert(content.group_type == GroupType.LAYER)
                filename_base = filename[:-5]
                found += 1

                for part_idx, filename_label in [
                        (0, 'leadin'),
                        (1, 'body'),
                        ]:
                    part = txtp.root.contents[part_idx]

                    # First figure out our max. random count for this part
                    max_random = 0
                    for layer in part.contents:
                        if type(layer) == Group and layer.group_type == GroupType.RANDOM:
                            max_random = max(max_random, len(layer.contents))

                    # Now loop through again and write 'em out
                    for rand_val in range(max_random):
                        filename_new = '{}-{}-{}.txtp'.format(
                                filename_base,
                                filename_label,
                                rand_val+1,
                                )
                        new_root = Group(GroupType.LAYER)
                        new_root.layer_channels = True
                        new_txtp = Txtp(new_root)
                        rand_pct = rand_val/max_random

                        for layer in part.contents:
                            new_part = layer.copy()
                            new_root.contents.append(new_part)
                            if type(new_part) == Group and new_part.group_type == GroupType.RANDOM:
                                new_part.random_selection = math.floor(rand_pct*len(new_part.contents))+1

                        with open(filename_new, 'w') as odf:
                            odf.write(new_txtp.to_string())
                        written += 1

        print('Found {} TXTPs, wrote {} variants'.format(found, written))

