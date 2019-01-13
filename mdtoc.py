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

# import the sys module for standard IO and the re module for parsing regular expressions
import sys, re

# Create the regexp object used to match lines.
heading_re = re.compile("^\s*#+\\s.*$")
# This list will hold each matched line.
headings = []

# Loop through all the lines of standard input
for line in sys.stdin.read().split("\n"):
  # Trim out any unneeded whitespace.
  line = line.strip()
  # Match the line to the heading re.
  match = heading_re.match(line)
  # Check if this line matches the heading pattern.
  if bool(match) == True:
    # We have a match, so add it to our list of headings.
    headings.append(line)

print(headings)
