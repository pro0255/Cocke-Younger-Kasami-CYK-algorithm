from collections import defaultdict

class Grammar():

    def __init__(self, filename):
        self.rightside2left = defaultdict(list)
        self.leftside2right = defaultdict(list)
       



        for line in open(filename):
            left, right = line.split("->")
            right = right.rstrip('\n').strip().split(" ")

            left = left.strip()


            self.leftside2right[left] = self.leftside2right[left] + right 
            for right_item in right:
                self.rightside2left[right_item].append(left)

        if len(self.rightside2left) == 0:
            raise ValueError("No rules found in the grammar file")

        self.leftNonT = self.leftside2right.keys()  #X
        print('Grammar file readed succesfully. Rules readed:')
        print(self)


    def __str__(self):
        output = ''
        for k,v in self.leftside2right.items():
            right = "|".join(v)
            output += f'{k} -> {right}\n'
        return output

