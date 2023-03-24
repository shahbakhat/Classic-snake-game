
import curses
from random import randint

# constatns
WINDOW_WIDTH = 60
WINDOW_HEIGHT = 20
# Setting up the window
curses.initscr()
win = curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Snake and Food
snake = [(4,4),(4,3),(4,2)]
food = (6 , 6)

# Game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0,2, 'Score' + str(score) + '')
    #increase speed of the snake
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120 )




    prev_key = key
    event = win.getch()
    key = event if event !=-1 else prev_key




    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT,
    curses.KEY_UP, curses.KEY_DOWN, ESC] :
        key = prev_key

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    # New head of the snake
    snake.insert(0,(y,x))
    # if snake hits the border, then
    if y == 0: break
    if y == WINDOW_HEIGHT - 1: break
    if x == 0: break
    if x == WINDOW_WIDTH - 1: break

    # when snake hits his his own body
    if snake[0] in snake[1:]:break

    # when snake eats the food
    if snake [0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint,(1,WINDOW_HEIGHT -  2)
                    , randint(1,WINDOW_WIDTH - 2))
            if food in snake:
                food = ()
                win.addch(food[0], food[1] , '#')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(food[0], food[1] , '#')

curses.endwin()
print(f"Final score = {score}")


