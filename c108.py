import random
import plotly.figure_factory as ff
#import plotly.express as px
list_a = []
count = []
for i in range(0,100):
    val = random.randint(1,6)
    val2 = random.randint(1,6)
    list_a.append(val+val2)
    count.append(i)
    
#fig = px.bar(x=list_a,y = count)
#fig.show()

fig = ff.create_distplot([list_a],["Result"])
fig.show()
