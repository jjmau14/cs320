import sys
#from directed_graph import Digraph
from directed_graph import Digraph

# Feel free to use bipartite_recognition/core.py as a reference


def sort(directed_graph_filename):
    '''Given a file containing the edges of a directed graph,
    compute a topological sort of the nodes, returning them as a list.
    If the input graph is not a DAG, raise a ValueError with the nodes
    of cycle attached as a list, in cycle order.'''
    def read_edges_from_file(filename):
      '''The file should have lines of the form "x y",
      indicating that there is an edge between the node
      named "x" and the node named "y"'''
      with open(filename) as f:
        return [tuple(line.strip().split()) for line in f.readlines()]
    #  read in graph from file
    def read_graph_from_file(filename):
     '''Parse edges from the file and load them into a graph object.'''
     edges = read_edges_from_file(filename)
     g = Digraph()
     for v, u in edges:
        g.add_edge(v, u)
     return g
    g=read_graph_from_file(directed_graph_filename)
    #  compute a topological sort using DFS
    stack=[]
    stack1=[]
    result=[]
    node=list(g.nodes)
    color= [ 0 for i in range(len(node))]
    def dfs(i):
      stack.append(i)
      color[i]=1
				
      for n in g.neighbors(node[i]):
        if color[node.index(n)]==1:
          err = ValueError("There's a cycle in here!")
          cycleindex=stack[stack.index(node.index(n)):]
          err.cycle= [node[i] for i in cycleindex]
          raise err
        if color[node.index(n)]==0:
          dfs(node.index(n))
				
				
      stack.pop()
      color[i]=2
      stack1.append(node[i])
		
				
		
    for i in range(len(node)):
      if color[i]==0:
        dfs(i)
	
    for i in range(len(stack1)-1,-1,-1):
      result.append(stack1[i])
									

		
    #  return the sort as a list of nodes, like:
    return result
    #  unless you detect a cycle. If there is a cycle,
    #  there is no way to topologically sort the nodes.
    #  so create a ValueError object, like this:
    # err = ValueError("There's a cycle in here!")
    #  then attach a list of the nodes in the cycle, like this:
    # err.cycle = ['a', 'b', 'c']
    #  and raise the error, like this:
    # raise err


# For example, the file topological_sort/resources/graph1.txt looks like:
# a b
# b c
# c d
# And represents a graph like: a->b->c->d
# The function would return the topological sort as ['a', 'b', 'c', 'd']

# However, the file topological_sort/resources/graph3_cycle.txt looks like:
# a b
# b c
# c a
# And represents a graph like: a->b->c
#                              ^-----|
# It's a cycle of size three. The function would raise a ValueError.
# The error object would have a field, cycle, holding the nodes of the cycle.
# The cycle should be ['a', 'b', 'c'] or ['b', 'c', 'a'] or ['c', 'a', 'b']

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
