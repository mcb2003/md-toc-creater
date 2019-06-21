#!/usr/bin/env python3

#    mdtoc: Generates a table of contents for a markdown document in markdown.
#    Copyright (C) 2019 Michael Connor Buchan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# include the needed library file.
import libmdtoc
# Also include the argparse module to parse command line arguments and sys to get access to stdio.
import argparse
import sys

# Create an ArgumentParser object to parse the command line arguments.
arg_parser = argparse.ArgumentParser("MD TOC",
                                     description="Generate a table of contents for a markdown document",
                                     epilog="Submit any bugs to https://github.com/mcb2003/md-toc-creater/issues/new"
                                     )
# This argument defines what file (default stdin) to read  the TOC from.
arg_parser.add_argument("input",
                        help="The markdown file to read.",
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs="?"
                        )
# This argument defines the minimum heading level for which the indentation will be 0.
# Headings at or below this level will not be indented.
arg_parser.add_argument("-m", "--min-indent",
                        help="Specify the minimum level of heading for which the list items will be indented. Headings at or below this level will not be indented and the rest of the heading levels will be adjusted accordingly. The default is 1.",
                        type=int,
                        choices=range(1, 7),
                        default=1
                        )
# This argument specifies the maximum level of heading for which the list items will be indented.
# Headings above this level will not be indented any further; Thus, specifying 0 flattens the list.
arg_parser.add_argument("-M", "--max-indent",
                        help="Specify the maximum level of heading for which the list items will be indented. Headings above this level will not be indented any further; Thus, specifying 0 flattens the list. The default is 6.",
                        type=int,
                        choices=range(0, 7),
                        default=6
                        )
# This argument specifies whether to output the TOC items as links to their sections or as simple plane text.
arg_parser.add_argument("-n", "--no-links",
                        help="Do not link the sections of the document to their list items in the table of contents.",
                        action="store_true"
                        )
# This argument defines what file (default stdout) to write   the TOC to.
arg_parser.add_argument("-o", "--output",
                        help="The markdown file to write the table of contents to. The default is standard output.",
                        type=argparse.FileType('w'),
                        default=sys.stdout
                        )
# This argument allows the exclusion of specific heading levels from the TOC.
# It can be repeated to exclude multiple levels.
arg_parser.add_argument("-x", "--exclude",
                        help="Specify specific levels of heading to exclude from the table of contents. This option can be repeated to exclude multiple levels.",
                        metavar="LEVEL",
                        type=int,
                        action="append",
                        default=[]
                        )


# Parse the arguments passed to the script.
args = arg_parser.parse_args()

# Create an MDTOC object with the parsed options.
tocobj: libmdtoc.MDTOC = libmdtoc.MDTOC(
    args.input, not args.no_links, args.min_indent, args.max_indent, args.exclude)
# Get the text representing the contents and print it to the standard output or the specified file.
text: str = tocobj.get_toc()
print(text, file=args.output)
