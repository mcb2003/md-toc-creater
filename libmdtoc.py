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

# import the sys module for standard IO and the re module for parsing regular expressions.
import sys, re
# Import some bits and pieces from the typing module to be used with type hints
from typing import List, IO, Union

# This variable is a type hint alias that defines a list of words.
Strings = List[str]
# This alias specifies a type of either a file object or a string (path to a file).
File = Union[str, IO['TextIO']]

# Create the MDTOCItem class, which represents an item on the table of contents.
class MDTOCItem(object):
  # This is the constructor function, which sets up the object.
  def __init__(self, level: int, title: Strings, min_indent: int=1):
# Set some important properties.
    self.level: int = level
    self.title: Strings = title
    self.min_indent: int = min(1, min_indent)
  
# This function joins a given list of strings with a given separator.
  def join(self, words: Strings, separator: str=" ") -> str:
    # Initialise the text variable to an empty string.
    text: str = ""
    # Loop through each of the words.
    for word in words:
      # Append the word, as well as a proceeding separator, to the text variable.
      text += separator + word
    # Remove the first proceeding separator from text and then return it.
    separator_end: int = len(separator)
    text = text[separator_end:]
    return text
  
# This function returns a non-linked list item representing this list item. 
  def get_list_item_nonlinked(self) -> str:
# First, get a textual representation of the title.
    title_text: str = self.join(self.title, " ")
# Next, create white space based on the level of the item and the minimum indent level.
    whitespace: str = "\t" * (self.level - self.min_indent)
# Finally, return the full list item.
    return whitespace + "* " + title_text
  
  # This function returns a linked list item representing this list item. 
  def get_list_item_linked(self) -> str:
# First, get a textual representation of the title.
    title_text: str = self.join(self.title, " ")
# Also, get a textual representattion of a link reference to this heading.
    title_reference: str = "#" + self.join(self.title, "-").lower()
# Next, create white space based on the level of the item and the minimum indent level.
    whitespace: str = "\t" * (self.level - self.min_indent)
# Finally, return the full list item.
    return whitespace + "* [" + title_text + "](" + title_reference + ")"

  
# Create the MDTOC class, which handles everything to do with the table of contents.
class MDTOC(object):
  # Define the constructor function.
  def __init__(self, file: File, linked: bool=False, min_indent: int=1):
# Set some important properties.
    self.linked: bool = linked
    self.min_indent: int = min(1, min_indent)
    # Set the lines' property based on the return value of the get_file_contents function.
    self.lines: Strings = self.get_file_contents(file)
    # Create the regexp object used to match lines.
    self.heading_re = re.compile("^\s*#+\\s.*$")
    # This list will hold each matched line.
# Call the 'get_headings' function to get all headings from the document.
    self.headings: Strings = self.get_headings()
    # Next, get a list of MDTOCItems using the 'get_items' function.
    self.items = self.get_items()
  
# This function uses re to find all headings within the markdown document.
  def get_headings(self) -> Strings:
# Initialise the list of headings.
    headings: Strings = []
    # Loop through all the lines of the file.
    for line in self.lines:
      # Trim out any unneeded whitespace.
      line = line.strip()
      # Match the line to the heading re.
      match = self.heading_re.match(line)
      # Check if this line matches the heading pattern.
      if bool(match) == True:
        # We have a match, so add it to our list of headings.
        headings.append(line)
# Return the list of headings.
    return headings
  
  # This function generates and returns a list of MDTOCItem objects to be used to generate the table of contents.
  def get_items(self) -> List[MDTOCItem]:
# Initialise the items list.
    items: List[MDTOCItem] = []
    # Now that we have all the headings in the document, loop through them.
    for heading in self.headings:
      # Find out what level of heading this is by getting the amount of '#' characters at the start.
      whitespace_re = re.compile("\s")
      words: Strings = whitespace_re.split(heading)
      level: int = len(words[0])
      # Next, create an MDTOCItem object representing this item.
      li: MDTOCItem = MDTOCItem(level, words[1:], self.min_indent)
      items.append(li)
    # Finally, return the list of list items.
    return items
  
# This function takes either a path or a file object, returning always the file's contents.
  def get_file_contents(self, file: File) -> Strings:
    # Check if the passed 'file' argument is a string.
    if type(file) == str:
      # It is, so open a file with this path.
      file: IO['TextIO'] = open(file, "r")
    # We've got a file object regardless now, so return it's contents as a list of lines.
    text: str = file.read()
    lines: Strings = text.split("\n")
    return lines
  
  # This function returns the markdown representation of the table of contents.
  def get_toc(self) -> Strings:
    # Initiate the text variable to hold the returned TOC.
    lines: Strings = []
    # Loop through all of the list items in the items list.
    for item in self.items:
      # Check whether we need to return linked or non-linked list items as part of the TOC.
      if self.linked == False:
      # Append the returned text of the current item's to the lines list.
        lines.append(item.get_list_item_nonlinked())
      # If we do want links:
      else:
      # Append the returned text of the current item's to the lines list.
        lines.append(item.get_list_item_linked())
    # Finally, return the lines.
    return lines
