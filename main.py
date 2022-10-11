
from parser import parseRegex
from syntaxtree import Node, printTree


regex = "a(a|b)*a"
parsedRegex = parseRegex(regex)


root = Node()
for i in parsedRegex[::-1]:
    root.add(i)

printTree(root)