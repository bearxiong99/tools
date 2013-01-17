# body

this small script is like a mix of head and tail in linux; where one shows the first lines and the other shows the last
lines in a file, body shows some lines in the middle of a file.

Sure, you can make some nice shell macro or alias for it, but with this I can extend it with eg syntax highlighting etc.

Examples:
	body 15 hi.c
	show lines 15--35 (default is 20 lines) from hi.c
	
	body 15 55 hi.c
	show lines 15--70 from hi.c

	body 15 e32 hi.c
	show lines 15--32 from hi.c
