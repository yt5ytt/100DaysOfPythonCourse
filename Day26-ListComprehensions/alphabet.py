import pandas

class Alphabet:

    def __init__(self):
        df = pandas.read_csv("nato_phonetic_alphabet.csv")
        self.dict = {row.letter: row.code for (index, row) in df.iterrows()}