import os
import sys

print("Sample Python Code")

#### String work ############
mystr = "Hello World"
print("Mystr: ", mystr)
print("reverse Str: ", mystr[::-1])
print("Capitilize: ", mystr.capitalize())
print("Upper ", mystr.upper())


######## List, Tuple Work ###########
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)

print("Mylist: {}, Mytuple {}".format(mylist, mytuple))



############# Dict work ###############
mydict = {1: "hi", 2: "hello"}
print("Mydict: {mydict}".format(mydict=mydict))

for k, v in mydict.items():
    print("key {}, Value {}".format(k, v))

############ List Comprehension, map, filter, zip, lambda #######
s = [x*2 for x in range(10)]
print("My new list updated data: ", s)

m = [1, 2, 3, 4]
n = ['a', 'b', 'c', 'd']
def Sq(n):
    return n*2
print("Square of m list: ", list(map(Sq, m)))
print("Filtered of m list: ", list(filter(Sq, m)))
print("zipped of two lists: ", list(zip(m, n)))

Sq = lambda n: n * 2
print("Lambda Result: ", Sq(5))


############## Decorators ######################

def mydec(fun):
    def mywrapper(x):
        print("Before calling function: ", x)
        x = 1
        print("after modify x: ", x)
        fun(x)
        x = 2
        print("After calling function: ", x)
    return mywrapper

@mydec
def sapm(x):
    print("x values is: ", x)

sapm(4)


########### Generators  #########

def create_cube(n):
    for x in range(n):
        yield x*3

g = create_cube(10)
print(g)
print(next(g), next(g))


###### Sample Class to execute the Class instance program  ########
class SampleClass:
    def __init__(self, **kwargs):
        self.ARGS = kwargs

    def samplerun(self):
        print("Hello....!")
        print("Datas: {}".format(self.ARGS))


objsample = SampleClass(Myname="Chetan", Surname="Jadhav", Designation="Technical Architect")
objsample.samplerun()


class childclass(SampleClass):
    def __init__(self, **kwargs):
        SampleClass.__init__(self, x=kwargs)
        self.childARGS = kwargs

    def childexec(self):
        print(self.childARGS)

objchild = childclass(Myname="Chetan", Surname="Jadhav", Designation="Technical Architect")
objchild.samplerun()
objchild.childexec()

class A:
    def __init__(self, a=1):
        self.a = a
        self.__secured = 1
        # print(self.a)
        # print(self.__secured)

    def mytest(self):
        print(self.a)
        print(self.__secured)

class B(A):
    def __init__(self, b=2):
        super().__init__(a=2)
        self.b = b

    def mytest(self):
        A().mytest()
        print(self.b)

obj = B()
obj.mytest()


from abc import ABC, abstractmethod

class AA(ABC):
    @abstractmethod
    def mymethod(self):
        pass

class BB(AA):
    def mymethod(self):
        print("hello world...!")

objABC = BB()
objABC.mymethod()
