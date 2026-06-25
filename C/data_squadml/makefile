CC = gcc
CFLAGS = -Wall -Wextra -Iinclude
src = $(wildcard src/*.c)
OUT = build/main

all:
	mkdir -p build
	$(CC) $(CFLAGS) $(src) -o $(OUT)

run:
	./$(OUT)

clear:
	rm -rf $(OUT)
