import os
import heapq as hq
import math


if os.path.exists("output.txt"):
    os.remove("output.txt")


file = open('input.txt', 'r')

method = file.readline().strip()

dimensions_grid = file.readline().split()
size_x, size_y, size_z = [int(i) for i in dimensions_grid]
dimension = [size_x, size_y, size_z]

entrance_grid = file.readline().split()
entrance_x, entrance_y, entrance_z = [int(i) for i in entrance_grid]
entrance = [entrance_x, entrance_y, entrance_z]

exit_grid = file.readline().split()
exit_x, exit_y, exit_z = [int(i) for i in exit_grid]
exit_point = [exit_x, exit_y, exit_z]

grid_size = int(file.readline())

adj_list = {}  # graph inputted as a dict with values representing the key neighbors
discovered = {}  # Explored nodes with flags
cost = {}  # cost of every action in all nodes
predecessors = {}  # Traversal dict to get path
heuristic = {}  # heuristic of every node for A* path search
next_lines = file.readlines()
line_list = [i.split() for i in next_lines]

c = 0
for line in line_list:
    arr = [int(line[i]) for i in range(3)]  # get coordinates from every line
    arr_tup = tuple(arr)
    adj_list[arr_tup] = []
    cost[arr_tup] = []
    discovered[arr_tup] = 0
    if method != 'BFS':
        predecessors[arr_tup] = [None]
        dx = abs(arr[0] - exit_x)
        dy = abs(arr[1] - exit_y)
        dz = abs(arr[2] - exit_z)
        heuristic[arr_tup] = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)  # heuristic calculation
    for i in range(3, len(line)):
        action = int(line[i])  # get action from every line
        if action == 1:
            new_node = [arr[0] + 1, arr[1], arr[2]]  # get neighbor by calculating the resulting
            if [0, 0, 0] < new_node < dimension:  # coordinates from an action
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 2:
            new_node = [arr[0] - 1, arr[1], arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 3:
            new_node = [arr[0], arr[1] + 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 4:
            new_node = [arr[0], arr[1] - 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 5:
            new_node = [arr[0], arr[1], arr[2] + 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 6:
            new_node = [arr[0], arr[1], arr[2] - 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(10)

        elif action == 7:
            new_node = [arr[0] + 1, arr[1] + 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 8:
            new_node = [arr[0] + 1, arr[1] - 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 9:
            new_node = [arr[0] - 1, arr[1] + 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 10:
            new_node = [arr[0] - 1, arr[1] - 1, arr[2]]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 11:
            new_node = [arr[0] + 1, arr[1], arr[2] + 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 12:
            new_node = [arr[0] + 1, arr[1], arr[2] - 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 13:
            new_node = [arr[0] - 1, arr[1], arr[2] + 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 14:
            new_node = [arr[0] - 1, arr[1], arr[2] - 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 15:
            new_node = [arr[0], arr[1] + 1, arr[2] + 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 16:
            new_node = [arr[0], arr[1] + 1, arr[2] - 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 17:
            new_node = [arr[0], arr[1] - 1, arr[2] + 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)

        elif action == 18:
            new_node = [arr[0], arr[1] - 1, arr[2] - 1]
            if [0, 0, 0] < new_node < dimension:
                adj_list[arr_tup].append(new_node)
                cost[arr_tup].append(14)
    c += 1

file.close()


def bfs():
    bfs_queue = [[entrance]]
    while len(bfs_queue) > 0:  # While the queue is not empty, dequeue the first element S, then check the
        edges = bfs_queue.pop(0)  # adjacent points, if it is not discovered, set it to true and add it to queue
        node = edges[-1]
        if discovered[tuple(node)] == 0:
            connections = adj_list[tuple(node)]  # get neighbors
            for connection in connections:
                temp = list(edges)
                temp.append(connection)  # add path to every neighbor
                bfs_queue.append(temp)  # add path to the queue
                if connection == exit_point:  # if goal node then exit
                    return temp  # return current path
            discovered[tuple(node)] = 1

    return 0


def ucs():
    open_queue = [(0, tuple(entrance))]
    closed_queue = []
    discovered[tuple(entrance)] = 1
    while len(open_queue) > 0:
        hq.heapify(open_queue)  # priority queue using a min-heap
        curr = hq.heappop(open_queue)
        if discovered[tuple(curr[1])] == 2:  # skip nodes in closed_queue
            continue
        discovered[tuple(curr[1])] = 0
        curr_cost = curr[0]
        if curr[1] == tuple(exit_point):  # if curr node is the exit, loop through the predecessor dict
            route = []  # until the entrance node to construct the closest path
            node = (tuple(exit_point), 0)
            total = 0
            while predecessors[node[0]] != [None]:
                route.append(node[0])
                node = predecessors[node[0]]
                total = total + node[1]
            return route, total
        children = adj_list[curr[1]]
        costs = cost[curr[1]]
        temp_c = 0
        for child in children:  # check if each neighbor is open_queue, closed_queue or neither
            added_cost = costs[temp_c] + curr_cost
            if discovered[tuple(child)] == 0:  # if neither, push into queue
                hq.heappush(open_queue, (added_cost, tuple(child)))
                discovered[tuple(child)] = 1
                predecessors[tuple(child)] = (curr[1], costs[temp_c])
            elif discovered[tuple(child)] == 1:  # if in open_queue, delete node from queue and add new node if
                if added_cost < curr_cost:  # the new cost is less than the current cost
                    open_queue.remove((curr_cost, tuple(child)))
                    hq.heappush(open_queue, (added_cost, tuple(child)))
                    discovered[tuple(child)] = 1
                    predecessors[tuple(child)] = (curr[1], costs[temp_c])
            elif discovered[tuple(child)] == 2:  # if in closed_queue, delete node from queue and add new node if
                if added_cost < curr_cost:  # the new cost is less than the current cost
                    closed_queue.remove((curr_cost, tuple(child)))
                    hq.heappush(open_queue, (added_cost, tuple(child)))
                    discovered[tuple(child)] = 1
                    predecessors[tuple(child)] = (curr[1], costs[temp_c])
            temp_c += 1
        closed_queue.append(curr)  # visited
        discovered[curr[1]] = 2
    return 0, 0


def a_star():
    open_queue = [(0, tuple(entrance), 0)]  # last element in the tuple represents the g-cost
    closed_queue = []
    discovered[tuple(entrance)] = 1
    while len(open_queue) > 0:
        hq.heapify(open_queue)  # we heapify the queue with f values instead of curr_cost
        curr = hq.heappop(open_queue)
        if discovered[tuple(curr[1])] == 2:
            continue
        discovered[tuple(curr[1])] = 0
        if curr[1] == tuple(exit_point):
            route = []
            node = (tuple(exit_point), 0)
            total = 0
            while predecessors[node[0]] != [None]:
                route.append(node[0])
                node = predecessors[node[0]]
                total = total + node[1]  # we calculate the total cost by summing the g-costs
            return route, total
        old_f_cost = curr[0]
        children = adj_list[curr[1]]
        costs = cost[curr[1]]
        g_cost = curr[2]
        temp_c = 0
        for child in children:
            g_cost = g_cost + costs[temp_c]
            f_cost = heuristic[tuple(child)] + g_cost  # cost function: f(n) = g(n) + h(n)
            if discovered[tuple(child)] == 0:
                hq.heappush(open_queue, (f_cost, tuple(child), g_cost))
                discovered[tuple(child)] = 1
                predecessors[tuple(child)] = (curr[1], costs[temp_c])
            elif discovered[tuple(child)] == 1:
                if f_cost < old_f_cost:
                    open_queue.remove((old_f_cost, tuple(child), curr[2]))
                    hq.heappush(open_queue, (f_cost, tuple(child), g_cost))
                    discovered[tuple(child)] = 1
                    predecessors[tuple(child)] = (curr[1], costs[temp_c])
            elif discovered[tuple(child)] == 2:
                if f_cost < old_f_cost:
                    closed_queue.remove((old_f_cost, tuple(child), curr[2]))
                    hq.heappush(open_queue, (f_cost, tuple(child), g_cost))
                    discovered[tuple(child)] = 1
                    predecessors[tuple(child)] = (curr[1], costs[temp_c])
            temp_c += 1
        closed_queue.append(curr)
        discovered[curr[1]] = 2
    return 0, 0


f = open("output.txt", "x")
if method == 'A*':
    path, cost = a_star()
    if path == 0:
        f.write('FAIL')
        exit()
    f.write(str(cost) + "\n")
    f.write(str(len(path) + 1) + "\n")
    f.write(str(entrance_x) + " " + str(entrance_y) + " " + str(entrance_z) + " " + "0" + "\n")
    path.reverse()
    for i in path:
        for j in range(3):
            f.write(str(i[j]) + " ")
        if i == tuple(exit_point):
            f.write(str(predecessors[i][1]))
            break
        f.write(str(predecessors[i][1]) + "\n")
elif method == 'BFS':
    answer = bfs()
    if answer == 0:
        f.write('FAIL')
        exit()
    total_cost = len(answer) - 1
    f.write(str(total_cost) + "\n")
    f.write(str(total_cost + 1) + "\n")
    f.write(str(entrance_x) + " " + str(entrance_y) + " " + str(entrance_z) + " " + "0" + "\n")
    answer.pop(0)
    for i in answer:
        for j in range(3):
            f.write(str(i[j]) + " ")
        f.write("1" + "\n")
elif method == 'UCS':
    path, cost = ucs()
    if path == 0:
        f.write('FAIL')
        exit()
    f.write(str(cost) + "\n")
    f.write(str(len(path) + 1) + "\n")
    f.write(str(entrance_x) + " " + str(entrance_y) + " " + str(entrance_z) + " " + "0" + "\n")
    path.reverse()
    for i in path:
        for j in range(3):
            f.write(str(i[j]) + " ")
        if i == tuple(exit_point):
            f.write(str(predecessors[i][1]))
            break
        f.write(str(predecessors[i][1]) + "\n")
f.close()
