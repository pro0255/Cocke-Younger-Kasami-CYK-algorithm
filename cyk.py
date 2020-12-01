import numpy as np

"""
Lets assume that this gramma will be in CNF
"""
ASSUMED_STARTING_SYMBOL = 'S' 

class Cyk():
    def __init__(self, grammar):
        self.grammar = grammar 
        pass
    
    def get_substrings(self, k):
        return [self.word[i: j] for i in range(len(self.word)) for j in range(i + 1, len(self.word) + 1) if len(self.word[i:j]) == k] 


    def print_T_row(self, index):
        substring_size = index + 1
        print(f'Word {self.word} substrings with size of {substring_size} can get as follows')
        print(f'{self.X2index}')
        substrings = self.get_substrings(substring_size)

        for index_substring_cell, substring in enumerate(substrings):
            tmp = self.T[index]
            print(f'Substring {substring} from word {self.word}')
            substring_cell = tmp[index_substring_cell]
            print(substring_cell)

    def init_phase(self, word):
        for index, c in enumerate(word):
            Xs = self.grammar.rightside2left[c]
            # print(f'For characted {c} {Xs}')
            for X in Xs:
                self.T[0, index, self.X2index[X]] += 1
        self.print_T_row(0)


    def make_product(self, left, right):
        products = []
        for lI, lValue in enumerate(left):
            for rI, rValue in enumerate(right):
                if lValue > 0 and  rValue > 0:
                    products.append((f'{self.index2X[lI]}{self.index2X[rI]}', lValue*rValue))
        return products
     
    def run(self, word):
        word_size = len(word)
        self.word = word
        X_len = len(self.grammar.leftNonT)
        self.X2index = {X:index for index, X in enumerate(self.grammar.leftNonT)}
        self.index2X = {index:X for index, X in enumerate(self.grammar.leftNonT)}

        #vytvorime pole T[i,j,X], kde X je neterminal
        self.T = np.zeros((word_size, word_size, X_len))
        #pro kazdy znak na pozici i a pro kazde X urcujici znak na i nastavime 1
        self.init_phase(word)
        n = len(self.word)
        for l in range(2, n + 1):
            print(f'Processing length of substring {l}')
            for s in range(0, n - l + 1): #kolik podretezcu o velikost len_subs se vleze do procesu radku
                sub_right_border = s+l
                print(f'\tSubstring {self.word[s:sub_right_border]}')
                for p in range(0, l - 1): #kolikrat mohu participovat dany substring
                    print('\t\tParts:', self.word[s:s+p+1], self.word[s+p+1:sub_right_border])
                    # print(self.word[s:s+p+1], p,s)
                    # print(self.word[s+p+1:sub_right_border], l-2-p, p+s+1)
                    column_up_movement = self.T[p,s]
                    diagonal_down_movement = self.T[l-2-p, p+s+1]
                    for production in self.make_product(column_up_movement, diagonal_down_movement):
                        rightSide, productValue = production
                        if rightSide in self.grammar.rightside2left:
                            parents = self.grammar.rightside2left[rightSide]
                            for parent in parents:
                                self.T[l-1, s, self.X2index[parent]] += productValue
            self.print_T_row(l - 1)
        print('\n\nFinished wtih result')
        number_of_trees = self.T[n-1,0,self.X2index[ASSUMED_STARTING_SYMBOL]]
        print(f'Number of trees {number_of_trees}') 
