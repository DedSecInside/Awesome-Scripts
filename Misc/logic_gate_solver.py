# Step by Step Logic Gate Solver. Execute input_equation() to start the program!

def input_equation():
    """
    Evaluate input : input input

    Args:
    """
    print("Enter equation without whitespaces")
    equation = input()
    var = []
    for character in equation:
        if(character.isalpha):
            if(character not in var):
                var.append(character)
    answer = fill_variable(var, equation)
    print("The answer is:", answer)

def fill_variable(var, equation):
    """
    Fill variable with variable.

    Args:
        var: (array): write your description
        equation: (str): write your description
    """
    print("The variables are the following")
    for v in var:
        if(v.isalpha()):
            print(v)
    equation_n = equation
    for v in var:
        if(v.isalpha()):
            print("Enter the value of:", v)
            temp = input()
            equation_n = equation_n.replace(v, temp)
    return calculate(equation_n)

def calculate(equation):
    """
    Calculate the equation.

    Args:
        equation: (int): write your description
    """
    print("Calculating now")
    equation = list(equation)
    equation = solve_complement(equation)
    equation = solve_and(equation)
    equation = solve_or(equation)
    return equation

def solve_complement(equation):
    """
    Solve the linear equation.

    Args:
        equation: (todo): write your description
    """
    unsolve = True
    while(unsolve):
        if("'" in equation):
            ind = equation.index("'")
            if(equation [ ind - 1 ] == '1'):
                equation [ ind - 1 ] = 0
                equation.pop(ind)
            else:
                equation [ ind - 1] = 1
                equation.pop(ind)
        else:
            print("Solved Complements")
            print(equation)
            unsolve = False
            return equation

def solve_and(equation):
    """
    Solve the linear equations.

    Args:
        equation: (todo): write your description
    """
    unsolve = True
    while(unsolve):
        if("." in equation):
            ind = equation.index(".")
            if(equation[ind - 1] == '1'):
                if(equation[ind + 1] == '1'):
                    equation[ ind ] = '1'
                    equation.pop(ind - 1), equation.pop(ind)
                else:
                    equation[ ind ] = '0'    
                    equation.pop(ind - 1), equation.pop(ind)
            else:
                equation[ ind ] = '0'
                equation.pop(ind - 1)
                equation.pop(ind)
        else:
            print("Solved AND")
            print(equation)
            unsolve = False
            return equation

def solve_or(equation):
    """
    Solve a linear equation.

    Args:
        equation: (todo): write your description
    """
    unsolve = True
    while(unsolve):
        if("+" in equation):
            ind = equation.index("+")
            if(equation[ind - 1] == '0'):
                if(equation[ind + 1] == '0'):
                    equation[ ind ] = '0'
                    equation.pop(ind - 1), equation.pop(ind)
                else:
                    equation [ ind ] = '1'
                    equation.pop(ind - 1)
                    equation.pop(ind)
            else:
                equation[ ind ] = '1'
                equation.pop(ind - 1)
                equation.pop(ind)
        else:
            print("Solved OR")
            print(equation)
            unsolve = False
            return equation

input_equation()
