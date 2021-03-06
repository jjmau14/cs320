import copy
from collections import defaultdict

def normalize_attributes(attributes):
    if attributes == None:
        attributes = {}
    if not isinstance(attributes, (dict, set)):
        raise ValueError('attributes must be a dict or a set')
    return attributes

class graph:
    def __init__(self):
        self.nodes = {}
        self.edges = defaultdict(dict)

    def __repr__(self):
        return str({'nodes': self.nodes, 'edges': self.edges})

    def copy(self):
        ret = Graph()
        ret.nodes = copy.deepcopy(self.nodes)
        ret.edges = copy.deepcopy(self.edges)
        return ret

    def add_node(self, identity, attributes=None):
        self.nodes[identity] = normalize_attributes(attributes)

    def ensure_node(self, identity):
        if identity not in self.nodes:
            self.add_node(identity)

    def add_edge(self, identity1, identity2, attributes=None):
        attributes = normalize_attributes(attributes)
        self.ensure_node(identity1)
        self.ensure_node(identity2)
        self.edges[identity1][identity2] = attributes
        

    def get_nodes(self):
        return self.nodes.keys()

    def get_edges(self):
        return ((a, b) for a in self.edges for b in self.edges[a])

    def neighbors(self, identity):
        if identity in self.edges:
            return self.edges[identity].keys()
        return set()

    def attributes_of(self, identity, identity2=None):
        if identity2 == None:
            return self.nodes[identity]
        return self.edges[identity][identity2]
