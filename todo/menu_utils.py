import curses
import colorama
from colorama import Fore, Back, Style
colorama.init()
class menuInterface:
    def __init__(self, menu):
        self.info = menu

    def print_menu(self,stdscr, selected_row_idx):
        list = self.info
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(list):
            char = ' ✓ ' if row["status"] else ' x '
            text = '{id} {char} {task}'
            x = w//2 - len(text)//2
            y = h//2 - len(list)//2 + idx
            pair = 2
            if row["status"]:
                pair = 1
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(pair))
                stdscr.addstr(y, x, text.format(
                    id=idx,
                    char = char,
                    task=row["task"],
                ))
                stdscr.attroff(curses.color_pair(pair))
            else:
                stdscr.addstr(y, x, text.format(
                    id=idx,
                    char = char,
                    task=row["task"],
                ))
        x = 0
        y = h//2 + len(list)//2 +1
        text = "↑ or ↓ to scroll the list \n ↵ (Enter) to toggle" +"\n" +"q to quit"
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(y,x,text,)
        stdscr.attron(curses.color_pair(3))
        stdscr.refresh()

    def update(self,stdscr,rowid,status):
        self.info[rowid]["status"] = not status
        self.print_menu(stdscr, rowid)

        return

    def main(self,stdscr):
        menu = self.info
        # turn off cursor blinking
        curses.curs_set(0)

        # color schemes
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_WHITE,curses.COLOR_BLACK)

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(stdscr, current_row)

        while 1:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu)-1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                s = menu[current_row]["status"]

                self.update(stdscr,current_row,s)
                # if user selected last row, exit the program
            elif key==ord("q"):
                return self.info


            self.print_menu(stdscr, current_row)


    