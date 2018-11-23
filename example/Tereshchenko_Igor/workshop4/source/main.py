import plotly
import plotly.graph_objs as go

from example.Tereshchenko_Igor.workshop4.source.data.dataset import dataset

from example.Tereshchenko_Igor.workshop4.source.data.data_helpers import *

from example.Tereshchenko_Igor.workshop4.source.datascience.lib import *

if __name__ == "__main__":


    addNewUser(dataset,"Kiki","kiki@kpi.ua",20)

    addNewOrder(dataset,"kiki@kpi.ua","22.11.2018","ATB")

    addProductToOrder(dataset,"kiki@kpi.ua","22.11.2018","tea",0.2,15.6)
    addProductToOrder(dataset,"kiki@kpi.ua","22.11.2018","sugar",0.5,15.6)



    productsWeight = getProductWeight(dataset)
    allUsersExpenses = getAllUsersExpenses(dataset)

    labels = list( allUsersExpenses.keys() )
    values = list ( allUsersExpenses.values() )

    trace = go.Pie(labels=labels, values=values)

    plotly.offline.plot([trace], filename='getAllUsersExpenses.html')


    trace0 = go.Bar(
        x= list( productsWeight.keys() ),
        y= list (productsWeight.values() ),
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title=' Report',
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='productsWeight.html')


    print(getUserExpenses(dataset,"kiki@kpi.ua"))