from sympy import *
import time
import math
import numpy as np
reg = "Newton Running"
def newton(var,objfun,x0 = 1):  #x0 is initial value given to NR method
    #var is a + b *h form
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
    print(reg)
    return step_size

if __name__ == '__main__':
        x0 = 3 # This are coordinates of initial guess
        y0 = 2
        x, y = symbols('x y')
        h = symbols('h')
        objfun = x ** 2 + y ** 2 + 2 * x  # This is our objective function
        # variables = [x,y]
        delfunx = Derivative(objfun,x).doit()
        delfuny = Derivative(objfun,y).doit()

        templist = [[delfunx.subs([(x, x0), (y, y0)]),delfuny.subs([(x, x0), (y, y0)])],]  # List of list of gradients of obj function
        itervalue = [[x0, y0], ]
        nextvalue = [[1, 1], ]  # No significance of [1,1] only to create 2d array like list
        nextvalue[0] = [itervalue[0][0] + h * templist[0][0], itervalue[0][1] + h * templist[0][1]]
        print("0. itervalue is", itervalue)
        print("0. templist is :", templist)
        print("0. nextvalue is ", nextvalue)

        step_size = [1,] #to initialize the array of step_sizes
        step_size[0] = newton(nextvalue[0],objfun)
        print("0. step_size is",step_size)

        itervalue.append([nextvalue[0][0].subs(h, step_size[0]), nextvalue[0][1].subs(h, step_size[0])])
        print("1. itervalue is", itervalue)
        templist.append([delfunx.subs([(x, itervalue[1][0]), (y, itervalue[1][1])]),
                         delfuny.subs([(x, itervalue[1][0]), (y, itervalue[1][1])])])
        print("1. templist is :", templist)
        nextvalue.append([itervalue[1][0] + h * templist[1][0], itervalue[1][1] + h * templist[1][1]])
        print("1. nextvalue is ", nextvalue)
        step_size.append(newton(nextvalue[1], objfun))
        print("1. step_size is ",step_size[1])

        itervalue.append([nextvalue[1][0].subs(h, step_size[1]), nextvalue[1][1].subs(h, step_size[1])])
        print("2. itervalue is", itervalue)
        templist.append([delfunx.subs([(x, itervalue[2][0]), (y, itervalue[2][1])]),
                         delfuny.subs([(x, itervalue[2][0]), (y, itervalue[2][1])])])
        print("2. templist is :", templist)
        nextvalue.append([itervalue[2][0] + h * templist[2][0], itervalue[2][1] + h * templist[2][1]])
        print("2. nextvalue is ", nextvalue)
        step_size.append(newton(nextvalue[2], objfun))
        k = 1
        i = 1
        # while k == 1:
        #     print("Iteration number :" , i+2 )
        #     step_size[i] =  newton(nextvalue[i],objfun)
        #     itervalue.append([nextvalue[i][0].subs(h, step_size[i]), nextvalue[i][1].subs(h, step_size[i])])
        #     print("itervalue is", itervalue)
        #     templist.append([delfunx.subs([(x, itervalue[i][0]), (y, itervalue[i][1])]),
        #                      delfuny.subs([(x, itervalue[i][0]), (y, itervalue[i][1])])])
        #     print("templist is :", templist)
        #     nextvalue.append([itervalue[i][0] + h * templist[i][0], itervalue[i][1] + h * templist[i][1]])
        #     print("nextvalue is ",nextvalue,sep="\n")
        #     i=i+1
        #     if i == 60:
        #         break



        # k = 1
        # iteration_no = 0
        # while k == 1: #assumed 10 iteration required taking index 0 to 9
        #     print("Iteration No. ",iteration_no+1)
        #     time.sleep(1)
        #     nextvalue.append([ itervalue[iteration_no][0] + h * templist[iteration_no][0] , itervalue[iteration_no][1] + h * templist[iteration_no][1]])
        #     step_size = newton(nextvalue[iteration_no],objfun) #stepsize of iteration
        #     print("h is : ",step_size)
        #     itervalue.append([nextvalue[iteration_no][0].subs(h, step_size), nextvalue[iteration_no][1].subs(h, step_size)])
        #     templist.append([delfunx.subs(x,itervalue[iteration_no][0]),delfuny.subs(y,itervalue[iteration_no][1])])
        #     if templist[iteration_no][0] == 0 and templist[iteration_no][1] == 0:
        #         # print("Solution obtained:")
        #         break
        #     # print(f"Step size (h) for iteration no. {iteration_no+1} is {step_size}")
        #     # print("itervalue" , itervalue)
        #     print("templist",templist)
        #     iteration_no += 1
