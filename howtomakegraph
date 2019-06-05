class Node(object):
    def __init__(self, name):
        """name은 string"""
        self.name = name
    #초기화 
    def getName(self):
        return self.name
    def __repr__(self):
        return self.name
    #node의 속성을 만들고 초기화를 해주는 과정이다.
    #node는 점 하나 하나를 의미한다.
class Edge(object):
    def __init__(self, src, dest):
        """src와 dest는 각각 Node 객체"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __repr__(self):
        return self.src.getName() + '->' + self.dest.getName()
    #src는 출발점, dest는 도착지점
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """src와 dest는 각각 Node 객체, weight는 숫자"""
        super().__init__(src, dest)
        self.weight = weight
        #weight는 출발점에서 도착지점으로 갈 때, 값을 나타낸다.
    def getWeight(self):
        return self.weight
    def __repr__(self):
        return self.src.getName() + '-(' + str(self.weight) + ')->' + self.dest.getName()
    #__repr__은 변수를 부를 때, 값을 프린트해주는 클래스 함수이다.
    
class Digraph(object):
    """
    nodes는 graph에 있는 node들의 list
    edges는 각 node에 자식 node들의 list를 대응시키는 dict
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('이미 존재하는 node입니다.')
            #이미 존재하는 node를 다시 지정해줄 이유는 없다.
        else:
            self.nodes.append(node)
            self.edges[node] = []
            #출발점의 노드를 기준으로 edges를 넣고 부모-자식 클래스처럼 이용하고 있다.
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("node가 graph에 포함되어 있지 않습니다.")
            #src와 dest가 같으면 필요가 없다.
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    #nodes 안에 node값이 있는지 확인해주는 함수이다.
    def __repr__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1] # 마지막 '\n'd을 제외, 마지막 도착지에는 어느 다른 곳으로 갈 수 없기 때문에 -1로 지정해주는 것이다.

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        #Edge값은 출발점에서 도착점으로 가는 것도 값을 가지고 있지만 , 도착점에서 출발점으로 가는 것도 값을 가지고 있다.
class Digraph(object):
    """
    nodes는 graph에 있는 node들의 list
    edges는 각 node에 자식 node들의 list를 대응시키는 dict
    """
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('이미 존재하는 node입니다.')
            #이미 존재하는 node를 다시 지정해줄 이유는 없다.
        else:
            self.nodes.append(node)
            self.edges[node] = []
            #출발점의 노드를 기준으로 edges를 넣고 부모-자식 클래스처럼 이용하고 있다.
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("node가 graph에 포함되어 있지 않습니다.")
            #src와 dest가 같으면 필요가 없다.
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    #nodes 안에 node값이 있는지 확인해주는 함수이다.
    def __repr__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1] # 마지막 '\n'd을 제외, 마지막 도착지에는 어느 다른 곳으로 갈 수 없기 때문에 -1로 지정해주는 것이다.

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        #Edge값은 출발점에서 도착점으로 가는 것도 값을 가지고 있지만 , 도착점에서 출발점으로 가는 것도 값을 가지고 있다.
        
      def BFS(graph, start, end, toPrint=False):
    """
    입력::
    graph: Digraph
    start, end: 각각 Node 객체
    출력::
    shortest path
    """
    initPath = [start]
    pathQueue = [initPath]
    #pathQueue는 경로를 저장해주는 리스트이다.
    if toPrint:
        print('Current BFS path:', printPath(initPath))
    while len(pathQueue) !=0:
        tmpPath = pathQueue.pop(0) # pathQueues에서 가장 오래된 성분을 꺼내기
        #pop은 마지막 리스트부터 뽑는 것이나 pop(0)면 처음 있는 것을 뽑는 다는 것을 알아두자
        #FILO : first in last out이 pop형태
        #FIFO : first in first out 은행 돈 인출 현황 
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None
#BFS는 stack과 비슷하다.   
