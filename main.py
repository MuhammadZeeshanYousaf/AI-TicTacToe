from minimax import *
from tkinter import *


def gui(mark):
    if mark is TICK:
        return "✔"
    elif mark is CROSS:
        return "✘"
    return ''


# Driver code here
if __name__ == '__main__':
    # declarations
    board = Board()
    window = Tk()  # main window
    # create buttons list
    button = [[Button(window, text="   ", pady=22, padx=35, font="none 15") for _ in range(3)] for _ in range(3)]

    # window configurations
    window.geometry("600x390")
    window.title(f"AI Project {TICTACTOE}")

    # Labels
    main_label = Label(window, text=f"{TICTACTOE.upper()} Game", padx=30, pady=18, fg="#666666", font=f"{FONT} 16 bold")
    main_label.grid(row=0, column=0)
    cells_label = Label(window, text=f"Empty Cells: {empty_cells(board)}", padx=30, pady=18, fg="#3A3B3C",
                        font=f"{FONT} 11")
    cells_label.grid(row=1, column=0)
    author_label = Label(window, text=AUTHOR, padx=30, pady=18, fg="#A5A6A8", font=f"{FONT} 8")
    author_label.grid(row=4, column=0)
    win_label = Label(window, text="\t", bg="#FFFFFF", fg="Green", padx=15, pady=7, font=f"{FONT} 10 bold")
    win_label.grid(row=2, column=0)

    def action(row, col):
        if terminate_test(board) is BLANK and board.game_board()[row][col] is BLANK:
            # human turn made (MIN turn)
            board.cross(row, col)
            # update gui components
            button[row][col].config(text=gui(board.game_board()[row][col]))
            cells_label.config(text=f"Empty Cells: {empty_cells(board)}")

            # computer agent turn (MAX turn)
            _terminate_state = terminate_test(board)
            if _terminate_state is BLANK:
                print(board.game_board())
                val = minimax(0, board, True, MIN, MAX)
                r, c = val[1], val[2]
                print("Main return:", val[0])
                board.tick(r, c)
                button[r][c].config(text=gui(board.game_board()[r][c]))
                cells_label.config(text=f"Empty Cells: {empty_cells(board)}")
                _terminate_state = terminate_test(board)
                if _terminate_state is not BLANK:
                    win_label.config(text=f"{gui(terminate_test(board))} Won !")
            else:
                win_label.config(text=f"{gui(_terminate_state)} Won !")


    # add action events on 9 buttons
    r1, c1, r2, c2, r3, c3 = [0, 0, 1, 1, 2, 2]
    button[r1][c1].config(command=lambda: action(r1, c1))
    button[r1][c2].config(command=lambda: action(r1, c2))
    button[r1][c3].config(command=lambda: action(r1, c3))
    button[r2][c1].config(command=lambda: action(r2, c1))
    button[r2][c2].config(command=lambda: action(r2, c2))
    button[r2][c3].config(command=lambda: action(r2, c3))
    button[r3][c1].config(command=lambda: action(r3, c1))
    button[r3][c2].config(command=lambda: action(r3, c2))
    button[r3][c3].config(command=lambda: action(r3, c3))

    # set position of buttons on window
    button[r1][c1].grid(row=r1 + 1, column=c1 + 2)
    button[r1][c2].grid(row=r1 + 1, column=c2 + 2)
    button[r1][c3].grid(row=r1 + 1, column=c3 + 2)
    button[r2][c1].grid(row=r2 + 1, column=c1 + 2)
    button[r2][c2].grid(row=r2 + 1, column=c2 + 2)
    button[r2][c3].grid(row=r2 + 1, column=c3 + 2)
    button[r3][c1].grid(row=r3 + 1, column=c1 + 2)
    button[r3][c2].grid(row=r3 + 1, column=c2 + 2)
    button[r3][c3].grid(row=r3 + 1, column=c3 + 2)

    # create reset action
    def reset():
        for i in range(len(button)):
            for j in range(len(button[i])):
                board.blank(i, j)
                button[i][j].config(text="   ")
                cells_label.config(text=f"Empty Cells: {empty_cells(board)}")
                win_label.config(text="\t")
    # create reset button
    Button(window, text="Reset", fg='Red', pady=4, padx=10, font=f"{FONT} 10", command=reset).grid(row=3, column=0)

    # initialize the window
    window.mainloop()
