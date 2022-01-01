from alphabet import Alphabet
from wordProcess import WordProcess

a = Alphabet()

word = input("Enter a word: ").upper()

w = WordProcess(word)
w.list_comprehension(a.dict)