# https://www.acmicpc.net/problem/4256

class Tree:
    def __init__(self):
        self.root = None

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.value, end=" ")

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def set_right(self, node):
        self.right = node

    def set_left(self, node):
        self.left = node


def answer(T, preorder, inorder):
    if not preorder:
        return
    root_value = preorder[0]
    node = Node(root_value)

    if len(inorder) == 1:
        return node
    division = inorder.index(root_value)

    left_sub = inorder[:division]
    right_sub = []
    if division + 1 < len(inorder):
        right_sub = inorder[division + 1:]

    left_pre = preorder[1: 1 + len(left_sub)]
    right_pre = preorder[len(left_pre) + 1:]

    left = answer(T, left_pre, left_sub)
    right = answer(T, right_pre, right_sub)

    node.left = left
    node.right = right
    return node


import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    T = Tree()
    visited = [False for _ in range(len(inorder))]

    T.root = answer(T, preorder, inorder)
    T.postorder(T.root)
    print()
