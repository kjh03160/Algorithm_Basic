"""
1. 다른 노드문제들 처럼 DFS로 풀 되, ORDER 순서를 지키지 않은 노드는 stack에 추가하지마세요
2. ORDER 순서를 지키지 않은 노드는 stack에 추가하진 않지만, AFTER에 넣어주고 나중에 따로 처리해 줄게요
3. stack에서 나온 tmp_node가 AFTER에 있나요? 그렇다면 ORDER순서에 따라 tmp_node 다음에 오는 노드도 stack에 넣어주세요
4. 이렇게해서 모든 노드를 방문할 수 있다면 True를 다 방문하지 못한 채 stack이 끝나버렸다면 False를 반환해주세요
"""
# https://programmers.co.kr/learn/courses/30/lessons/67260

def solution(n, path, order):
    answer = True
    G = {i: set() for i in range(n)}

    need_to_pass = [-1 for _ in range(n)]
    for a, b in path:
        G[a].add(b)
        G[b].add(a)

    after = [-1 for _ in range(n)]
    for a, b, in order:
        if b == 0:
            return False
        # b를 처리하기 전에 a를 처리해야됨
        need_to_pass[b] = a

    stack = [0]
    visited = [False for _ in range(n)]

    while stack:
        node = stack.pop()

        # 현재 노드 전에 처리해야되는 노드가 있고, 그것을 먼저 방문 안했으면
        if need_to_pass[node] != -1 and not visited[need_to_pass[node]]:
            # 먼저 방문해야되는 노드 이후 현재 노드를 처리하도록 마킹
            after[need_to_pass[node]] = node
            continue

        visited[node] = True
        for i in G[node]:
            if not visited[i]:
                stack.append(i)

        # 현재 노드 이후에 처리해야될 것이 있으면
        if after[node] != -1:
            stack.append(after[node])

    return True if False not in visited else False

n = 9
path =[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order =[[4,1],[8,7],[6,5]]
print(solution(n, path, order))