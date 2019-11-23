import math

class Vec():

    def __init__(self,*entries):
        self.coord = entries
        self.dim = len(entries)
    
    @classmethod
    def vec_add(cls,*vectors):
        return cls(* map(sum, zip(*vectors)))
    @classmethod
    def scalar(cls, vec, r):
        return cls(*(i*r for i in vec.coord))
    
    """def vec_add(*vectors):
        return Vec(* map(sum, zip(*vectors)))
    
    def scalar(vec, r):
        return Vec(*(i*r for i in vec.coord))"""
    
    # 인스턴스 메소드
    def __add__(self, other):
        if self.dim == other.dim:
            return self.__class__.vec_add(self.coord, other.coord)
        else:
            print("두 벡터의 차원이 같아야 합니다.")
    def __sub__(self, other):
        if self.dim == other.dim:
            #inverse = other.__class__.scalar(other, -1)
            inverse = other *-1
            return self.__class__.vec_add(self.coord, inverse.coord)
        else:
            print("두 벡터의 차원이 같아야 합니다.")
    
    def __rmul__(self, r):
        return self.__class__.scalar(self, r)
    
    def __mul__(self, r):
        return self.__class__.scalar(self, r)
    
    def __eq__(self, other):
        temp = True
        if self.dim == other.dim:
            for i in range(len(self.coord)):
                if round(self.coord[i]-other.coord[i],7)!=0.0:
                    return not temp
            return temp
        else:
            print("두 벡터의 차원이 같아야 합니다.")
    
    def __repr__(self):
        return str(self.coord)
    
    def __neg__(self):
        return -1*self
    
    def dot(self, other):
        if self.dim == other.dim:
            return sum([i*j for i,j in zip(self.coord, other.coord)])
        else:
            print("두 벡터의 차원이 같아야 합니다.")
            
    def norm(self):
        return round(math.sqrt(sum(map(lambda x:x**2, self.coord))),3)
    
    def distance(self, other):
        if self.dim == other.dim:
            temp = self-other
            return temp.norm()
        else:
            print("두 벡터의 차원이 같아야 합니다.")
    
    def unit(self):
        return 1/self.norm()*self
    
    def angle(self, other):
        return math.acos(self.dot(other)/(self.norm()*other.norm()))
#벡터구현함수입니다. __example__로 되어 있는 부분은 실제로 함수가 구현되어 있지만, 제가 직접 바꾸어서 만든 것입니다.

class Vec3(Vec):
    def __init__(self, x=0,y=0,z=0):
        super().__init__(x,y,z)
    def cross(self, other):
        (a1,b1), (a2,b2), (a3,b3)=zip(self.coord, other.coord)
        return Vec3(a2*b3-a3*b2, a3*b1-b1*b3, a1*b2-b1*a2)
#외적입니다.
