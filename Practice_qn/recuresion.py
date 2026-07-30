count=0
def fun():
    global count
    if count==4:
        return 
    print("Sagar Pradhan")
    count+=1
    fun()
print(fun())
