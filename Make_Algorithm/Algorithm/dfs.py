Graph = { 
    1: [2,3],
    2: [3,4,5],
    3: [5,7,8],
    4: [5],
    5: [6],
    6: [],
    7: [8],
    8: []
}
# dict 구조로 만든 임의의 그래프입니다.

def dfs(graph, start):
    tovisit = [start]
    visited = []
    while tovisit:
        last = tovisit.pop()
        visited.append(last)
        for i in graph[last]:
            if i not in visited + tovisit:
                tovisit.append(i)
    return visited
# dfs 형태로 돌아가는 코드입니다.

print(dfs(Graph, 1))
print(dfs(Graph, 2))