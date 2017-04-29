import sys
from directed_graph import graph

def sort(directed_graph_filename):

	def read_edges_from_file(filename):
		with open(filename) as f:
			return [tuple(line.strip().split()) for line in f.readlines()]
	
	def read_graph_from_file(filename):
		edges = read_edges_from_file(filename)
		g = graph()
		for v, u in edges:
			g.add_edge(v, u)
		return g
    
	g = read_graph_from_file(directed_graph_filename)
	st = []
	stack = []
	result = []
	node = list(g.nodes)
	color = [0 for i in range(len(node))]
    
	def depth_first_search(i):
		st.append(i)
		color[i]=1
		for n in g.neighbors(node[i]):
			if color[node.index(n)] == 1:
				err = ValueError("ERROR: Cycle Found!")
				cycleindex = st[st.index(node.index(n)):]
				err.cycle = [node[i] for i in cycleindex]
				raise err
			if color[node.index(n)] == 0:
				depth_first_search(node.index(n))
			
		st.pop()
		color[i] = 2
		stack.append(node[i])
			
	for i in range(len(node)):
		if color[i] == 0:
			depth_first_search(i)
	
	for i in range(len(stack)-1,-1,-1):
		result.append(stack[i])

	return result

def main(argv):
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
