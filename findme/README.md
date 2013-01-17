# findme

Very simple, very stupid, very lazy.
I was too lazy to enter 'grep -r "search term" *' so I just wrote this quick wrapper to do just that.
It just recursively greps the search term with some proper grep arguments.

Example
	findme hello
	recursively searches ./* for "hello"

	findme "hello world"
	same but for "hello world"

	findme "hello world" *.c
	searches in all .c-files (but not recursively)

	findme "what" hello.c world.h
	you get it.
