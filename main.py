import math
import time
import vertex


def append_vertex_list(attempt, vertex_list):
    new_vertex = vertex.Vertex(attempt)

    for vertex_instance in vertex_list:
        square_number_try = new_vertex.number + vertex_instance.number

        if math.sqrt(square_number_try) % 1 == 0:
            new_vertex.edge_list.append(vertex_instance)
            vertex_instance.edge_list.append(new_vertex)

    vertex_list.append(new_vertex)


def traverse_graph(attempt, vertex_list, current_time):
    path = []

    vertex_list_length = len(vertex_list)

    for vertex_instance in vertex_list:
        vertex_instance.check_path(path, vertex_list_length)

    file = open("output{current_time}.txt".format(current_time=current_time), "a+")

    if len(path) == vertex_list_length:
        output = "{attempt} Success {path}".format(attempt=attempt, path=path)
    else:
        output = "{attempt} Fail".format(attempt=attempt)

    print(output)

    file.write("{output}\n".format(output=output))

    file.close()

    for vertex_instance in vertex_list:
        vertex_instance.traversed = False


def main():
    current_time = time.time()

    attempt = 0
    vertex_list = []

    while True:
        append_vertex_list(attempt, vertex_list)

        traverse_graph(attempt, vertex_list, current_time)

        attempt += 1


main()
