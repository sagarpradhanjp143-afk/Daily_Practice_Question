n=[1,2,4,5,3,1,3,2,4,5,6]
m=[1,3,55,33,2,4,5,6]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(num, "occurs", count, "times")