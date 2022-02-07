from Classes.billboard import Billboard
from Classes.my_spotipy import MySpotipy
from const import ID, SECRET

date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
songs = Billboard(date)
list_of_songs = songs.title_list

sp = MySpotipy(ID, SECRET, list_of_songs, date)
sp.import_songs_to_playlist()
