from vector_norm import *
from matrix_inf_norm import * 
from matrix_one_norm import *   
from random import randint


def vector_to_latex(vec):
    """formatts vectors to be added to a latex document"""
    latex_code = "\\begin{pmatrix}"
    for element in vec:
        latex_code += str(element) + " \\\\"
    latex_code += "\\end{pmatrix}"
    
    return latex_code

def matrix_to_latex(matrix):
    """formats matrices to be added to a latex document"""
    latex_code = "\\begin{pmatrix}"
    for row in matrix:
        latex_code += " & ".join(map(str, row)) + " \\\\"
    latex_code += "\\end{pmatrix}"
    return latex_code

def pnorm_to_latex(matrix_latex ,p, ans):
    """ formats the norm to be added to the latex document """
    return "$$ \\left\\| "+matrix_latex+"\\right\\|_{"+str(p)+"} = "+str(ans)+"$$"

""" test vector Norm """
for i in range(4,7):
    vec = []
    for j in range(i):
        vec.append(randint(-10, 10))
    p = randint(1,3)
    ans  = round(p_norm(vec, p),3)
    latex = vector_to_latex(vec)
    print(pnorm_to_latex(latex ,p, ans))

print()
"""test one_norm """
for i in range(3):
    m = randint(3,5)
    n = randint(3,5)
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randint(-10,10))
        matrix.append(row)
    p = 1
    ans = one_norm(matrix)
    matrix_latex = matrix_to_latex(matrix)
    print(pnorm_to_latex(matrix_latex, p, ans))

print()
"""test inf_norm """
for i in range(3):
    m = randint(3,5)
    n = randint(3,5)
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randint(-10,10))
        matrix.append(row)
    p = "\\infty"
    ans = inf_norm(matrix)
    matrix_latex = matrix_to_latex(matrix)
    print(pnorm_to_latex(matrix_latex, p, ans))