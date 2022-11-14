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

inv_name = "Invalid argument. Name must be string (len >= 2)."
inv_surname = "Invalid argument. Surname must be string (len >= 2)."
def format_name(name, surname):
    if isinstance(name, str) and len(name) >= 2:
        if isinstance(surname, str) and len(surname) >= 2:
            print(name[0].upper() +". " + surname + " (" + name + ")")
        else:
            print(inv_surname)
    else:
        print(inv_name)


print(format_name("Wallace", "Corbo Ugulino"))

