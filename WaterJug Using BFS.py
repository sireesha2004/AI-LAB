class Waterjug:
  def __init__(self,a,b,target):
    self.a=a
    self.b=b
    self.target=target
    
  def solution(self):
    explored=[]
    frontier=[]
    frontier.append([0,0,[]])
    while frontier:
        node=frontier.pop(0)
        x=node[0]
        y=node[1]
        path=node[2]
        if x==self.target or y==self.target:
            print("Target Found")
            return len(path),path+[(x,y)]

        if [x,y] not in explored:
            explored.append([x,y])
            current_path=path+[(x,y)]
            frontier.append([0,y,current_path])
            frontier.append([x,0,current_path])
            frontier.append([self.a,y,current_path])
            frontier.append([x,self.b,current_path])
            frontier.append([max(0,x-(self.b-y)),min(self.b,y+x),current_path])
            frontier.append([min(self.a,x+y),max(0,y-(self.a-x)),current_path])
j1=int(input("capacity of jug1: "))
j2=int(input("capacity of jug2: "))
g=int(input("amout of water to be measwured: "))
steps,path=Waterjug(j1,j2,g).solution()
if steps!=-1:
    print(steps)
    print("Path:")
    for i in path:
        print(i)


output:-
capacity of jug1: 7
capacity of jug2: 4
amout of water to be measwured: 5
Target Found
8
Path:
(0, 0)
(0, 4)
(4, 0)
(4, 4)
(7, 1)
(0, 1)
(1, 0)
(1, 4)
(5, 0)
In [ ]:


​

