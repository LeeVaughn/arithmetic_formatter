def arithmetic_arranger(problems):
    row_one = ""
    row_two = ""
    row_three = ""
    
    arranged_problems = f"""{row_one}
{row_two}
{row_three}"""

    # for problem in problems:
    #     arranged_problem += f"""{problem[0]}\n
    #     {problem[1]}\n
    #     {problem[2]}\n
    #     """

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))