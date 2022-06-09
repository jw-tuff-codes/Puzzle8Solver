# NOTE TO GRADER:
# I used https://stackoverflow.com/questions/26979266/convert-a-list-of-integers-to-string
# for getting string representation of an arr of ints in solve method
# ''.join(map(str, level))

import numpy as np
import heapq


def h(arr):
    solved = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    orig = np.array(arr)
    orig_2d = np.reshape(orig, (3, 3))
    d = 0
    for i in range(3):
        for j in range(3):
            if solved[i][j] != orig_2d[i][j] and solved[i][j] != 0:
                location = np.argwhere(orig_2d == solved[i][j])
                x = abs(location[0][0] - i) + abs(location[0][1] - j)
                d += x
    return d


def get_succ(arr):
    lines = np.zeros((4, 9), dtype=int)
    orig = np.array(arr)
    orig_2d = np.reshape(orig, (3, 3))
    location = np.argwhere(orig_2d == 0)
    added_count = 0
    if (location[0][0] - 1) >= 0:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0] - 1][location[0][1]]
        temp[location[0][0] - 1][location[0][1]] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1

    if (location[0][0] + 1) <= 2:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0] + 1][location[0][1]]
        temp[location[0][0] + 1][location[0][1]] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    if (location[0][1] + 1) <= 2:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0]][location[0][1] + 1]
        temp[location[0][0]][location[0][1] + 1] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    if (location[0][1] - 1) >= 0:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0]][location[0][1] - 1]
        temp[location[0][0]][location[0][1] - 1] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    lines = lines.tolist()
    lines = sorted(lines)
    if added_count == 4:
        return lines

    while added_count != 4:
        lines = np.delete(lines, 0, 0)
        added_count += 1
    lines = lines.tolist()
    return lines


def print_succ(arr):
    lines = np.zeros((4, 9), dtype=int)
    orig = np.array(arr)
    orig_2d = np.reshape(orig, (3, 3))
    location = np.argwhere(orig_2d == 0)
    added_count = 0
    if (location[0][0] - 1) >= 0:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0] - 1][location[0][1]]
        temp[location[0][0] - 1][location[0][1]] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1

    if (location[0][0] + 1) <= 2:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0] + 1][location[0][1]]
        temp[location[0][0] + 1][location[0][1]] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    if (location[0][1] + 1) <= 2:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0]][location[0][1] + 1]
        temp[location[0][0]][location[0][1] + 1] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    if (location[0][1] - 1) >= 0:
        temp = np.copy(orig_2d)
        temp_val = temp[location[0][0]][location[0][1] - 1]
        temp[location[0][0]][location[0][1] - 1] = 0
        temp[location[0][0]][location[0][1]] = temp_val
        temp = temp.flatten()
        lines[added_count] = temp
        added_count += 1
    lines = lines.tolist()
    lines = sorted(lines)
    if added_count == 4:
        for level in lines:
            print(level, 'h=' + str(h(level)))
        return lines

    while added_count != 4:
        lines = np.delete(lines, 0, 0)
        added_count += 1
    lines = lines.tolist()

    for level in lines:
        print(level, 'h=' + str(h(level)))
    return lines


def solve(arr):
    pq = []
    closed = []
    key_vals = {}

    heapq.heappush(pq, (h(arr), arr, (0, h(arr), -1)))
    notFound = True
    index = 0
    popcount = 0
    while notFound:
        takeOne = heapq.heappop(pq)
        popcount += 1
        #if takeOne[1] not in closed:
        heapq.heappush(closed, takeOne[1])

        if takeOne[2][1] == 0:
            traceback(takeOne[1], key_vals, arr, index)
            notFound = False
            break

        succs = get_succ(takeOne[1])
        #print(takeOne[2][0])
        for level in succs:
            if ''.join(map(str, level)) not in key_vals:
                heapq.heappush(pq, (h(level) + (takeOne[2][0] + 1), level, ((takeOne[2][0] + 1), h(level), index)))
                key_vals[''.join(map(str, level))] = ''.join(map(str, takeOne[1]))

        index += 1


def traceback(solved, dic, orig, moves):
    orig_string = ''.join(map(str, orig))
    new_dict = {}
    a = []
    start = '123456780'
    a.append(start)
    # print(dic)
    for i in range(100000):
        for k, v in dic.items():
            if k == a[i]:
                a.append(v)
                break
        if orig_string in a:
            break

    a.reverse()
    j = 0
    for item in a:
        ar_as_string = item
        arry = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        index = 0
        for char in item:
            arry[index] = int(char)
            index += 1

        print('h=' + str(h(arry)), "moves:", j)
        print (np.reshape(arry, (3, 3)))
        j += 1


# print_succ([8,7,6,5,4,3,2,1,0])
#solve([1, 2, 3, 4, 5, 6, 7, 0, 8])
solve([6, 5, 1, 0, 3, 7, 4, 8, 2])
