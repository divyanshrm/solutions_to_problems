

def distance(x, y):
    # calculate distance from origin
    x = x*x
    y = y*y
    ans = x + y
    return ans

if __name__="__main__":
    import random
    #calculates the distance from the origin and appends the counter if the point is in the circle
    c = 0
    u = 1000000000
    for _ in range(u):
        x = random.random()
        y = random.random()
        if distance(x, y) < 1:
            c += 1

    print(c * 4 / u)



    