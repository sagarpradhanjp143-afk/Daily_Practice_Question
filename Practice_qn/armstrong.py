n=153
num=n
total=0
nol=len(str(n))
while num>0:
    dig=num%10
    total=total+(dig**nol)
    num=num//10


if total==n:
   print(n,"is a Armstrong number")
else:
  print(n,"is not a Armstrong number")

