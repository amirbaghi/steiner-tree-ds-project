import re
from os.path import join


class FileHandler:

    # Method to read from file, returns three dictionaries containing info: comment, graph, terminals
    @staticmethod
    def read_stp_file(file_name):
        f = open(file_name, "r")

        lines = f.readlines()

        # Extracting Comment
        comment = {}
        current_line = 2
        while lines[current_line] != "End\n":
            findings = re.findall("Name|Creator|Remark|\".+\"", lines[current_line])
            comment[findings[0]] = findings[1]
            current_line += 1

        # Reaching Graph Section, Skipping blank lines
        current_line += 1
        while lines[current_line] == "\n":
            current_line += 1

        # Extracting Graph
        graph = {}
        current_line += 1
        nodes_findings = re.findall("Nodes|[0-9]+", lines[current_line])
        graph[nodes_findings[0]] = int(nodes_findings[1])
        current_line += 1
        edges_findings = re.findall("Edges|[0-9]+", lines[current_line])
        graph[edges_findings[0]] = int(edges_findings[1])
        current_line += 1
        edge_number = 1
        while lines[current_line] != "End\n":
            findings = re.findall("E|[0-9]+", lines[current_line])
            graph[edge_number] = list(map(int, [findings[1], findings[2], findings[3]]))
            edge_number += 1
            current_line += 1

        # Skipping blank lines until Terminal Section
        current_line += 1
        while lines[current_line] == "\n":
            current_line += 1

        # Extracting Terminals
        current_line += 1
        terminals = {}
        terminals_findings = re.findall("Terminals|[0-9]+", lines[current_line])
        terminals[terminals_findings[0]] = int(terminals_findings[1])
        current_line += 1
        terminal_number = 1
        while lines[current_line] != "End\n":
            findings = re.findall("T|[0-9]+", lines[current_line])
            terminals[terminal_number] = int(findings[1])
            terminal_number += 1
            current_line += 1

        f.close()

        return comment, graph, terminals

    # Method to write an output for a file, gets the file name, the cost,
    # and the graph edges as inputs and writes into a file
    # in the outputs directory, with the name being filename.out
    @staticmethod
    def write_output(filename, cost, edges):
        # Include your own directory here as the outputs dir
        path = join("/home/amir/Desktop/dev/steiner-tree-ds/steiner-tree-ds-project/outputs",
                    "".join([filename, '.out']))
        file = open(path, "w")

        # Writing out the Cost
        file.write(f"Cost {cost}")

        # Writing out the number of the edges
        file.write(f"\nEdges {len(edges)}")

        # Writing out the edges, with the nodes and the weight
        for edge in list(edges.values()):
            file.write(f"\nE {edge[0]} {edge[1]} {edge[2]}")

        file.close()
