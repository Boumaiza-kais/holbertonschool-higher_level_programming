#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, "r", encoding="UTF8") as f:
        i = 0
        for line in f:
            i += 1
        return i
