# MD TOC
  A tool to create tables of contents from markdown files, in markdown format.

## Introduction

  MD TOC is a tool written in python that adheres to the old unix-philosophy of doing one thing and one thing well. It reads a given markdown file (or standard input) and produces a table of contents, with or without links, for the given markdown document, in markdown format, based on any headings that may exist in the document, as well as their level. The list items within the table of contents are indented depending on the heading level. How much each level is indented is also determined by the min-heading-indent option.

## Usage Information

```
    $ ./mdtoc.py -h
usage: MD TOC [-h] [-n] [-m {1,2,3,4,5,6}] [-M {0,1,2,3,4,5,6}] [-x LEVEL]
              [input]

Generate a table of contents for a markdown document

positional arguments:
  input                 The markdown file to read.

optional arguments:
  -h, --help            show this help message and exit
  -n, --no-links        Do not link the sections of the document to their list
                        items in the table of contents.
  -m {1,2,3,4,5,6}, --min-indent {1,2,3,4,5,6}
                        Specify the minimum level of heading for which the
                        list items will be indented. Headings at or below this
                        level will not be indented and the rest of the heading
                        levels will be adjusted accordingly. The default is 1.
  -M {0,1,2,3,4,5,6}, --max-indent {0,1,2,3,4,5,6}
                        Specify the maximum level of heading for which the
                        list items will be indented. Headings above this level
                        will not be indented any further; Thus, specifying 0
                        flattens the list. The default is 6.
  -x LEVEL, --exclude LEVEL
                        Specify specific levels of heading to exclude from the
                        table of contents. This option can be repeated to
                        exclude multiple levels.

Submit any bugs to https://github.com/mcb2003/md-toc-creater/issues/new
```