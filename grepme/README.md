# grepme

Very simple, very stupid, very lazy.
I was too lazy to enter 'grep -r "search term" *' so I just wrote this quick wrapper to do just that.
It just recursively greps the search term with some proper grep arguments.

Example

	grepme hello
	recursively searches ./* for "hello"

	grepme "hello world"
	same but for "hello world"

	grepme "hello world" *.c
	searches in all .c-files (but not recursively)

	grepme "what" hello.c world.h
	you get it.
