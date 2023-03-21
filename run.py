import curses
import random import randint
# Setting up the window
curses.initscr()
win = curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Snake and Food
snake = [(4,10),(4,9),(4,8)]
food = (10,20)

# Game logic
score = 0

while True:
    event = win.getch()
    for c in snake:
        win.addch(c[0], c[1] , '*')

    win.addch(food[0], food[1] , '#')
curses.endwin()
print(f"Final score = {score}")

