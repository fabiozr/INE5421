# Classe responsavel por fazer o parser inicial de uma expressão regular, para transformala em uma arvore sintatica.
class RegexParser:
    operatorsPrecedence = {
        "(": -1,
        "|": 0,
        ".": 1,
        "*": 2,
    }

    def __init__(self, expr):
        self.expr = expr

    # Adiciona o simbolo de concatenação "." explicitamente em uma expressão regular
    def __preProcess(self):
        output = ""
        for i in range(len(self.expr)):
            token = self.expr[i]
            output += token

            if token in ["(", "|"]:
                continue

            if i < (len(self.expr) - 1):

                lookahead = self.expr[i + 1]
                if lookahead in [")", "|", "*"]:  # ? + [ ] -
                    continue

                output += "."

        return output

    # Transforma uma expressão regular infixa para posfixa
    def __toPostfix(self):
        output = ""

        stack = []
        stack.append("(")
        extendedExpr = self.expr + ')'

        for i in extendedExpr:
            if i == "(":
                stack.append(i)
            elif i == ")":
                while stack[-1] != "(":
                    output += stack.pop()
                stack.pop()
            elif i in dict.keys(self.operatorsPrecedence):
                while len(stack) > 0:
                    charPrecedence = self.operatorsPrecedence[i]
                    topStackPrecedence = self.operatorsPrecedence[stack[-1]]

                    if charPrecedence > topStackPrecedence:
                        stack.append(i)
                        break
                    else:
                        output += stack.pop()
            else:
                output += i
        return output


parser = RegexParser()
parsed = parser.preProcess(regex)
postfix = parser.toPostfix(parsed)

print(postfix)
