from flask import Flask, redirect, render_template, url_for, request, flash, session
import os
from sudoku_solver import *

app = Flask(__name__)
app.secret_key = 'sudoku'

@app.route('/', methods=["GET", "POST"])
def sudoku():
    return render_template("sudoku.html")

@app.route('/unsolvable/')
def unsolvable():
    return render_template('unsolved.html')

@app.route('/solution/', methods=['GET', 'POST'])
def solved_board():
    # try:
    init_board = [[], [], [], [], [], [], [], [], []]

    count = 0

    if request.method == "POST":
        num = request.form.getlist("num")

        for i in range(81):
            num[i] = int(num[i])

        for r in range(9):
            for j in range(9):
                init_board[r].append(num[count])
                count += 1

        import boards
        boards.unfinished = init_board
        import sudoku_solver

        if sudoku_solver.is_valid(init_board):
            solved_board = sudoku_solver.run()
            return render_template('solved.html', lst=solved_board)
        else:
            return redirect(url_for('unsolvable'))

    # except Exception as e:
    #print ('failed to connect')


if __name__ == "__main__":
    app.run(debug=True)
