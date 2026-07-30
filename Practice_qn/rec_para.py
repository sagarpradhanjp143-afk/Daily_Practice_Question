def math(x,n):
    if n==0:
       return
    print(x)
    math(x,n-1)

math(20,4)