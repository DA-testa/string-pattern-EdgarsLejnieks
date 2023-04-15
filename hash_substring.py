# python3

import sys


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    inputtype = input()
    inputtype = inputtype.strip()

    if inputtype == "I":
        try:
            firstline = input().rstrip()
            secondline = input().rstrip()
            line_list = [firstline, secondline]
            return line_list
        except IOError as e:
            print(e)

    if inputtype == "F":
        try:
            filepath = input()
            filepath = "tests/" + filepath
            file = open(filepath, "r")
            firstline = file.readline().rstrip()
            secondline = file.readline().rstrip()
            file.close()
            line_list = [firstline,secondline]
            return line_list
        except EOFError as e:
            print(e)

    else:
        print("input type error")
        sys.exit()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    PATTERN_HASH = hash(pattern)
    ITERABLE_RANGE = len(text)-len(pattern)
    zeroBasedMatches = []
    for i in range(ITERABLE_RANGE):
        activePatternHash = hash(text[i:len(pattern)+i])
        if activePatternHash == PATTERN_HASH:
            zeroBasedMatches.append(i)
    # and return an iterable variable
    return zeroBasedMatches


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

