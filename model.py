# import operator
import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import matplotlib.animation 
# import requests
# import bs4

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
# content = r.text
# soup = bs4.BeautifulSoup(content, 'html.parser')
# td_ys = soup.find_all(attrs={"class" : "y"})
# td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys)
# print(td_xs)
f = open("in.txt")
environment=[]
random.shuffle(environment)
for row in f:
    parsed_line = str.split(row,",")
    rowlist=[]
    for values in parsed_line:
        rowlist.append(int(values))
    environment.append(rowlist)
f.close()
# Make the agents.
for i in range(num_of_agents):
    # y = int(td_ys[i].text)
    # x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents))
# print(agents, type(agents))
#Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
         agents[i].move()
         agents[i].eat()
         agents[i].share_with_neighbours(neighbourhood)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
# matplotlib.pyplot.show()
for agents_row_a in agents:
      for agents_row_b in agents:
          distance = agentframework.Agent(environment,agents)             
carry_on = True
def update(frame):
    fig.clear()
    global carry_on
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i].y  = (agents[i].y + 1) % 99
        else:
            agents[i].y  = (agents[i].y - 1) % 99
        if random.random() < 0.5:
            agents[i].x  = (agents[i].x + 1) % 99
        else:
            agents[i].x  = (agents[i].x - 1) % 99
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    for i in range(num_of_agents):
        print(agents[i].x, agents[i].y)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
# matplotlib.pyplot.show()
def run():
  animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
  canvas.show()
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()