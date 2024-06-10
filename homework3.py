from collections import defaultdict
import numpy as np
import time

file = open('input.txt', 'r')

start = time.time()
method = file.readline().strip()

dimensions = file.readline().split()
size_x, size_y, size_z = [int(i) for i in dimensions]

entrance_grid = file.readline().split()
entrance_x, entrance_y, entrance_z = [int(i) for i in entrance_grid]
entrance = [entrance_x, entrance_y, entrance_z]

exit_grid = file.readline().split()
exit_x, exit_y, exit_z = [int(i) for i in exit_grid]
exit_point = [exit_x, exit_y, exit_z]

grid_size = int(file.readline())

next_lines = file.readlines()
line_list = [i.split() for i in next_lines]

graph = defaultdict(list)
nodes = []
actions = []
cost_list = []
[cost_list.append([]) for _ in range(grid_size)]

for line in line_list:
    arr = np.array([int(line[i]) for i in range(3)]).tolist()
    action = np.array([int(line[i]) for i in range(3, len(line))]).tolist()
    nodes.append(arr)
    actions.append(action)
if entrance in nodes and exit_point in nodes:
    start_index = nodes.index(entrance)
    exit_index = nodes.index(exit_point)
else:
    print('FAIL')
    exit()

counter = 0
for action in actions:
    neighbors = []
    for i in action:
        if i == 1:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0] + 1, nodes[counter][1], nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 2:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0] - 1, nodes[counter][1], nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 3:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0], nodes[counter][1] + 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 4:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0], nodes[counter][1] - 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 5:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0], nodes[counter][1], nodes[counter][2] + 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 6:
            cost_list[counter].append(10)
            new_arr = [nodes[counter][0], nodes[counter][1], nodes[counter][2] - 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 7:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] + 1, nodes[counter][1] + 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 8:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] + 1, nodes[counter][1] - 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 9:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] - 1, nodes[counter][1] + 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 10:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] - 1, nodes[counter][1] - 1, nodes[counter][2]]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 11:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] + 1, nodes[counter][1], nodes[counter][2] + 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 12:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] + 1, nodes[counter][1], nodes[counter][2] - 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 13:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] - 1, nodes[counter][1], nodes[counter][2] + 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 14:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0] - 1, nodes[counter][1], nodes[counter][2] - 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 15:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0], nodes[counter][1] + 1, nodes[counter][2] + 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 16:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0], nodes[counter][1] + 1, nodes[counter][2] - 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 17:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0], nodes[counter][1] - 1, nodes[counter][2] + 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
        elif i == 18:
            cost_list[counter].append(14)
            new_arr = [nodes[counter][0], nodes[counter][1] - 1, nodes[counter][2] - 1]
            index = nodes.index(new_arr)
            neighbors.append(index)
    graph[counter] = neighbors
    counter += 1
end = time.time()
print("Time elapsed:", end - start)
exit()


def bfs(tree):
    bfs_queue = []

    # if start_index == exit_index:
    #     print("Placeholder")
    #     return
    discovered = [False for _ in range(grid_size)]  # Setting all elements of the set discovered to false

    bfs_queue.append([start_index])
    while len(bfs_queue) > 0:  # While the queue is not empty, dequeue the first element S, then
        edge = bfs_queue.pop(0)  # check the adjacent points, if it is not discovered, set it to true and add it
        node = edge[-1]
        if not discovered[node]:
            connections = tree[node]
            for connection in connections:
                new_edge = list(edge)
                new_edge.append(connection)
                bfs_queue.append(new_edge)

                if connection == exit_index:
                    return new_edge
            discovered[node] = True

    print('FAIL')
    return


def ucs(tree, cost):
    open_queue = [(0, start_index)]
    closed_queue = []
    predecessors = [None for _ in range(grid_size)]
    while len(open_queue) > 0:
        curr = open_queue.pop()
        curr_cost = curr[0]
        if curr[1] == exit_index:
            route = []
            node = exit_index
            while node:
                route.append(node)
                node = predecessors[node]
            print(route)
            return curr
        children = tree[curr[1]]
        for child in children:
            added_cost = cost[curr[1]][children.index(child)] + curr_cost
            open_flag = list_check(child, open_queue)
            close_flag = list_check(child, closed_queue)
            if open_flag is False and close_flag is False:
                open_queue.append((added_cost, child))
                predecessors[child] = curr[1]
            elif open_flag is not False:
                if added_cost < open_queue[open_flag][0]:
                    open_queue.pop(open_flag)
                    open_queue.append((added_cost, child))
                    predecessors[child] = curr[1]
            elif close_flag is not False:
                if added_cost < closed_queue[close_flag][0]:
                    closed_queue.pop(close_flag)
                    open_queue.append((added_cost, child))
                    predecessors[child] = curr[1]
        closed_queue.append(curr)
        open_queue.sort()



def list_check(node, queue):
    for i in range(len(queue)):
        if node == queue[i][1]:
            return i

    return False


# def a_star(self, b):
#     return print(self + b)

if method == 'A*':
    print("A*")
elif method == 'BFS':
    print("BFS")
    print(graph)
    # answer = bfs(graph)
    # total_cost = len(answer)
    # print(total_cost)
    # # print(total_cost - 1)
    # for i in answer:
    #     print(nodes[i][0], nodes[i][1], nodes[i][2], '1')
elif method == 'UCS':
    print("UCS")
    print(graph)

file.close()