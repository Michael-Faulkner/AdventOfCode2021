with open('../Data/Day4.txt') as f:
    data = f.read().splitlines()


def part1(data):
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]

    boards = []
    current_board = []
    marked_boards = []
    for line in data[1:]:
        if line == '':
            boards.append(current_board)
            marked_boards.append([['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o']])
            current_board = []
        else:
            num_list = line.split()
            nums = [int(x) for x in num_list]
            current_board.append(nums)

    boards = boards[1:]
    marked_boards = marked_boards[1:]
    found_board = False
    for num in numbers:
        for i in range(len(boards)):
            for row_idx in range(5):
                for column_idx in range(5):
                    if boards[i][row_idx][column_idx] == num:
                        marked_boards[i][row_idx][column_idx] = 'x'

        for j in range(len(boards)):
            #check diagnols
            if marked_boards[j][0][0] == marked_boards[j][1][1] == marked_boards[j][2][2] == marked_boards[j][3][3] == marked_boards[j][4][4] == 'x':
                found_board = True
                score_board(data, boards[j], num)
                break

            if marked_boards[j][0][4] == marked_boards[j][1][3] == marked_boards[j][2][2] == marked_boards[j][3][1] == marked_boards[j][4][0] == 'x':
                found_board = True
                score_board(data, boards[j], num)
                break


            for row_idx in range(5):
                if marked_boards[j][row_idx][4] == marked_boards[j][row_idx][3] == marked_boards[j][row_idx][2] == marked_boards[j][row_idx][1] == marked_boards[j][row_idx][0] == 'x':
                    found_board = True
                    score_board(data, boards[j], num)
                    break

            for row_idx in range(5):
                if marked_boards[j][0][row_idx] == marked_boards[j][1][row_idx] == marked_boards[j][2][row_idx] == marked_boards[j][3][row_idx] == marked_boards[j][4][row_idx] == 'x':
                    found_board = True
                    score_board(data, boards[j], num)
                    break
        if found_board:
            break


def score_board(data, board, num):
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]
    total = 0

    for i in range(5):
        for j in range(5):
            total += board[i][j]
    idx = 0
    n = numbers[idx]
    neg_total = 0
    while True:
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    neg_total += n

        if n == num:
            break
        idx += 1
        n = numbers[idx]
    total = total - neg_total
    print(total*num)


part1(data)



def part2(data):
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]

    boards = []
    current_board = []
    marked_boards = []
    won_boards = []
    for line in data[1:]:
        if line == '':
            boards.append(current_board)
            marked_boards.append([['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o'],['o','o','o','o','o']])
            current_board = []
        else:
            num_list = line.split()
            nums = [int(x) for x in num_list]
            current_board.append(nums)

    boards = boards[1:]
    marked_boards = marked_boards[1:]
    for num in numbers:
        for i in range(len(boards)):
            for row_idx in range(5):
                for column_idx in range(5):
                    if boards[i][row_idx][column_idx] == num:
                        marked_boards[i][row_idx][column_idx] = 'x'

        for j in range(len(boards)):
            if boards[j] not in won_boards:
                #check diagnols
                if marked_boards[j][0][0] == marked_boards[j][1][1] == marked_boards[j][2][2] == marked_boards[j][3][3] == marked_boards[j][4][4] == 'x':

                    won_boards.append(boards[j])
                    score_board(data, boards[j], num)

                if marked_boards[j][0][4] == marked_boards[j][1][3] == marked_boards[j][2][2] == marked_boards[j][3][1] == marked_boards[j][4][0] == 'x':
                    won_boards.append(boards[j])
                    score_board(data, boards[j], num)


                for row_idx in range(5):
                    if marked_boards[j][row_idx][4] == marked_boards[j][row_idx][3] == marked_boards[j][row_idx][2] == marked_boards[j][row_idx][1] == marked_boards[j][row_idx][0] == 'x':
                        won_boards.append(boards[j])
                        score_board(data, boards[j], num)
                        break

                for row_idx in range(5):
                    if marked_boards[j][0][row_idx] == marked_boards[j][1][row_idx] == marked_boards[j][2][row_idx] == marked_boards[j][3][row_idx] == marked_boards[j][4][row_idx] == 'x':
                        won_boards.append(boards[j])
                        score_board(data, boards[j], num)
                        break

part2(data)