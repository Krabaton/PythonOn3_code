# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm\nPython\tTest')

    def function1(item):
        result = item**2
        return result


    def function2(list_items):
        result = []
        for item in list_items:
            result.append(function1(item))
        return result

    print(function2([2, 3, 4]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
