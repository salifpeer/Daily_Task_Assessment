#Program for multithreading using multithreading module
import threading
import time
def Calc_square(l):
    for i in l:
        time.sleep(0.4)
        print(f"the square is {i*i}")
def Calc_cube(l):
    for i in l:
        time.sleep(0.4)
        print(f"the cube is {i*i*i}")
if __name__=="__main__":
    a=[10,20,30]
    t1=threading.Thread(target=Calc_square,args=(a,))
    t2=threading.Thread(target=Calc_cube,args=(a,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("thread completed")

