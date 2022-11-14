# Task 4
def test_is_valid(test):
    if isinstance(test, int) and test in range(1, 4):
        print("True")
    else:
        print("False")


test_is_valid('fdj')
