#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#     
# \file
#       body.py
# \author
#       Marcus Lunden <marcus.lunden@bithappens.com>
# \desc
#     This prints a number of lines from the eg middle of a textfile.
#     
#     Examples:
#       print line 17 and 30 more:
#           body 17 30 helloworld.c
#       print line 17 and default more (20)
#           body 17 helloworld.c
#       print line 17 and end at 30
#           body 17 e30 helloworld.c
#     
#     Motivation - head and tail in linux are great for printing a number of lines
#     from the start or the end of a file, but I ran into a 15kLOC file where I
#     wanted to see the lines around 10k, as my text editor was too slow to render
#     the file efficiently due to syntax highlighting. Some shell ninjary would've
#     done it, but this was more fun to do and I can expand it later should I feel
#     like it.
#     
#     Make sure it's executable (chmod +x plines.py) and alias to it so it can be
#     called from anywhere (alias plines='~/tools/plines.py')
#     
#     Todo:
#       add spaces for linenumbering so that the start lines line up
#       make explicit line-numbering at start of print optional
#       make colors optional through option
#       better, ie more flexible, arguments parsing with argparse
# 
import sys
import os

EXECUTION_SUCCESS                 = 0
ERR_ARGS_TOO_FEW_OR_MANY          = 1
ERR_ARGS_INTEGER_ERROR            = 2
ERR_ARGS_FILE_DOES_NOT_EXIST      = 3
ERR_FILE_READ_ERROR               = 4
ERR_UNKNOWN_ERROR                 = 99

DEFAULT_LINES_TO_READ = 20    # default read 20 lines, if not specified elsewhise

# change this for use of colors or not
use_color = True
#use_color = False

#-------------------------------------------------------------------------------
def bailout(errstr = "", exitcode = 0):
  if exitcode != 0:
    print("Print lines in the middle of a file; like a combination of 'head' and 'tail' in Linux")
    print("usage: " + sys.argv[0] + " LINESTART <LINEEND> FILE")
    print("Examples:----------")
    print("  Print line 17--67 from helloworld.c")
    print("     " + sys.argv[0] + " 17 50 helloworld.c")
    print("")
    print("  Print line 17--20 from helloworld.c")
    print("     " + sys.argv[0] + " 17 e20 helloworld.c")
    print("")
    print("  Print line 17--37 from helloworld.c (per default 20 lines are read)")
    print("     " + sys.argv[0] + " 17 helloworld.c")
    print("")
    print("  Print line 17--end of helloworld.c (effectively 'tail')")
    print("     " + sys.argv[0] + " 17 - helloworld.c")
    print("")
    print("  Print line 1--17 of helloworld.c (effectively 'head')")
    print("     " + sys.argv[0] + " - 17 - helloworld.c")
    print("")
    print("*** Error ***: " + errstr),
  sys.exit(exitcode)
# ------------------------------------------------------------------------------
def main():
  # set up defaults------------------------------
  if use_color:
    RED = '\x1b[31m' # red
    YELLOW = '\x1b[33m' # yellow
    GRN = '\x1b[32m' # green 
    PINK = '\x1b[35m' # pink
    NRM = '\x1b[0m' # normal
  else:
    RED = ''
    YELLOW = ''
    GRN = ''
    PINK = ''
    NRM = ''

  # parse input arguments---------------------------------
  # number of arguments
  if len(sys.argv) == 1:
    # nothing to do here, carry on
    bailout("", EXECUTION_SUCCESS)
  if len(sys.argv) < 3:
    bailout("too few args", ERR_ARGS_TOO_FEW_OR_MANY)
  if len(sys.argv) > 4:
    bailout("too many args", ERR_ARGS_TOO_FEW_OR_MANY)


  # lines to print
  try:
    if sys.argv[1].count('-') > 0:
      linestart = 0
    else:
      linestart = int(sys.argv[1])
      if linestart <= 0:
        bailout("linestart must be > 0", ERR_ARGS_INTEGER_ERROR)
  except:
    bailout("linestart must be an integer", ERR_ARGS_INTEGER_ERROR)

  lineend = DEFAULT_LINES_TO_READ
  if len(sys.argv) > 3:
    # end can be absolute (if prefixed with e, eg 'e38') or relative
    try:
      if sys.argv[2].count('e') > 0:
        lineend = int(sys.argv[2].replace('e',''))
      elif sys.argv[2].count('-') > 0:
        lineend = 0
      else:
        lineend = int(sys.argv[2])
        lineend = linestart + lineend
    except:
      bailout("lineend must be an integer", ERR_ARGS_INTEGER_ERROR)
    if lineend < linestart and lineend != 0:
      bailout("lineend is absolute, but smaller than start", ERR_ARGS_INTEGER_ERROR)


  # file to read from
  if len(sys.argv) is 4:
    fileread = sys.argv[3]
  else:
    fileread = sys.argv[2]
  if not os.path.isfile(fileread):
    bailout("file does not exist", ERR_ARGS_FILE_DOES_NOT_EXIST)

  # read the input file------------------------------
  # this will be used for left-adjustment of line number
  if lineend > 100000:
    maxspace = 6
  elif lineend > 10000:
    maxspace = 5
  elif lineend > 1000:
    maxspace = 4
  elif lineend > 100:
    maxspace = 3
  elif lineend > 10:
    maxspace = 2
  else:
    maxspace = 1

  try:
    fp = open(fileread)
    for i, line in enumerate(fp):
        if i >= (linestart - 1):
          k = i + 1
#          if k > 10:
#            print(" " * (maxspace - 2))
#          elif k > 100:
#            print(" " * (maxspace - 2))
          print(GRN + str(k) + ": " + NRM),
          print(line),
        if lineend != 0:
          if i >= (lineend - 1):
            break

    # done
    fp.close()    
    bailout("", EXECUTION_SUCCESS)

  except Exception:
    # having 'Exception' makes it not catch system exceptions like keyboard etc,
    # as they are derived directly from exceptions.BaseException, not exceptions.Exception
    fp.close()
    print(Exception)
#    sys.exit(ERR_FILE_READ_ERROR)
    bailout("error while reading file", ERR_FILE_READ_ERROR)

# ------------------------------------------------------------------------------
if __name__=="__main__":
    main()

# ------------------------------------------------------------------------------


