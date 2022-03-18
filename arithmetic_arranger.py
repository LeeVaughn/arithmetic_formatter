def arithmetic_arranger(problems, solve=False):
    row_one = ""
    row_two = ""
    row_three = ""
    row_four = ""

    # error handling for too many problems
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    for problem in problems:
        split_problem = problem.split(" ")
        num_1 = split_problem[0]
        num_2 = split_problem[2]
        operator = split_problem[1]
        length = max(len(split_problem[0]), len(split_problem[2]))
        divider_length = length + 2

        # error handling for operators other than + or -
        if operator != "+" and operator != "-":
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        # error handling for numbers only containing digits
        if problem.upper().isupper():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
            

        # error handling for numbers greater than four digits
        if len(num_1) > 4 or len(num_2) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

        row_one += f"{' ' * ((length + 2) - len(num_1))}{num_1}"
        row_two += f"{operator}{' ' * ((length + 1) - len(num_2))}{num_2}"
        row_three += f"{'-' * divider_length}"

        # adds for spaces between problems except after the last problem
        if problem is not problems[len(problems) -1]:
            row_one += "    "
            row_two += "    "
            row_three += "    "

        if solve is True:
            if operator == "+":
                total = int(num_1) + int(num_2)
                row_four += f"{' ' * (divider_length - len(str(total)))}{int(num_1) + int(num_2)}"
            elif operator == "-":
                total = int(num_1) - int(num_2)
                row_four += f"{' ' * (divider_length - len(str(total)))}{int(num_1) - int(num_2)}"

            if problem is not problems[len(problems) -1]:
                row_four += "    "
            


    if solve is True:
        arranged_problems = f"""{row_one}
{row_two}
{row_three}
{row_four}"""
    else:
        arranged_problems = f"""{row_one}
{row_two}
{row_three}"""

    return arranged_problems


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))