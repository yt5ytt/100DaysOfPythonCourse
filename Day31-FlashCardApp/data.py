import pandas


class Data:

    def __init__(self):
        self.words_list = {}
        self.guessed_rows = {}
        data = pandas.read_csv("./data/french_words.csv")
        rows = data.iterrows()
        for index, row in rows:
            self.words_list[index] = [row.French, row.English]