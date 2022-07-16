from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

game_board = ["", "", "", "", "", ""]
game_board_hidden = ["?", "?", "?", "?", "?", "?"]


@app.get("/", response_class=HTMLResponse)
async def home_screen():
    return "Welcome to the game <br> go to /game"


def make_new_board():
    global game_board_hidden
    game_board_hidden = ["?", "?", "?", "?", "?", "?"]
    for index in range(len(game_board)):
        game_board[index] = "O"
    random_cell_that_has_x = random.randint(0, 5)
    game_board[random_cell_that_has_x] = "X"
    print(random_cell_that_has_x)


def won():
    counter = 0
    for cell in game_board_hidden:
        if cell == "?":
            counter += 1
    return counter == 1


@app.get("/game/")
async def game():
    make_new_board()
    return game_board_hidden


@app.get("/game/{index}", response_class=HTMLResponse)
async def game_move(index: int):
    game_board_hidden[index] = game_board[index]
    msg = ""
    if game_board_hidden[index] == "X":
        msg = "Lost"
    elif won():
        msg = "Won"
    else:
        msg = "Make another move"
    return f"{game_board_hidden} <br> {msg}"

