# https://www.acmicpc.net/problem/1991

def preorder(node):
    global G, result
    if node == '.':
        return
    result.append(node)
    preorder(G[node][0])
    preorder(G[node][1])


def inorder(node):
    global G, result
    if node == '.':
        return
    inorder(G[node][0])
    result.append(node)
    inorder(G[node][1])


def postorder(node):
    global G, result
    if node == '.':
        return
    postorder(G[node][0])
    postorder(G[node][1])
    result.append(node)

import sys
input = sys.stdin.readline
n = int(input())
G = {}
for i in range(n):
    parent, left, right = input().split()
    G[parent] = [left, right]

result = []
preorder('A')
print(*result, sep='')

result.clear()
inorder('A')
print(*result, sep='')

result.clear()
postorder('A')
print(*result, sep='')
