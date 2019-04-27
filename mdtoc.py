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
# This argument defines what file (default stdout) to write the TOC to.
arg_parser.add_argument("input",
                        help="The markdown file to read.",
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs="?"
                        )
# This argument specifies whether to output the TOC items as links to their sections or as simple plane text.
arg_parser.add_argument("-n", "--no-links",
                        help="Do not link the sections of the document to their list items in the table of contents.",
                        action="store_true"
                        )
# This argument defines the minimum heading level for which the indentation will be 0. Headings at or below this level will not be indented.
arg_parser.add_argument("-m", "--min-indent",
                        help="Specify the minimum level of heading for which the list items will be indented. Headings at or below this level will not be indented and the rest of the heading levels will be adjusted accordingly. The default is 1.",
                        type=int,
                        choices=range(1, 7),
                        default=1
                        )


# Parse the arguments passed to the script.
args = arg_parser.parse_args()

# Create an MDTOC object with the parsed options.
tocobj: libmdtoc.MDTOC = libmdtoc.MDTOC(
    args.input, not args.no_links, args.min_indent)
# Get the text representing the contents and print it to the standard output.
text = tocobj.get_toc()
print(text)
