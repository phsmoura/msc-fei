import pandas as pd
from matrices_methods import *


# Get features
def build_points(data: pd.DataFrame) -> list:
    x = [ [] for i in range(data.shape[0]) ]
    y = [ [] for i in range(data.shape[0]) ]

    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            if i < (data.shape[1] - 1):
                x[j].append(data.iloc[j,i])
            else:
                y[j].append(data.iloc[j,i])
    return [x,y]

def build_data(data: pd.DataFrame) -> list:
    x = [ [1] for k in range(data.shape[0]) ]
    y = [ [] for k in range(data.shape[0]) ]
    
    for i in range(data.shape[1]):
        for j in range(data.shape[0]):
            if i < (data.shape[1] - 1):
                x[j].append(data.iloc[j,i])
            else:
                y[j].append(data.iloc[j,i])

    return [x,y]

# methods
def linear(dataset: list) -> list:
    beta = find_beta(dataset[0], dataset[1])
    print("Beta: ", beta)
    n = len(beta)
    x = [i for i in range(3000)]
    y = [0 for i in range(len(x))]
    
    for j in range(len(x)):
        for i in range(n-1):
            y[j] = y[j] + x[j]*beta[i+1][0]
        y[j] = y[j] + beta[0][0]
    
    return [x,y]

def quadratic(dataset: list) -> list:
    for v in dataset[0]:
        v.append(v[1]*v[1])

    beta = find_beta(dataset[0], dataset[1])

    print("Beta: ", beta)

    # n = len(beta)
    x = [i for i in range(3000)]
    y = [0 for i in range(len(x))]

    for j in range(len(x)):
        y[j] = y[j] + x[j]*beta[1][0] + x[j]*x[j]*beta[2][0] + beta[0][0]

    return [x,y]
