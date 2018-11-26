###########################################################
#  Programming Project 10
#
#  This is  a game named Checkers writen by python.
#  This project contains a board class ,a piece class
#   and  several funtions.
#   when we run this program:
#    initial a board object and several piece object.
#    then the plaer chose a colot,two people (or a people and
#     an AI player) took turns play it.
#    when a player can't move any piece or don't have any piece,
#     game over.
###########################################################

import tools
import gameai as ai
from checkers import Piece
from checkers import Board



def indexify(position):
    """
    Indexify a string type position to a int type position.
    :param position: A sting of position.
    :return:A tuple of int of position.
    """

    position_str="abcdefghijklmnopqrstuvwxyz"
    return (position_str.index(position[0]),int(position[1:])-1)


def deindexify(row, col):
    """
    De indexify a tuple of position to a string type position.
    :param row: A int of row index.
    :param col:A int of col index.
    :return:A string of positon.
    """

    position_str="abcdefghijklmnopqrstuvwxyz"
    return position_str[row]+str(col+1)


def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """

    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())


def count_pieces(board):
    """
    Count the number of piece in a board object.
    :param board: A board object.
    :return: A tuple contains the number of black pieces and white pieces.
    """

    black_int=white_int=0
    length_int=board.get_length()
    for row in range(length_int):
        for col in range(length_int):
            if board.get(row,col):
                color=board.get(row,col).color()
                if color=="white":
                    white_int += 1
                else:
                    black_int += 1
    res_list= (black_int,white_int)
    return res_list


def get_all_moves(board, color, is_sorted=False):
    """
    Get all moves a player can do.
    :param board: A board object.
    :param color: A string of the color of the player.
    :param is_sorted: A boolean of if sort.
    :return: A list of all moves.
    """

    length_int = board.get_length()
    all_moves_list = []
    for row in range(length_int):
        for col in range(length_int):
            if board.get(row,col) :
                if board.get(row,col).color()==color:
                    moves_tuple=tools.get_moves(board,row,col,is_sorted)
                    for move in moves_tuple:
                        all_moves_list.append((deindexify(row,col),move))
    return all_moves_list


def sort_captures(all_captures, is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''
    return sorted(all_captures, key=lambda x: (-len(x), x[0])) if is_sorted \
        else all_captures


def get_all_captures(board, color, is_sorted=False):
    """
    Get all captures a player can do.
    :param board:A board object.
    :param color:A string of the color of the player.
    :param is_sorted:A boolean of if sort.
    :return:A list of all captures.
    """

    all_captures_list=[]
    length_int=board.get_length()
    for row in range(length_int):
        for col in range(length_int):
            if board.get(row,col):
                if board.get(row,col).color()==color:
                    if tools.get_captures(board, row, col, ):
                        all_captures_list.extend(tools.get_captures(board,row,col,))
    sorted_captures_list=sort_captures(all_captures_list,is_sorted)
    return sorted_captures_list


def apply_move(board, move):
    """
    Apply a given move to a board object.

    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.")
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function to
            get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.
    """
    row,col=indexify(move[0])[0],indexify(move[0])[1]
    moves_list=tools.get_moves(board,row,col)
    if not move[1] in moves_list:
        raise RuntimeError("Invalid move, please type" \
                           + " \'hints\' to get suggestions.")
    board.place(indexify(move[1])[0],indexify(move[1])[1],board.get(indexify(move[0])[0],indexify(move[0])[1]))
    board.remove(indexify(move[0])[0],indexify(move[0])[1])
    if board.get(indexify(move[1])[0],indexify(move[1])[1]).is_black() and move[1][0]=="h":  #check if need  turn king.
        board.get(indexify(move[1])[0],indexify(move[1])[1]).turn_king()
    if board.get(indexify(move[1])[0],indexify(move[1])[1]).is_white() and move[1][0]=="a":
        board.get(indexify(move[1])[0],indexify(move[1])[1]).turn_king()


def apply_capture(board, capture_path):
    """
    Apply a given capture to a board object.

    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.")
    If,
        a. there is no jump found from any position in capture_path, row.e. use
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.
    """
    for ii in range(len(capture_path)-1):
        jumps_str=tools.get_jumps(board,*indexify(capture_path[ii]))
        if not capture_path[ii+1] in jumps_str:
            raise RuntimeError("Invalid jump/capture, please type" \
                               + " \'hints\' to get suggestions.")
        board.place(*indexify(capture_path[ii+1]),board.get(*indexify(capture_path[ii]))) #generate new piece.
        board.remove(*indexify(capture_path[ii]))       #remove origin piece.
        board.remove(int((indexify(capture_path[ii])[0]+indexify(capture_path[ii+1])[0])/2),int((indexify(capture_path[ii])[1]+indexify(capture_path[ii+1])[1])/2),)  # remove captured piece.

        if board.get(*indexify(capture_path[ii+1])).is_black() and capture_path[ii+1][0]=="h":
            board.get(*indexify(capture_path[ii+1])).turn_king()
        if board.get(*indexify(capture_path[ii+1])).is_white() and capture_path[ii+1][0]=="a":
            board.get(*indexify(capture_path[ii+1])).turn_king()


def get_hints(board, color, is_sorted=False):
    """
    Get some help from program.
    """
    jumps_list=get_all_captures(board,color,is_sorted)
    moves_list=get_all_moves(board,color,is_sorted)
    if jumps_list:
        return ([],jumps_list)
    return (moves_list,jumps_list)


def get_winner(board, is_sorted=False):
    """
    To determine who is winner.
    """
    winner=""
    white_hints_list=get_hints(board,"white",is_sorted)
    black_hints_list=get_hints(board,"black",is_sorted)
    if black_hints_list[0] or black_hints_list[1]:
        if not (white_hints_list[0] or white_hints_list[1]):
            winner= "black"

    if white_hints_list[0] or white_hints_list[1]:
        if not (black_hints_list[0] or black_hints_list[1]):
            winner= "white"
    black_count_int,white_count_int=count_pieces(board)
    if black_count_int==1 and white_count_int==1:
        length_int=board.get_length()
        king_count=0
        for row in range(length_int):
            for col in range(length_int):
                if board.get(row,col):
                    if board.get(row,col).is_king():
                        king_count+=1
        if king_count==2:
            winner ="draw"

    if black_count_int>white_count_int:
        winner= "black"
    if black_count_int<white_count_int:
        winner= "white"
    if black_count_int==white_count_int:
        winner= "draw"
    return winner

def is_game_finished(board, is_sorted=False):
    """
    To determine is thie game finished.
    """
    finished_boolean=False
    if get_hints(board,"black",is_sorted)==([],[]):
        finished_boolean= True
    if get_hints(board,"white",is_sorted)==([],[]):
        finished_boolean= True
    return finished_boolean


# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."


def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    # Piece.symbols = ['b', 'w']
    # Piece.symbols_king = ['B', 'W']

    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)

            print("Current board:")
            board.display(piece_count)

            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()

            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}" \
                              .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            #raise #del
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---


def game_play_ai():
    """
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human()
    function.

    For a given board situation/state, you can call the ai function to get
    the next best move, like this:

        move = ai.get_next_move(board, turn)

    where the turn variable is a color 'black' or 'white', also you need to
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    """

    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']

    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)

            print("Current board:")
            board.display(piece_count)

            if turn==opponent_color:   # start of AI
                next_move_list = ai.get_next_move(board, turn)
                if type(next_move_list)==type((1,2)):
                    apply_move(board,next_move_list)
                if type(next_move_list)==type([1,2]):
                    apply_capture(board,next_move_list)
                turn = my_color if turn == opponent_color else opponent_color
                print("\tblack played",str(next_move_list)+".")
                continue

            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()

            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, next_move_list in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}" \
                              .format(i + 1, next_move_list[0], next_move_list[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play ai ---


def main():
    #game_play_human()
    game_play_ai()


# main function, the program's entry point
if __name__ == "__main__":
    main()