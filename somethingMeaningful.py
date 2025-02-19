import math

def circle(x, x0, y0, r):
    '''
    Takes array x, center coords of the circle, and radius, and returns all y coordinates of the circle 
    Formula for circle:
        (x-x0)^2+(y-y0)^2=r^2
                thfr
        y = math.sqrt(r^2-(x-x0)^2)+y0
    '''
    y = []
    yLower = []
    for point in x:
        y.append(math.sqrt(r**2-(point-x0)**2))
        yLower.append((math.sqrt(r**2-(point-x0)**2))*-1)

    return y, yLower

def order_array(input_array):
    '''
    takes as input an array of numbers and returns a new array with the numbers ordered from smallest to largest.
    
    I make bubble sort
    '''
    lL = len(input_array)
    swapped = False

    for i in range(lL):
        swapped = False
        for j in range(lL - 1 - i): #total elements, iterate till last element (-1), minus the already sorted elements
            if(input_array[j] > input_array[j+1]): #if previous element is greater than next
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j] #swap elements
                swapped = True
        if not swapped:
            break
    return input_array
