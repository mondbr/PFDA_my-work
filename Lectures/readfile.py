# read a simple file
# author: Monika Dabrowska

FILENAME = "data.txt"
DATADIR = "../datafiles/"

print (DATADIR + FILENAME)
with open(DATADIR + FILENAME, "rt") as fp:
    total = 0 #rt stands for read text
    for line in fp:
        total += int(line)
        print (f"{line} is size {len(line)}")
        print (line, end="")
    print (" ")
    print (f"total is {total} ")