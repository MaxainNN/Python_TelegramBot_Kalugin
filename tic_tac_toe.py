# Функция из первого пункта
# Function from the first paragraph

def draw_board(board):
    # Run loop that goes through all 3 rows of the board
    # Запустить цикл, который проходит по всем 3 элементам строки
    for i in range(3):
        # Print value separators in a string
        # Поставить разделители значений в строке
        print(" | ".join(board[i]))
        # Print string separators
        # Поставить разделители строк
        print("---------")

# Функция из второго пункта
# Function from the second paragraph

# def ask_and_make_move(player, board):
#     # Give the player feature to make move, input coordinates
#     # Дать игроку возможность сделать ход, то есть ввести координаты
#     x, y =input(f"{player}, enter x and y coordinates (e.g. 0 0): ").split()
#     # Convert coordinate to integers
#     # Преобразовать координаты в целые числа
#     x, y = int(x), int(y)
#     # Set a condition that checks whether the coordinate is within the field
#     # and whether the place is free
#     # Задать условие, которое проверяет,
#     # находится ли координата в пределах поля и свободно ли место
#     if (0 < x < 2) and (0 < y < 2) and (board[x][y] == " "):
#         # if free write player's value (x or 0) in cell
#         # Если свободно, записать значение игрока (X или 0) в ячейку
#         board[x][y] = player
#     else:
#         print("That spot is already taken. Try again.")
#         ask_and_make_move(player, board)


# Функции из третьего пункта
# Functions from the third paragraph

def ask_and_make_move(player, board, x, y):
    x, y = ask_move(player, board, x, y)
    # Coordinates x and y take from function ask_move(player, board)
    # Координаты x и y взять из функции ask_move(player, board)
    make_move(player, board)

def ask_move(player, board):
    # Give the player feature to make move, input coordinates
    # Дать игроку возможность сделать ход, то есть ввести координаты
    x, y =input(f"{player}, enter x and y coordinates (e.g. 0 0): ").split()
    # Convert coordinate to integers
    # Преобразовать координаты в целые числа
    x, y = int(x), int(y)
    #
    # Задать условие, которое проверяет, свободно ли место
    if (0 < x < 2) and (0 < y < 2) and (board[x][y] == " "):
        # If cell is free return coordinates
        # Если клетка свободна, вернуть ее координаты
        return (x, y)
    else:
        print("The cell is busy.Enter coordinates again.")
        # print("Клетка занята.Введите координаты еще раз.")
        return ask_move(player, board)


def make_move(player, board, x, y):
    # Check that cell is free
    # проверить, что клетка свободна
    if board[x][y] != " ":
        print("The cell is busy!")
        # print("Клетка занята!")
        return False
    # if cell is free - record the move
    # если клетка свободна,записать ход
    board[x][y] = player
    return True

# Функция из четвертого пункта
# Function from the fourth paragraph

def check_win(player, board):
    # Check if values in rows and columns are the same
    # Проверить, совпадают ли значения в строках и столбцах
    for i in range(3):
        # Check if values in rows are the same
        # Проверить совпадают ли значения в строках
        if board[i] == [player, player, player]:
            return True
    # Check if values in columns are the same
    # Проверить совпадают ди значения в столбцах
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
        return True
    # Check if the values on the diagonal are the same from top left to bottom right
    # Проверить, совпадают ли значения на диагонали из левого верхнего в правый нижний угол
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # Check if the values on the diagonal are the same from top right to bottom left
    # Проверить, совпадают ли значения на диагонали из правого верхнего в левый нижний угол
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Функция из пятого пункта
# Function from the fifth paragraph

def tic_tac_toe():
    # Set infinite loop that runs game
    # Задать бесконечный цикл, который проводит игры
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        # Set infinite loop that runs particular game
        # Задать бесконечный цикл, который проводит конкретную игру
        while True:
            # Draw the playing field
            # Нарисовать игровое поле
            draw_board(board)
            # Request a move
            # Запросить ход
            ask_and_make_move(player, board)
            # Check if player is win
            # Проверить, выиграл ли игрок
            if check_win(player, board):
                print(f"{player} win!")
                # print(f"{player} выиграли!")
                break
            # Check if it's tie
            # Проверить, произошла ли ничья
            tie_game = True
            for row in board:
                for cell in row:
                    if cell == " ":
                        return False
            # If there is a draw, end the loop
            # Если произошла ничья, завершить цикл
            if not tie_game:
                break
            player = "O" if player == "X" else "X"
        # Ask the players if they want to play again
        # Спросить игороком не хотят лт они сыграть снова
        restart = input("Do you want to play again? (y/n) ")
        # restart = input("Хотите сыграть еще раз? (y/n)")
        if restart.lower() != "y":
            break
