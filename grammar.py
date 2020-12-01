from collections import defaultdict


class Grammar:
    """Class represents input grammar. It also parse grammar from txt."""

    def __init__(self, filename):
        """Constructor which will generate as class prop two dictionaries. Which will represent rules.
        One will represent nonterminal left side with one nonterimal Z -> XY or Z -> character. On right side can be more then one value.

        Second one will represent opossite approach. XY -> Z. Same as above. XY can be generated with more then one rule.
        Args:
            filename (string): Location of input file. This file will be parse.
        Raises:
            ValueError: If smth bad with grammar.
        """
        self.rightside2left = defaultdict(list)
        self.leftside2right = defaultdict(list)

        for line in open(filename):
            left, right = line.split("->")
            right = right.rstrip("\n").strip().split(" ")

            left = left.strip()

            self.leftside2right[left] = self.leftside2right[left] + right
            for right_item in right:
                self.rightside2left[right_item].append(left)

        if len(self.rightside2left) == 0:
            raise ValueError("No rules found in the grammar file")

        self.leftNonT = self.leftside2right.keys()  # X
        print("Grammar file readed succesfully. Rules readed:")
        print(self)

    def __str__(self):
        """ToString method which shows how grammar looks.
        Returns:
            [string]: Grammar.
        """
        output = ""
        for k, v in self.leftside2right.items():
            right = "|".join(v)
            output += f"{k} -> {right}\n"
        return output
