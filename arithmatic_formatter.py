def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    dash_line = ''
    answer_line = ''

    for problem in problems:
        operand = problem.split()

        if operand[1] not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if operand[0].isdigit() == False or operand[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if len(operand[0]) > 4 or len(operand[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand[0]), len(operand[2])) + 2

        first_line += operand[0].rjust(width) + '    '
        second_line += operand[1] + ' ' + operand[2].rjust(width - 2) + '    '
        dash_line += '-' * width + '    '

        if show_answers:
            answer = str(eval(problem))
            answer_line += answer.rjust(width) + '    '

    formatted_problem = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dash_line.rstrip()

    if show_answers:
        formatted_problem += '\n' + answer_line.rstrip()

    return formatted_problem

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))