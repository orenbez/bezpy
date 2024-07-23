# Tutorial: https://www.youtube.com/watch?v=Db4oc8qc9RU
# Documentation: https://docs.python.org/3/library/curses.html
# ===========================================================
# this library can control the display on your command line screen with precision
# not all terminals will appear the same for any given curser instruction
# pip install windows-curses (already included with linux)
# Must run from the command line
# print() commands won't work at all


# ===========================================================
# Structure of the program is like this ...
# ===========================================================
# def main(stdscr):
# 	...
# 	...
# wrapper(main)

# ===========================================================
# Constants
# ===========================================================
# A_BLINK		Blinking text
# A_BOLD		Extra bright or bold text
# A_DIM			Half bright text
# A_REVERSE		Reverse-video text
# A_STANDOUT	The best highlighting mode available
# A_UNDERLINE	Underlined text

# COLOR_CYAN
# COLOR_BLUE
# COLOR_YELLOW
# COLOR_GREEN
# COLOR_MAGENTA
# COLOR_WHITE
# COLOR_RED
# COLOR_BLACK

# ===========================================================


import curses  # requires pip install windows-curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from time import sleep




def main(stdscr):
	# sets curses.color_pair(1) to curses.color_pair(8)
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_RED)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)


	stdscr.attron(curses.color_pair(1))
	stdscr.border()
	stdscr.attroff(curses.color_pair(1))

	stdscr.clear()  # Clear the command screen,  not sure what stdscr.erase() is
	stdscr.addstr('# =========================================================================================\n')
	stdscr.addstr("Welcome to curses\n")  # Sets at top-left, moves one line down and sets curser

	# Picks up Curser and relocates to coordinates 3,10, first row is counted as row ZERO,  first column is column ZERO
	stdscr.addstr(3,10, 'x 3,10')       # cooridinates (row,col) for text on screen i.e. (3,10) row 4 column 11
	stdscr.addstr(3,20, 'x 3,20')       # cooridinates for text on screen, and continues from here

	stdscr.addstr(" ...  This should be in bold\n", curses.A_BOLD)
	stdscr.addstr("This should be CYAN on RED background\n", curses.color_pair(1))
	stdscr.addstr("This should be BLUE on BLACK background and BOLD\n", curses.color_pair(2) | curses.A_BOLD)
	stdscr.addstr("This should be YELLOW on BLACK background and BOLD\n", curses.color_pair(3) | curses.A_BOLD)
	stdscr.addstr("This should be GREEN on BLACK background and BOLD\n", curses.color_pair(4) | curses.A_BOLD)
	stdscr.addstr("This should be MAGENTA on BLACK background and BOLD\n", curses.color_pair(5) | curses.A_BOLD)
	stdscr.addstr("This should be WHITE on BLACK background and BOLD\n", curses.color_pair(6) | curses.A_BOLD)
	stdscr.addstr("This should be RED on BLACK background and BOLD\n", curses.color_pair(7) | curses.A_BOLD)
	stdscr.addstr("This should be BLACK on WHITE background and BOLD\n", curses.color_pair(8) | curses.A_BOLD)
	stdscr.addstr("Press any key to continue ...\n")
	stdscr.refresh()
	stdscr.getkey()  # Waits for any key entry

	stdscr.clear()
	stdscr.addstr("Enter any key twice ...\n")
	stdscr.refresh() # displays whatever you have drawn

	key = stdscr.getkey()  # waits for input returns key character
	stdscr.addstr(f'You entered:  {key}\n')
	stdscr.refresh()
	ch = stdscr.getch()    # waits for input returns key ordinal value e.g. 'w' = 119
	stdscr.addstr(f'You entered: {ch}\n')
	stdscr.refresh()
	sleep(1)

	stdscr.clear()
	stdscr.addstr(f'Hit the F1 key:')
	stdscr.refresh()

	key = stdscr.getch()
	if key == curses.KEY_F1:  # constant stores integer value of 265 for the f1 key
		stdscr.addstr(f'CORRECT')
	else:
		stdscr.addstr(f'INCORRECT')
	stdscr.refresh()

	# Draw Rectangle from Coordinates (1,2) ->  (3,10) around your Window
	rectangle(stdscr, 1, 2, 3, 10)
	stdscr.refresh()

	# Window of 4 characters
	# create a window which can be updated independently from the main screen of height x width = 1 x 5
	# Width of Window is '5' chars but you can only use '4' as you need one for curser, else will crash the program
	# Place the window on screen coordinates (2,3)
	win = curses.newwin(1, 5, 2, 3)   # nlines=1, ncols=5, begin_y=2, begin_x=3
	for i in range(3, 0, -1):
		win.clear()
		win.addstr(f"..{i}", curses.color_pair(1) | curses.A_BOLD)
		win.refresh()
		sleep(1)


	# =================================================================================================
	# Textbox
	# =================================================================================================
	win.clear() # Set the new Window as a text box  uses emacs shortcuts e.g. CTRL+G to exit textbox
	tb = Textbox(win)
	win.refresh()
	tb.edit()  # moves cursor to textbox
	text = tb.gather()
	stdscr.clear()
	stdscr.addstr(1,1, f'You entered "{text}" in the box')
	win.refresh()
	win.getkey()

	stdscr.clear()
	# =======================================================================
	# create a pad
	# =======================================================================
	pad = curses.newpad(100, 100)
	# These loops fill the pad with letters; addch() is
	# explained in the next section
	for y in range(0, 99):
		for x in range(0, 99):
			pad.addch(y, x, ord('a') + (x * x + y * y) % 26)

	# Displays a section of the pad in the middle of the screen.
	# (0,0) : coordinate of upper-left corner of pad area to display.
	# (5,5) : coordinate of upper-left corner of window area to be filled
	#         with pad content.
	# (20, 75) : coordinate of lower-right corner of window area to be
	#          : filled with pad content.
	pad.refresh(0, 0, 5, 5, 20, 75)
	# =======================================================================
	stdscr.getch()
	stdscr.addstr("\n\n\nPress any key to Terminate!", curses.A_UNDERLINE)
	stdscr.refresh()


	# curses.echo()  # echoes typed keys to screen

	# This sets an attribute 'on' then switches it 'off' doesn't seem to work with windows
	# stdscr.attron(curses.color_pair(1))
	# rectangle(stdscr, 1, 2, 3, 10)
	# stdscr.attroff(curses.color_pair(1))
	# stdscr.refresh()
	#

	# stdscr.nodelay(True)   # getch() will be non-blocking.
	# stdscr.nodelay(False)  # getch() will be non-blocking.

	stdscr.getkey()


wrapper(main)