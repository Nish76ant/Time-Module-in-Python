#Time Module in Python
#Time Module is Basically use in Python to known the execution time of Program
#time.sleep is used for gap
import time

intial = time.time()
print(intial)

k = 0
while(k<45):
    print('This is Nishant Bhai')
    time.sleep(5)  #time.sleep is used for gap
    k = k+1
print('While loop ran in',time.time()-intial,'Seconds')

intial2 = time.time()
for i in range(45):
     print('This is Nishant Bhai')
print('While loop ran in',time.time()-intial2,'Seconds') 


#For Local time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)







