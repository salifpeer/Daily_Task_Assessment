#Program for multiprocessing
import multiprocessing
import time
def Calc_square(l):
    for i in range(0,len(l)):
        time.sleep(0.4)
        print(f"the square is {l[i]*l[i]}")
        
def Calc_cube(l):
    for i in range(0,len(l)):
        time.sleep(0.4)
        print(f"the cube is {l[i]*l[i]*l[i]}")
def square(l):
    for i in range(0,len(l)):
        time.sleep(0.4)
        print(f"the square is {l[i]*l[i]}")
        
def cube(l):
    for i in range(0,len(l)):
        time.sleep(0.4)
        l[i]=l[i]*l[i]
    print(f"The list inside process p3 is {l}")
if __name__=="__main__":
    l=[10,20,30]
    p1=multiprocessing.Process(target=Calc_square,args=(l,))
    p2=multiprocessing.Process(target=Calc_cube,args=(l,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
#processes cannot modify the global data
    print(f"List before execution p3 {l}")
    p3=multiprocessing.Process(target=cube,args=(l,))
    p3.start()
    p3.join()
    print(f"List after the execution of p3 {l}")