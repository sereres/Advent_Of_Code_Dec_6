# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def CalculateGroupCount(input_str):
    val = input_str.replace("\n", "")
    return len(set(val))


def CountEachGroup(input_str):
    group_list = input_str.split("\n\n")
    return [CalculateGroupCount(x) for x in group_list]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_str = []
    with open("/Users/sereres/aoc_day6_input.txt","r") as file:
        input_str = file.read()
    group_count_list = CountEachGroup(input_str)
    final_answer = sum(group_count_list)
    print(final_answer)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
