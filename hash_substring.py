# python3

import sys


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    inputtype = input()
    inputtype = inputtype.strip()

    #if inputtype == "I":
    if "I" in inputtype:
        try:
            firstline = input().strip()
            secondline = input().strip()
            #line_list = [firstline, secondline]
            return firstline, secondline
        except IOError as e:
            print(e)

    #if inputtype == "F":
    if "F" in inputtype:
        # print("i got to F") <--- debug, issue after this
        try:
            filepath = input()
            print("cmd1 pass")
            filepath = "tests/" + filepath
            print("cmd1 pass")
            file = open(filepath, "r")
            print("cmd1 pass")
            firstline = file.readline().strip()
            print(firstline)
            secondline = file.readline().strip()
            print(secondline)
            file.close()
            #line_list = [firstline,secondline]
            # print("i have returned vals") <--- debug, issue before this
            return firstline, secondline
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
    ITERABLE_RANGE = len(text)-len(pattern)+1
    zeroBasedMatches = []
    for i in range(ITERABLE_RANGE):
        activePatternHash = hash(text[i:len(pattern)+i])
        if activePatternHash == PATTERN_HASH:
            zeroBasedMatches.append(i)
    # and return an iterable variable
    # print("am returning matches") <--- debug
    return zeroBasedMatches


# this part launches the functions
if __name__ == '__main__':
    inputVar = read_input()
    print_occurrences(get_occurrences(str(inputVar[0]),str(inputVar[1])))