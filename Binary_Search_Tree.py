# -*- encoding:utf-8 -*-
# __author__=='Gan'


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for node in node_list[1:]:
            self.insert(node)

    def search(self, data, node, parent):
        if node is None:
            return False, node, parent

        if node.data == data:
            return True, node, parent

        if node.data > data:
            return self.search(data, node.lchild, node)

        elif node.data < data:
            return self.search(data, node.rchild, node)

    def insert(self, data):
        flag, node, parent = self.search(data, self.root, self.root)
        if not flag:
            new_node = Node(data)

            if data > parent.data:
                parent.rchild = new_node
            else:
                parent.lchild = new_node

    def delete(self, root, data):
        flag, node, parent = self.search(data, root, root)
        if node == parent:
            if node.lchild is None:
                self.root = node.rchild
            elif node.rchild is None:
                self.root = node.lchild
        if flag is False:
            return False
        else:
            if node.lchild is None:
                if node == parent.lchild:
                    parent.lchild = node.rchild
                else:
                    parent.rchild = node.rchild
                del parent
            elif node.rchild is None:
                if node == parent.rchild:
                    parent.rchild = node.lchild
                else:
                    parent.lchild = node.lchild
                del parent
            else:
                pre = node.rchild
                if pre.lchild is None:
                    node.data = pre.data
                    node.rchild = pre.rchild
                    del pre
                else:
                    next_ = pre.lchild
                    while next_.lchild:
                        pre = next_
                        next_ = pre.lchild
                    node.data = next_.data
                    pre.lchild = next_.rchild
                    del pre

    def postOrderTraverse(self, node):
        if node is not None:
            print(node.data)
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)


if __name__ == '__main__':
    node_list = [0, 123, 34, 5, 6, -1]
    b = BST(node_list)
    print(b.postOrderTraverse(b.root))
    print(b.delete(b.root, 0))
    print(b.delete(b.root, 123))
    print(b.delete(b.root, 34))
    print(b.delete(b.root, 5))
    print(b.delete(b.root, 6))
    print(b.delete(b.root, -1))
    print(b.postOrderTraverse(b.root))



