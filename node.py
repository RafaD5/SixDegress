class Node:
    def __init__(self, article, parent):
        self.article = article # String
        self.parent = parent # Node

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.article == other.article
        return False

if (__name__ == '__main__'):
    head_node = Node("/wiki/Albert_Einstein", None)
    child_one = Node("/wiki/Theory_of_relativity", head_node)
    child_two = Node("wiki/ETH_Zurich", head_node)
    child_tree = Node("/wiki/Albert_Einstein", child_two)

    print(head_node == child_two)
    print(head_node == child_tree)
