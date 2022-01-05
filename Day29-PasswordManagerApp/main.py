from quitButton import QuitButton
from mainWinow import MainWindow

window = MainWindow()

quit_button = QuitButton()
quit_button.config(command=window.destroy)

window.mainloop()
