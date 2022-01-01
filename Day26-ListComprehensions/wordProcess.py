class WordProcess:

    def __init__(self, word,):
        self.list = list(word)
    
    def list_comprehension(self, my_dict):
        spell_check = [my_dict[letter] for letter in self.list]
        print(spell_check)