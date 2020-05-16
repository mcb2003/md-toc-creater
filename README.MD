# MD TOC
  A tool to create tables of contents from markdown files, in markdown
  format.

## Introduction

  md-toc-creator is a tool written in python that adheres to the old
  Unix philosophy of doing one thing and one thing well. It reads a given
  markdown file (or standard input) and produces a table of contents. The
  TOC can be generated  with or without links, in markdown format, based
  on any headings that may exist in the document, as well as their level.

## Usage Information

```bash
    ./mdtoc.py -h
```

    usage: MD TOC [-h] [-m {1,2,3,4,5,6}] [-M {0,1,2,3,4,5,6}] [-n] [-o OUTPUT]
                  [-s SEPARATOR] [-w WHITESPACE] [-x LEVEL]
                  [input]

    Generate a table of contents for a markdown document

    positional arguments:
      input                 The markdown file to read.

    optional arguments:
      -h, --help            show this help message and exit
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
      -n, --no-links        Do not link the sections of the document to their list
                            items in the table of contents.
      -o OUTPUT, --output OUTPUT
                            The markdown file to write the table of contents to.
                            The default is standard output.
      -s SEPARATOR, --separator SEPARATOR
                            Specifies a string to be used as the separator between
                            the '*' character and the succeeding list item
                            (default: ' ').
      -w WHITESPACE, --whitespace WHITESPACE
                            Specify the characters used as whitespace before each
                            item. This is repeated or omitted depending on the
                            indentation level of each item. (default: ' ')
      -x LEVEL, --exclude LEVEL
                            Specify specific levels of heading to exclude from the
                            table of contents. This option can be repeated to
                            exclude multiple levels.

    Submit any bugs to https://github.com/mcb2003/md-toc-creater/issues/new
