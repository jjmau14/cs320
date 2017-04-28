import sys
from directed_graph import Graph
#from directed_graph import Digraph

# Feel free to use bipartite_recognition/core.py as a reference

def read_edges_from_file(filename):
    '''The file should have lines of the form "x y",
    indicating that there is an edge between the node
    named "x" and the node named "y"'''
    with open(filename) as f:
        return [tuple(line.strip().split()) for line in f.readlines()]
	
def read_graph_from_file(filename):
    edges = read_edges_from_file(filename)
    g = Graph()
    for v, u in edges:
        g.add_edge(v, u)
    return g

def sort(directed_graph_filename):
	g = read_graph_from_file(directed_graph_filename)
	topoSort = []
	edges = g.get_edges()
	while len(topoSort) != len(g.get_nodes()):
		break
	for k,v in g.get_edges():
		print(k + "->" + v)

	
def main(argv):
    '''An example main to make it easy to try from the command line'''
    if len(argv) < 2:
        print('Must provide a filename for the graph to work on.')
        exit(1)
    graph_filename = argv[1]
    try:
        topo_sort = sort(graph_filename)
        print('Graph is a DAG. It\'s topological sort is:')
        print(topo_sort)
    except ValueError as err:
        print('Graph contains a cycle, cannot perform a topological sort.')
        print('The cycle is: {}'.format(err.cycle))

if __name__ == "__main__":
    main(sys.argv)
