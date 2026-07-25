n=121
num=n
result=0
while num>0:
   lar=num%10
   result=result*10+lar
   num=num//10
if n==result:
  print("it is a palindrome number")
else:
  print("it is not a palindrome number")