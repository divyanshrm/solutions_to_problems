import random
import math
def generate():
    return [random.random(),random.random()]
def distance(x,y):
    #calculate distance from origin
    x=pow(x,2)
    y=pow(y,2)
    ans=x+y
    return math.sqrt(ans)
def give(data):

    c=0
    for x in data:
        if distance(x[0],x[1])<=1:
            c+=1
    return c
def calculate_pi(n):

    arr=[]
    for x in range(n):
        arr.append(generate())
    return (give(arr)*4/n)

if __name__=='__main__':
    x=input("enter the number of samples for accuracy, more the number of samples, more is the accuracy: ")
    print(calculate_pi(int(x)))
    