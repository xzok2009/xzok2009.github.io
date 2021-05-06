import random
# import matplotlib.pyplot
class Agent:
    def __init__(self,environment,agents,x,y):
        self.environment = environment
        self.agents = agents
        self.x = x
        self.y = y
        self.store = 0  # We'll come to this in a second.
        if (x == None):
         self._x = random.randint(0,100)
        else:
         self._x = x
        if (y == None):
         self._y = random.randint(0,100)
        else:
         self._y = y
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    def eat(self):  # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def share_with_neighbours(self, neighbourhood):
     for agent in self.agents:
        dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
     return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
# f = open("in.txt")
# environment=[]
# for row in f:
#     parsed_line = str.split(row,",")
#     # print(parsed_line)
#     rowlist=[]
#     for values in parsed_line:
#         rowlist.append(float(values))  
#         environment.append(rowlist)
#print(environment[10])
# f.close()

