from sympy import *
import time
import math
import numpy as np
def newton(var,objfun,x0 = 1):  #x0 is initial value given to NR method
    print(var)
    functionh = objfun.subs([(x,var[0]),(y,var[1])])
    delfunctionh = Derivative(functionh,h).doit()
    max_iter = 50 #maximum iteration in NR method can be setted here
    k = 0
    ary = [0,]*16
    ary[0] = x0
    for i in range(15): #Assumed that we get correct answer in 15 iteration of NR method.
        # To increase the number of iteration you also have to increase the number of entries in ary.
        ary[i+1] = ary[i] - (functionh.subs(h,ary[i]))/(delfunctionh.subs(h,ary[i]))
        step_size = float(ary[i+1])
    return step_size
if __name__ == '__main__':
        x0 = 3 # This are coordinates of initial guess
        y0 = 2
        x, y = symbols('x y')
        objfun = x ** 2 + y ** 2 + 2 * x  # This is our objective function
        variables = [x,y]
        itervalue = [[x0,y0],]
        delfunx = Derivative(objfun,x).doit()
        delfuny = Derivative(objfun,y).doit()
        templist = [[delfunx.subs([(x, x0), (y, y0)]),delfuny.subs([(x, x0), (y, y0)])],]  # List of list of gradients of obj function
        rows, cols = (10, 2)
        nextvalue = [[0,0]] * 100#[[0 for i in range(cols)] for j in range(rows)]
        h = symbols('h')
        k = 1
        iteration_no = 0
        while k == 1: #assumed 10 iteration required taking index 0 to 9
            print("Iteration No. ",iteration_no+1)
            # time.sleep(1)
            nextvalue[iteration_no][0] = itervalue[iteration_no][0] + h * templist[iteration_no][0]
            nextvalue[iteration_no][1] = itervalue[iteration_no][1] + h * templist[iteration_no][1]
            step_size = newton(nextvalue[iteration_no],objfun) #stepsize of iteration
            itervalue.append([nextvalue[iteration_no][0].subs(h, step_size), nextvalue[iteration_no][1].subs(h, step_size)])
            templist.append([delfunx.subs(x,itervalue[iteration_no][0]),delfuny.subs(y,itervalue[iteration_no][1])])
            if templist[iteration_no][0] == 0 and templist[iteration_no][1] == 0:
                print("Solution obtained:")
                break
            # print(f"Step size (h) for iteration no. {iteration_no+1} is {step_size}")
            # print("itervalue" , itervalue)
            # print("templist",templist)
            iteration_no += 1
        print(nextvalue[-1][0].subs(h,step_size),nextvalue[-1][1].subs(h,step_size))
