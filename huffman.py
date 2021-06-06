import graphviz as graphviz
from treelib import Node, Tree

# Creating tree nodes
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return "%s%s" % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=""):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + "0"))
    d.update(huffman_code_tree(r, False, binString + "1"))
    return d


class Huffman_Parser:
    def __init__(self):
        self.tree = Tree()
        self.node_ids = {}

    def huffman_printer(self, node, left=True):
        if type(node) is str:
            print(node)
        else:
            (l, r) = node.children()
            self.huffman_printer(l, True)
            self.huffman_printer(r, False)

    def huffman_tree_parse(self, node, left=True, binString="", parent=None):
        try:
            if not parent:
                # korzen
                print(f"Creating node id: {str(node)}. Root node.")
                self.tree.create_node(tag=f"{node} = {binString}", identifier=node)
                self.node_ids.update({str(node): 1})
            else:
                print(f"Creating node id: {str(node)}. Node parent: {str(parent)}")
                self.tree.create_node(
                    tag=f"{node} = {binString}", identifier=node, parent=parent
                )
                self.node_ids.update({str(node): 1})
        except Exception as e:
            print(e)
            print(f"Existing nodes: {self.node_ids}. Trying to get nodes:")

            for nd in self.node_ids:
                if self.tree.get_node(nd):
                    print(f"Node {nd} present.")
                else:
                    print(f"Node {nd} absent.")

            raise e

        if len(str(node)) > 1:
            (l, r) = node.children()
            self.huffman_tree_parse(l, True, binString + "0", parent=node)
            self.huffman_tree_parse(r, False, binString + "1", parent=node)

    def huffman_draw_edge_to_children(self, node, binstring=""):
        if len(str(node)) > 1:
            (l, r) = node.children()
            self.graph.edge(f"{node}={binstring}", f"{l}={binstring}0")
            self.graph.edge(f"{node}={binstring}", f"{r}={binstring}1")
            self.huffman_draw_edge_to_children(l, binstring + "0")
            self.huffman_draw_edge_to_children(r, binstring + "1")

    def huffman_tree_graph(self, root_node):
        self.graph = graphviz.Graph()
        self.huffman_draw_edge_to_children(root_node)
        return self.graph


def huffman_output(input_string):
    # Calculating frequency
    freq = {}
    for c in input_string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    return huffmanCode, freq, nodes[0][0]
