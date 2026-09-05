# def Factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# print(Factorial(10))

import json

with open("data.json") as f:
    py_object=json.load(f)
    print((py_object))
