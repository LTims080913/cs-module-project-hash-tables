def no_dups(s):
    # Your code here
    dict = {}
    result = ''
    string = s.split()
    for word in string:
        if word not in dict:
            dict[word] = None
            result += word + ' '
    return result.strip()

# Input: a string of words separated by spaces. Only the letters `a`-`z`
# are utilized.

# Output: the string in the same order, but with subsequent duplicate
# words removed.

# There must be no extra spaces at the end of your returned string.

# The solution must be `O(n)`.
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

