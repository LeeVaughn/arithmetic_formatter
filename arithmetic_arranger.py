def arithmetic_arranger(problems):
    row_one = ""
    row_two = ""
    row_three = ""

    for problem in problems:
        split_problem = problem.split(" ", 1)
        length = max(len(split_problem[0]), len(split_problem[1]))
        # print(split_problem[0])
        # print(split_problem[1])
        # print(length)
        row_one += f"{split_problem[0]}\t"
        row_two += f"{split_problem[1]}\t"
        row_three += f"{'-' * length}\t"

    arranged_problems = f"""{row_one}
{row_two}
{row_three}"""

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))