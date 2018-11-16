class Vertex(object):
    def __init__(self, number):
        self.number = number
        self.edge_list = []

        self.traversed = False

    def check_path(self, path, vertex_list_length):
        self.traversed = True

        path.append(self.number)

        for edge_instance in self.edge_list:
            if not edge_instance.traversed:
                edge_instance.check_path(path, vertex_list_length)

        if len(path) == vertex_list_length:
            return

        path.pop()

        self.traversed = False
