# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
            pass

    if opening_brackets_stack:
            return opening_brackets_stack[0].position
    return "Success"


def main():
    i_or_f = input("")
    if i_or_f == 'I':
        text = input()
        mismatch = find_mismatch(text)
        if type(mismatch) == int:
            print(mismatch)
        else:
            print("Success")
    elif i_or_f == 'F':
        filename = input("")
        testfolder = "test/" + filename
        try: 
            with open (testfolder, 'r') as file:
                text = file.read()
                mismatch = find_mismatch(text)
                if type(mismatch) == int:
                    print(mismatch)
        except FileNotFoundError:
            print("Not exist")
        else:
            print("Success")

if __name__ == "__main__":
    main()
