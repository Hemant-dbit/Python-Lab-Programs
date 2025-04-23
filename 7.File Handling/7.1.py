import os

FILENAME = "sample.txt"
EXCLUSIVE_FILENAME = "exclusive_file.txt"

def write_initial_file():
    content = "This is line 1.\nThis is line 2.\nThis is line 3."
    with open(FILENAME, "w") as file:
        file.write(content)
    print(f"\nFile '{FILENAME}' written successfully.")

def read_with_read():
    print("\n--- Reading using read() ---")
    with open(FILENAME, "r") as file:
        print(file.read())

def read_with_readline():
    print("\n--- Reading using readline() ---")
    with open(FILENAME, "r") as file:
        while line := file.readline():
            print(line.strip())

def read_with_readlines():
    print("\n--- Reading using readlines() ---")
    with open(FILENAME, "r") as file:
        for line in file.readlines():
            print(line.strip())

def create_exclusive_file():
    try:
        with open(EXCLUSIVE_FILENAME, "x") as ex_file:
            ex_file.write("This file is created with 'x' mode.")
        print(f"\n '{EXCLUSIVE_FILENAME}' created exclusively.")
    except FileExistsError:
        print(f"\n File '{EXCLUSIVE_FILENAME}' already exists, cannot create with 'x' mode.")

# Run all operations
write_initial_file()
read_with_read()
read_with_readline()
read_with_readlines()
create_exclusive_file()
