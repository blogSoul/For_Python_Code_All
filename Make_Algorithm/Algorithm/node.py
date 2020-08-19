class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    market = "kospi"
# 파이썬 클래스는 그자체가 하나의 네임스페이스이기 때문에 
# 인스턴스 생성과 상관없이 클래스 내의 메서드를 직접 호출할 수 있습니다.

print(dir())
# Node 클래스가 확인가능합니다.

print(Node.__dict__)
# Node 클래스가 어떻게 이루어져 있는지 확인이 가능합니다.

s1 = Node("a")
s2 = Node("b")
# 인스턴스 s1, s2를 Node 클래스로 호출해줍니다.
print(s1.__dict__)
print(s2.__dict__)

# 인스턴스의 네임스페이스에 해당 이름이 없으면 클래스의 네임스페이스로 이동합니다.