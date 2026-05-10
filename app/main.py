import pygame
import math
import copy

pygame.init()

WIDTH = 600
HEIGHT = 600

ROWS = 6
COLS = 6

CELL_SIZE = WIDTH // COLS

WHITE = (240, 240, 240)
GRAY = (100, 100, 100)

BLUE = (50, 100, 255)
RED = (220, 50, 50)

BLACK = (0, 0, 0)

GREEN = (50, 200, 50)
YELLOW = (255, 255, 0)

HUMAN = "H"
AI = "A"
EMPTY = "."

visited_states = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Warcaby AI")

font = pygame.font.SysFont(None, 40)

def create_board():

    board = [
        [EMPTY for _ in range(COLS)]
        for _ in range(ROWS)
    ]

    for row in range(2):
        for col in range(COLS):

            if (row + col) % 2 == 1:
                board[row][col] = AI

    for row in range(ROWS - 2, ROWS):
        for col in range(COLS):

            if (row + col) % 2 == 1:
                board[row][col] = HUMAN

    return board


board = create_board()

selected = None
current_turn = HUMAN
last_ai_move = None

def draw_board(board):

    global selected
    global last_ai_move

    screen.fill(BLACK)

    for row in range(ROWS):
        for col in range(COLS):

            color = WHITE

            if (row + col) % 2 == 1:
                color = GRAY

            pygame.draw.rect(
                screen,
                color,
                (
                    col * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

            # Podświetlenie wybranego pionka gracza
            if selected == (row, col):

                pygame.draw.rect(
                    screen,
                    GREEN,
                    (
                        col * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    ),
                    5
                )

            # Podświetlenie ostatniego ruchu AI
            if last_ai_move:

                _, _, tr, tc = last_ai_move

                if tr == row and tc == col:

                    pygame.draw.rect(
                        screen,
                        YELLOW,
                        (
                            col * CELL_SIZE,
                            row * CELL_SIZE,
                            CELL_SIZE,
                            CELL_SIZE
                        ),
                        5
                    )

            piece = board[row][col]

            if piece == HUMAN:

                pygame.draw.circle(
                    screen,
                    BLUE,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    25
                )

            elif piece == AI:

                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    25
                )

def count_pieces(board, player):

    count = 0

    for row in board:
        count += row.count(player)

    return count

def evaluate(board):

    ai_score = count_pieces(board, AI)
    human_score = count_pieces(board, HUMAN)

    return ai_score - human_score

def is_valid_move(board, sr, sc, tr, tc, player):

    if tr < 0 or tc < 0:
        return False

    if tr >= ROWS or tc >= COLS:
        return False

    if board[tr][tc] != EMPTY:
        return False

    direction = -1 if player == HUMAN else 1

    # zwykły ruch
    if tr == sr + direction and abs(tc - sc) == 1:
        return True

    # bicie
    if tr == sr + 2 * direction and abs(tc - sc) == 2:

        mr = (sr + tr) // 2
        mc = (sc + tc) // 2

        enemy = AI if player == HUMAN else HUMAN

        if board[mr][mc] == enemy:
            return True

    return False

def get_all_moves(board, player):

    moves = []

    for row in range(ROWS):
        for col in range(COLS):

            if board[row][col] == player:

                for dr in [-1, 1]:
                    for dc in [-1, 1]:

                        tr = row + dr
                        tc = col + dc

                        if is_valid_move(
                            board,
                            row,
                            col,
                            tr,
                            tc,
                            player
                        ):

                            moves.append((row, col, tr, tc))

                        tr2 = row + dr * 2
                        tc2 = col + dc * 2

                        if is_valid_move(
                            board,
                            row,
                            col,
                            tr2,
                            tc2,
                            player
                        ):

                            moves.append((row, col, tr2, tc2))

    return moves

def make_move(board, sr, sc, tr, tc):

    piece = board[sr][sc]

    board[sr][sc] = EMPTY
    board[tr][tc] = piece

    # bicie
    if abs(sr - tr) == 2:

        mr = (sr + tr) // 2
        mc = (sc + tc) // 2

        board[mr][mc] = EMPTY

def minimax(board, depth, alpha, beta, maximizing):

    global visited_states

    visited_states += 1

    if depth == 0:
        return evaluate(board)

    if count_pieces(board, AI) == 0:
        return -100

    if count_pieces(board, HUMAN) == 0:
        return 100

    if maximizing:

        max_eval = -math.inf

        for move in get_all_moves(board, AI):

            new_board = copy.deepcopy(board)

            make_move(
                new_board,
                move[0],
                move[1],
                move[2],
                move[3]
            )

            evaluation = minimax(
                new_board,
                depth - 1,
                alpha,
                beta,
                False
            )

            max_eval = max(max_eval, evaluation)

            alpha = max(alpha, evaluation)

            if beta <= alpha:
                break

        return max_eval

    else:

        min_eval = math.inf

        for move in get_all_moves(board, HUMAN):

            new_board = copy.deepcopy(board)

            make_move(
                new_board,
                move[0],
                move[1],
                move[2],
                move[3]
            )

            evaluation = minimax(
                new_board,
                depth - 1,
                alpha,
                beta,
                True
            )

            min_eval = min(min_eval, evaluation)

            beta = min(beta, evaluation)

            if beta <= alpha:
                break

        return min_eval

def ai_move(board):

    global visited_states
    global last_ai_move

    visited_states = 0

    best_score = -math.inf
    best_move = None

    for move in get_all_moves(board, AI):

        new_board = copy.deepcopy(board)

        make_move(
            new_board,
            move[0],
            move[1],
            move[2],
            move[3]
        )

        score = minimax(
            new_board,
            4,
            -math.inf,
            math.inf,
            False
        )

        if score > best_score:

            best_score = score
            best_move = move

    if best_move:

        last_ai_move = best_move

        make_move(
            board,
            best_move[0],
            best_move[1],
            best_move[2],
            best_move[3]
        )

def check_winner(board):

    if count_pieces(board, HUMAN) == 0:
        return "AI"

    if count_pieces(board, AI) == 0:
        return "GRACZ"

    # brak możliwych ruchów = remis
    if len(get_all_moves(board, HUMAN)) == 0:
        return "REMIS"

    if len(get_all_moves(board, AI)) == 0:
        return "REMIS"

    return None

running = True

while running:

    draw_board(board)

    winner = check_winner(board)

    if winner:

        text = font.render(
            f"Koniec gry: {winner}",
            True,
            GREEN
        )

        screen.blit(text, (20, 20))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and current_turn == HUMAN
            and not winner
        ):

            x, y = pygame.mouse.get_pos()

            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if selected is None:

                if board[row][col] == HUMAN:
                    selected = (row, col)

            else:

                sr, sc = selected

                if is_valid_move(
                    board,
                    sr,
                    sc,
                    row,
                    col,
                    HUMAN
                ):

                    make_move(
                        board,
                        sr,
                        sc,
                        row,
                        col
                    )

                    current_turn = AI

                selected = None

    if current_turn == AI and not winner:

        ai_move(board)

        current_turn = HUMAN

pygame.quit()
