""" Modulo responsavel por fazer agrupar as funções que fazem o parser de um regex"""


def parseRegex(regex: str):
    """ Recebe uma string representando um regex e retorna uma string em um formato mais facil de transformar em uma arvore sintatica"""
    extendedRegex = extendsExpression(regex)
    procesedRegx = addConcatenationSymbol(extendedRegex)
    postfixRegex = toPostfix(procesedRegx)
    return postfixRegex


def extendsExpression(expr: str):
    """ Adiciona o simbolo de concatenação "#" que representa uma expressão regular extendida """
    return f"{expr}#"


def addConcatenationSymbol(expr: str):
    """ Adiciona o simbolo de concatenação "." explicitamente em uma expressão regular """
    output = ""
    for i in range(len(expr)):
        token = expr[i]
        output += token

        if token in ["(", "|"]:
            continue

        if i < (len(expr) - 1):

            lookahead = expr[i + 1]
            if lookahead in [")", "|", "*"]:  # ? + [ ] -
                continue

            output += "."

    return output


def getOperatorsPrecedence():
    """Retorna um dicionario com a precedencia dos operadores utilizados no regex"""
    return {
        "(": -1,
        "|": 0,
        ".": 1,
        "*": 2,
    }


def toPostfix(expr: str):
    """Transforma uma expressão regular infixa para posfixa"""
    output = ""

    stack = []
    stack.append("(")
    extendedExpr = expr + ')'
    operatorsPrecedence = getOperatorsPrecedence()

    for i in extendedExpr:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack[-1] != "(":
                output += stack.pop()
            stack.pop()
        elif i in dict.keys(operatorsPrecedence):
            while len(stack) > 0:
                charPrecedence = operatorsPrecedence[i]
                topStackPrecedence = operatorsPrecedence[stack[-1]]

                if charPrecedence > topStackPrecedence:
                    stack.append(i)
                    break
                else:
                    output += stack.pop()
        else:
            output += i
    return output
