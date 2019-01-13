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
import argparse, sys

arg_parser = argparse.ArgumentParser("MD TOC",
    description="Generate a table of contents for a markdown document",
  epilog="Submit any bugs to https://github.com/mcb2003/md-toc-creater/issues/new"
)
arg_parser.add_argument("file",
  help="The file to output the table of contents to. By default, output to standard output.",
  type=argparse.FileType('w'),
  default=sys.stdout,
  nargs="?"
)
arg_parser.add_argument("-n", "--no-links",
  help="Do not link the sections of the document to their list items in the table of contents.",
  action="store_true"
)
args = arg_parser.parse_args()
