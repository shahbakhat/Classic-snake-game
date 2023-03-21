import curses

# Setting up the window
curses.initscr()
window = curses.newwin(20,60,0,0) # 1st Y and then X
window.keypad(1)

curses.noecho(0) # To not hear any other inputs
curses.curs_set(0)
window.border(0)
window.nodelay(1) # Loop goes intil next user input
