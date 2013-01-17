#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# 
# Author: Marcus Lunden <marcus@bithappens.se>
#
#
import sys
import os
#-------------------------------------------------------------------------------
def bailout(errstr = "", exitcode = 1):
  if exitcode != 0:
    print("will grep (recursively if no files specified) for your search string.")
    print("usage: findme \"search string\" FILES")
    print("Examples: ----------")
    print("  findme hej")
    print("  findme hej *.c")
    print("  findme \"hej\" *.c")
    print("  findme \"hello world\" *.c")
    print("  findme \"hello world\"")
    print("")
    print("*** error ***: " + errstr)
  sys.exit(exitcode)
#-------------------------------------------------------------------------------
# was intended for checking the input argument but it seems it worked pertty well
# anyway, so I just reduced this to accept anything. Kept it here in case I later
# encounter anything to check for
def check_ok(arg = ''):
  return True
# ------------------------------------------------------------------------------
def main():
  command = "grep -r --color=auto -n "
  
  if len(sys.argv) == 1:
    bailout("", 0)

  if len(sys.argv) == 2:
    if check_ok(sys.argv[1]):
      command += '"' + sys.argv[1] + '" *'
    else:
      bailout("error in argument", 1)

  if len(sys.argv) >= 3:
    # the term to search for
    if check_ok(sys.argv[1]):
      command += '"' + sys.argv[1] + '"' + " "
    else:
      bailout("error in argument", 1)
    for arg in sys.argv[2:]:
      command += arg + " "

#  print(command)
  # execute OS command
#  print(os.getcwd())
  os.system(command)

# ------------------------------------------------------------------------------
if __name__=="__main__":
    main()

# ------------------------------------------------------------------------------


