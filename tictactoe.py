WINNING_CELLS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 4, 8),
    (6, 4, 2),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8)
)

COORDINATE_MAPPING = {
    (1, 3): 0,
    (2, 3): 1,
    (3, 3): 2,
    (1, 2): 3,
    (2, 2): 4,
    (3, 2): 5,
    (1, 1): 6,
    (2, 1): 7,
    (3, 1): 8
}

BLANK_CELL = ' '


def display_board(cells):
    print('---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------'.format(*cells))


def check_winners(cells):
    x_wins = 0
    o_wins = 0

    lines = [[cells[pos] for pos in positions] for positions in WINNING_CELLS]
    for line in lines:
        if line.count('X') == 3:
            x_wins += 1
        elif line.count('O') == 3:
            o_wins += 1

    return x_wins, o_wins


def check_board(cells):
    x_wins, o_wins = check_winners(cells)

    winner = 'X' if x_wins else 'O' if o_wins else None
    if winner:
        return f'{winner} wins'

    return 'Draw' if cells.count(BLANK_CELL) == 0 else None


def next_move(cells, symbol):
    while True:
        str_coordinates = input('Enter the coordinates: ').split(maxsplit=2)

        if not all(x.isnumeric() for x in str_coordinates):
            print('You should enter numbers!')
            continue

        coordinates = [int(x) for x in str_coordinates]
        if any(x < 1 or x > 3 for x in coordinates):
            print('Coordinates should be from 1 to 3!')
            continue

        pos = COORDINATE_MAPPING[tuple(coordinates)]
        if cells[pos] != BLANK_CELL:
            print('This cell is occupied! Choose another one!')
            continue

        cells[pos] = symbol
        break


status = None
players = list('XOXOXOXOX')
board_cells = list(BLANK_CELL * 9)

display_board(board_cells)

while status is None:
    next_move(board_cells, players.pop(0))
    display_board(board_cells)
    status = check_board(board_cells)

print(status)
