def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
from functools import reduce
def fn(x,y):
    return x * 10 + y
r = reduce(fn,[1,3,5,7,9])
print(r)
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(fn,list(map(char2num,s)))
print(str2int("3579"))
##############test 1#######################
def normalize(name):
    name = name.capitalize()
    return name
L1 = ["adam","LISA","barT"]
L2 = list(map(normalize,L1))
print(L2)
###############test 2####################
def prod(l):
    def ji(x,y):
        return x * y
    return reduce(ji,l)
print(prod([2,4,8]))
############test 3#######################
def str2float(s):
    s = s.split(".")
    frontNum = s[0]
    backNum = s[1]
    backNum = backNum + "0"
    def f1(x,y):
        return x * 10 + y
    def f2(x,y):
        return x/10 + y/10
    def char2Num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    return reduce(f1,map(char2Num,frontNum))+reduce(f2,map(char2Num,backNum[-1::-1]))
print(str2float("123.456"))
