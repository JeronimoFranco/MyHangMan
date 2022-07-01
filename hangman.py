"""
ES IMPORTANTE INSTALAR CURSES !
terminal : pip install windows-curses

"""

import curses
from random import randint
import string
WIDTH = 50
HEIGHT = 40
MANWIDTH = 10

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
curses.resize_term(HEIGHT, WIDTH)

def main():

    def showMan(attemps):
        if attemps == 0:
            stdscr.addstr(2, 4, """
            
            
                +----+
                |    |
                |
                |
                |
                |
                |
    """)
        elif attemps == 1:
                stdscr.addstr(2, 4, """
                
                
                +----+
                |    |
                |    O
                |
                |
                |
                |
        """)
        elif attemps == 2:
                stdscr.addstr(2, 4, """
                

                +----+
                |    |
                |    O
                |    |
                |    |
                |    
                |
        """)
        elif attemps == 3:
                stdscr.addstr(2, 4, """
                
                
                +----+
                |    |
                |    O
                |   /|
                |    |
                |    
                |
        """)
        elif attemps == 4:
                stdscr.addstr(2, 4, """
                
                
                +----+
                |    |
                |    O
                |   /|\\
                |    |
                |   
                |
        """)
        elif attemps == 5:
                stdscr.addstr(2, 4, """
                
                
                +----+
                |    |
                |    O
                |   /|\\
                |    |
                |   / 
                |
        """)
        elif attemps == 6:
                stdscr.addstr(2, 4, """
                
                
                +----+
                |    |
                |    O
                |   /|\\
                |    |
                |   / \\
                |
        """)

    def getRandomWord():
        words = ["Lapiz", "Boligrafo", "Laptop", "Telvecion", "Color", "Pantalla", "Escritorio", "Microsoft", "Apple", "Raton", "Mono", "Rana", "Sapo", "Electricidad", "Violin", "Bajo", "Alto", "Edificio", "Java", "JavaScript"]
        return list(words[randint(0, len(words) - 1)].lower())

    def youLost(answer):
        builder2 = ""
        count = 0
        for i in answer:
            if count == 0:
                ans = "{}".format(i)
                builder2 = builder2 + ans.upper()
            else:
                builder2 = builder2 + i
            count += 1
        answer = builder2
        stdscr.clear()
        stdscr.addstr(0, int( (WIDTH / 2) - int(len("Press [Tab] to acces the buttons") / 2) ), "Press [Tab] to acces the buttons")
        showButtons()
        stdscr.addstr(int(HEIGHT / 2) + 2, int( (WIDTH / 2) - int(len("You Lost.") / 2) ), "You Lost")
        stdscr.addstr(int(HEIGHT / 2) + 3, int( (WIDTH / 2) - int(len("The answer was : {}".format(answer)) / 2) ), "The answer was : {}".format(answer))

    def youWin():
        stdscr.clear()
        stdscr.addstr(0, int( (WIDTH / 2) - int(len("Press [Tab] to acces the buttons") / 2) ), "Press [Tab] to acces the buttons")
        showButtons()
        stdscr.addstr(int(HEIGHT / 2) + 2, int( (WIDTH / 2) - int(len("You Win.") / 2) ), "You Win")

    def showButtons():
        border = "_" * (WIDTH)
        stdscr.addstr(HEIGHT - 2, 0, border)
        stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len("Exit") / 2) ), "Exit")
        stdscr.addstr(HEIGHT - 5, 0, border)
        stdscr.addstr(HEIGHT - 6, int( (WIDTH / 2) - int(len("Reestart") / 2) ), "Reestart")
        stdscr.addstr(HEIGHT - 8, 0, border)
        stdscr.addstr(HEIGHT - 9, int( (WIDTH / 2) - int(len("*DON\'T RESIZE THIS WINDOW*") / 2) ), "*DON\'T RESIZE THIS WINDOW*")

    def buttonsInit():
        pos = 0
        while True:
            if pos == 1:
                stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len(">> Exit") / 2) ), ">> Exit")
                stdscr.addstr(HEIGHT - 6, int( (WIDTH / 2) - int(len("           ") / 2) ), "           ")
                stdscr.addstr(HEIGHT - 6, int( (WIDTH / 2) - int(len("Reestart") / 2) ), "Reestart")
            elif pos == 0:
                stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len("           ") / 2) ), "           ")
                stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len("Exit") / 2) ), "Exit")
                stdscr.addstr(HEIGHT - 6, int( (WIDTH / 2) - int(len(">> Reestart") / 2) ), ">> Reestart")
            elif pos == 2:
                break

            action = stdscr.getch()

            if str(action) == "9":
                if pos == 0:
                    pos = 1
                elif pos == 1:
                    pos = 2
            elif str(action) == "10":
                break
        
        stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len("           ") / 2) ), "           ")
        stdscr.addstr(HEIGHT - 3, int( (WIDTH / 2) - int(len("Exit") / 2) ), "Exit")
        return pos

    showButtons()
    Wattemps = 0
    word = getRandomWord()
    stringWord = ""
    progress = ""
    stdscr.addstr(0, int( (WIDTH / 2) - int(len("Press [Tab] to acces the buttons") / 2) ), "Press [Tab] to acces the buttons")

    for i in word:
        stringWord = stringWord + i
    for i in stringWord:
        progress = progress + 'X'

    while True:
        stdscr.addstr(28, int( (WIDTH / 2) - int(len("      THE GUI.. ") / 2) ), "      THE GUI.. ")
        stdscr.addstr(28, int( (WIDTH / 2) - int(len("...PLAYING...") / 2) ), "...PLAYING...")
        showMan(Wattemps)
        stdscr.addstr(9, int((WIDTH / 2) - int( (len(stringWord) / 2) ) + (MANWIDTH / 2)),progress)

        action = stdscr.getch()
        
        if str(action) == "9":
            stdscr.addstr(28, int( (WIDTH / 2) - int(len("...IN THE GUI...") / 2) ), "...IN THE GUI...")
            pos = buttonsInit()
            if pos == 0:
                break
            elif pos == 1:
                exit(0)
            else:
                continue
        elif chr(action) in word:
            progress = list(progress)

            count = 0
            for i in stringWord:
                if i == chr(action):
                    if count == 0:
                        progress[count] = '{}'.format(chr(action).upper())
                    else:
                        progress[count] = '{}'.format(chr(action))
                count += 1
            
            builder = ""
            for i in progress:
                builder = builder + i
            progress = builder
        else:
            Wattemps += 1
        
        if not 'X' in progress:
            youWin()
        
        if Wattemps == 6:
            youLost(stringWord)

if __name__ == "__main__":
    while True:
        stdscr.clear()
        main()