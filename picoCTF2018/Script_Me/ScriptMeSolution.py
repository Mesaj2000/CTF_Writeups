from pwn import *

# Breaks the question down into a list of the units that compose it
def findUnits(question):
    i = 0
    chr = question[i]
    units = []

    while chr != "?":
        while chr != "+" and chr != "=":
            i = i+1
            chr = question[i]
        units.append(question[:i-1])
        question = question[i+2:]
        i = 0
        chr = question[i]

    return units

# Takes a list of units (from "findUnits"), returns a parrallel list of corresponding depths
def findDepths(units):
    depths = []

    for unit in units:

        depth = 0
        maxDepth = 0

        for chr in unit:
            if chr == "(":
                depth = depth + 1
                if depth > maxDepth:
                    maxDepth = depth
            elif chr == ")":
                depth = depth - 1

        depths.append(maxDepth)

    return depths


# Takes a question, outputs a single string corresponding to the solution to the question
def merge(question):

    units = findUnits(question)
    depths= findDepths(units)

    for i in range(len(units)-1):

        # Absorb left
        if (depths[0] > depths[1]):
            units[0] = units[0][:-1] + units.pop(1) + ")"
            depths.pop(1)

        # Absorb right
        elif (depths[0] < depths[1]):
            units[0] = "(" + units[0] + units.pop(1)[1:]
            depths.pop(0)

        # Combinie
        else:
            units[0] = units[0] + units.pop(1)
            depths.pop(1)

	# At this point, "units" is a list of length 1, containing the solution
    return units[0]

# Whenever you answer a question incorrectly, the problem returns the expected solution
# In that event, I copied them here to test what my code was doing, and tried to figure out what it was doing wrong
def test():
    question = "(()()()(())()()) + (()(((()()())()())()())) + (()(((()()())()())()())) + ((())()) + (()()()) = ???"
    expected = "((()()()(())()())()(((()()())()())()()))(()(((()()())()())()())((())())(()()()))"
    units = findUnits(question)
    depths= findDepths(units)
    solution = merge(question)
    print(question)
    print(units)
    print(depths)
    print(solution)
    print(expected)


# Connects into the challenge, attempts to solve it
def solve():
    r = remote("18.224.157.204", 7866)
    r.recvuntil("warmup.")
    r.recvline()

    for i in range(5):
        question = r.recvline()
        r.recvline()
        print("question = " + question)			# Mostly just here to make sure it was grabbing the right line
        r.sendline(merge(question))
        for j in range(3):
            print("skipping = " + r.recvline())		# Figured the flag would be in one of these lines

    r.close()




#test()
solve()


