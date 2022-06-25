
def getGCD(*args)->int:
    for i in args:
        if type(i) != int:
            raise TypeError(f' "{i}" is not an integer')
        if i <= 0:
            raise ValueError(f'negative number or zero detected {i}')
    if len(args) >= 2:
        d = [*args]
        d.sort()

        minNum = d[0]
        maxNum = d[-1]

        minNum_hcf = [i for i in range(1,minNum+1) if maxNum %i==0]
        print(f'minNum_hcf {minNum_hcf}')
        union_set = []
        # def water(d):
        index = 0
        d = d[:-1]
        while index <= len(d)-1:
            hcf = [i for i in minNum_hcf if d[index]%i==0]
            union_set.append(hcf)
            index+=1
        
        print(f'The GCD of {args} is {union_set[0][-1]}')
        # u = [union_set[i] & union_set[i+1] for i,item in enumerate(union_set) if i<len(union_set)-1]
        # print(u)
        print()
    else:
        raise TypeError(f'Two or more arguments are needed getGCD{args}')


getGCD(12, 17)
getGCD(4, 6)
getGCD(336, 360)
# getGCD(128,96)
# getGCD(6,36)
# getGCD(360,210)
# getGCD(108 ,144)
# getGCD(36, 54, 90)
# getGCD(24, 148, 36)
# getGCD(15, 145, 155,5)

# TypeError: len() takes exactly one argument (2 given)
# def twoGCD(num1:int,num2:int)->int:
#     if num1 < num2:
#         minNum = num1
#     else:
#         minNum = num2
#     hcf = [i for i in range(1,minNum+1) if num1%i==0 and num2%i==0]
#     minNum = None
#     if num1 < num2:
#         minNum = num1
#     else:
#         minNum = num2
#     hcf = [i for i in range(1,minNum+1) if num1%i==0 and num2%i==0]
#     print(hcf[-1])
