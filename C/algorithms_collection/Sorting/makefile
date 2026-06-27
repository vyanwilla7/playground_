CC = gcc
CFLAGS = -Wall -Wextra
FOLDER = build

# buble sort
buble_sort:
	mkdir -p $(FOLDER)
	$(CC) $(CFLAGS) buble_sort.c -o $(FOLDER)/buble

run_buble:
	./$(FOLDER)/buble

# selection sort
selection_sort:
	mkdir -p $(FOLDER)
	$(CC) $(CFLAGS) selection_sort.c -o $(FOLDER)/selection

run_selection:
	./$(FOLDER)/selection

cls:
	rm -f $(FOLDER)/*
