from grammar import Grammar
from cyk import Cyk

g = Grammar("example_grammar3.txt")
cyk = Cyk(g)
word = "baaabaa"
cyk.run(word)

# g2 = Grammar('example_grammar1.txt')
# cyk2 = Cyk(g2)
# word2 = 'baaba'
# cyk.run(word2)
