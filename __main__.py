import numpy as np
from src.example import square, rectangle, circle

print("_____menu_____")
print("1: to find area of square \n\
2: to find area of rectangle\n\
3: to find area of circle")
  
ch = int(input())
  
if ch == 1:
    print("enter side")
    s = int(input())
    print ("the area is ", square(np.float64(s)))
  
if ch == 2:
    print("enter length and width")
    l = int(input())
    w = int(input())
    print("the area is ", rectangle(np.float64(l), np.float64(w)))
  
if ch == 3:
    print("enter radius")
    r = int(input())
    print("the area is ", circle(np.float64(r)))