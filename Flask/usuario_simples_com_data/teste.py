from datetime import *

def transformar_data(data:list):
    data = date(data[0], data[1], data[2])
    print(data)

transformar_data([2000,1,1])