import matplotlib.pyplot as plt
import csv 
import graficas
data =[]
def read_csv(path):
    with open ( path, 'r') as csvfile:
        reader= csv.reader(csvfile, delimiter=",")
        header = next(reader)
        for row in reader:
            codict=dict()
            for i,j in zip(header,row):
                if 'Country' in i or 'Population' in i  or "COL" in i:
                    codict[i]=j
            data.append(codict)
        return data
def read_csv_percentaje(path):
    with open ( path, 'r') as csvfile:
        reader= csv.reader(csvfile, delimiter=",")
        header = next(reader)
        for row in reader:
            codict=dict()
            for i,j in zip(header,row):
                if 'World' in i  or "Country" in i or "Continent" in i:
                    codict[i]=j
            data.append(codict)
        return data
def grafica(data,name):
    result= list(filter(lambda x:x["Country"]==name,data))[0]
    labels= list(result.keys())[1:-1]
    values= list(map(int,list(result.values())[1:-1]))
    fig, ax= plt.subplots()
    ax.bar(labels,values)
    plt.show()

def graficaContinents(data,name):
    data= list(filter(lambda x:x["Continent"]==name, data))
    result= list(map(lambda x:x["Country"],data))
    resultValues= list(map(lambda x:x["World Population Percentage"],data))
    graficas.generate_pie_chart(result, resultValues)

read_csv_percentaje("./funciones/app/data.csv")
graficaContinents(data, input("World population, per continent => "))