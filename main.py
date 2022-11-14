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

# Homewrok 1
def is_the_same(message1, message2):
    if isinstance(message1, str) and isinstance(message2, str):
        if message1.lower() == message2.lower():
            print("True")
        else:
            print("False")
    else:
        print("Please enter strings")


is_the_same("mad", "Ma")
