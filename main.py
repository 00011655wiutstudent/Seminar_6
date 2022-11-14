# Task 4

def test_is_valid(test):
    if isinstance(test, int) and test in range(1, 4):
        print("True")
    else:
        print("False")


test_is_valid('fdj')
# Task 5
def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find("computer", "u", 5))

