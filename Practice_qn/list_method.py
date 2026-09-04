# append(addd one elemnt in the last)

# marks=[10,20,30,40]
# marks.append(50)
# print(marks)

# insert(idx, val) insert element at idx
# marks.insert(1,69)
# print(marks)

# sort
# marks.sort()
# print(marks)

# reverse
# marks.reverse()
# print(marks)


# num=[1,2,3,4,5,6]
# for i in num:
#     print(i)
num=[1,2,3,4,5,6]
idx=1
t=6
for i in num:
    if i==t:
        print(idx)
        break
    idx+=1