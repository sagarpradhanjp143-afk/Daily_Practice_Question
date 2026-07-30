def math(i,n):
    if i>n:
        return
    print(i)
    math(i+1,n)
  

math(1,4)

def math(i,n):
    if i>n:
        return
    
    math(i+1,n)
    print(i)

math(1,4)