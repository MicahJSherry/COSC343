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
