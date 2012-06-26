# I am a comment... bro!
# this is David Rice's first Makefile

# Some variables that i can use by doing $(varname)
CC = gcc
HELLO = hello

# all does a standard make
all:
	@ mkdir -p files
#	@ touch files/test.sh
	@ mkdir -p files/ranger/my/face/lift
	@ touch files/ranger/test
	@ $(CC) '$(HELLO).c' -o files/$(HELLO)
	@ echo "I made a Makefile $(HELLO)"
	@ echo "tarring up files"
	@ tar czvf files.tar.gz files/*
#	@ echo "./files/hello" > /files/test.sh
	@ bash test.sh

# this is run on make clean
clean:
	@ rm -rf files
	@ rm files.tar.gz

# this is run on make rules
rules:
	@ echo "make              |           standard build" 
	@ echo "make clean        |           clean all prior builds"
