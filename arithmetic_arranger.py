def arithmetic_arranger(problems):
    row_one = ""
    row_two = ""
    row_three = ""

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

        row_one += f"{' ' * ((length + 2) - len(num_1))}{num_1}"
        row_two += f"{operator}{' ' * ((length + 1) - len(num_2))}{num_2}"
        row_three += f"{'-' * divider_length}"

        # adds for spaces between problems except after the last problem
        if problem is not problems[len(problems) -1]:
            row_one += "    "
            row_two += "    "
            row_three += "    "



    arranged_problems = f"""{row_one}
{row_two}
{row_three}"""

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))