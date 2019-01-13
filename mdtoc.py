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

## Function Definitions:

# This function joins a given list of strings with a given separator.
def join(words, separator):
  # Initialise the text variable to an empty string.
  text = ""
  # Loop through each of the words.
  for word in words:
    # Append the word, as well as a proceeding separator, to the text variable.
    text += separator + word
  # Remove the first proceeding separator from text and then return it.
  separator_end = len(separator)
  text = text[separator_end:]
  return text


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

# Now that we have all the headings in the document, loop through them.
for heading in headings:
  # Find out what level of heading this is by getting the amount of '#' characters at the start.
  whitespace_re = re.compile("\s")
  words = whitespace_re.split(heading)
  level = len(words[0])
# This level will determine the indentation of our list item, so create this whitespace now.
  whitespace = "\t" * (level - 1)
# Create the text for the list item using the join function we made earlier.
  text = join(words[1:], " ")
# Finally, print out the list item.
  print(whitespace + "* " + text)
