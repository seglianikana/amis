import re
import plotly
import plotly.graph_objs as go
from plotly import tools
'''
Функція plot() виводить зображення  графіків які було необхідно побудувати за даними

'''

def plot():
    
    keys_1=[]
    values_1=[]
    
    for (i,j) in res_num.items():
        keys_1.append(i)
        values_1.append(j)
    chart_1 = [go.Bar(x=keys_1, y=values_1)]
    layout = go.Layout(title="CountxName")
    fig = go.Figure(data=chart_1, layout=layout)
    plotly.offline.plot(fig, filename='plotly1.html')
   

    
    chart_2 = go.Pie(labels=list(f_m_num.keys()), values=list(f_m_num.values()))
    layout = go.Layout(title="Male/Female")
    fig2 = go.Figure(data=[chart_2], layout=layout)
    plotly.offline.plot(fig2, filename='plotly2.html') 

    chart_3 = [go.Bar(x=list(y_num.keys()), y=list(y_num.values()))]
    layout = go.Layout(title="people by year")
    fig = go.Figure(data=chart_3, layout=layout)
    plotly.offline.plot(fig, filename='plotly3.html')



def eliminate(line):
    result = re.split(',', line)
    result[5] = result[5][:1]
    return result




data = {
}
f_m_num = {'F':0 , 'M':0}
res_num={}
y_num={}
try:
    with open('StateNames.csv', 'r') as f:
        line_number=0
        
        for line in f:
            l = eliminate(line)
            if line_number != 0:
               
               name= l[1]
               year= l[2]
               gender=l[3]
               state= l[4]
               count = int(l[5])
               
               if state not in data:
                   data[state] = {}
               if year not in data[state]:
                   data[state][year] = dict()
               if gender not in data[state][year]:
                   data[state][year][gender] = dict()
               if name not in data[state][year][gender]:
                   data[state][year][gender][name] = dict()
               data[state][year][gender][name] = count
               if name not in res_num.keys():
                   res_num[name] =0
               else:
                   res_num[name] += count
               f_m_num[gender] += count     
               if year not in y_num.keys():
                   y_num[year] =0
               else:
                   y_num[year] += count
               
            line_number += 1
    
    plot()
   






except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))
