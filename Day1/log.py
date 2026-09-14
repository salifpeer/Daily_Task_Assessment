import logging
logging.basicConfig(level=logging.INFO,filename="demo.txt",filemode="a+")
logger=logging.getLogger(__name__)
def vote(age):
    if age<=0:
        raise Exception("you have entered an invalid age")
    if age>18:
        print("Perrson can vote")
    else:
        print("Person cannot vote")
for i in range(0,5):
 try:
    print("enter the age")
    a=int(input())
    vote(a)
 except Exception as e:
    logger.exception(e)

