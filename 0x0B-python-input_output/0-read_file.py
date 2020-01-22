#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, "r", encoding="UTF8") as f:
        read_data = f.read()
        for line in read_data:
            print(line, end="")
