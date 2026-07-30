count=0
def fun():
    global count
    if count==5:
       return 
   
    count+=1
    fun()
    print("jay shree ram")

fun()
