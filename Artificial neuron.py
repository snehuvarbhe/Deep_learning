import math 

def sigmoid(h):
    return ((1.0)/(1+math.exp(-h)))

def activation(input,weights):
    h=0
    for i,w in zip(input,weights):
        h=h+i*w
    h=sigmoid(h)
    return h

if __name__=='__main__':
    input=[0.5,0.3,0.2]
    weights=[0.4,0.7,0.2]
    output=activation(input,weights)
    print(output)