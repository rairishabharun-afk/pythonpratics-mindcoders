# age = 21
# print (age)

# name = "rishuu"
# profession = "Machine Learning "
# experince = 1
# print("Hello, I am",name,".I am ",profession,".I have",experince,"year experince.")

# x = 5
# print(type(x))
# x = "5"
# print(type(x))
# x = 5.5
# print(type(x))
# x = 1j
# print(type(x))
# x = True
# print(type(x))
# x =["apple","banana","cherry"]
# print(type(x))
# x = ("apple","banana","cherry")
# print(type(x))
# x = {"apple","banana","cherry"}
# print(type(x))
# x =range(6)
# print(type(x))
# x =True
# print(type(x)) 
# x =frozenset({"apple","banana","cherry"})
# print(type(x))
# x=b"Hello"
# print(type(x))
# x=bytearray(5)
# print(type(x))
# x = None
# print(type(x))
# x = memoryview(bytes(5))
# print(type(x))
# x ={"a":"1","b":"2"}
# print(type(x))


# for temp in range (1,7):
#     print(str(temp)*temp)

#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#     for iterator in range(len(my_list)):
#         print(my_list[iterator])

#     my_list = [1,2,3,4,5,6,7,8,9,10]
#     for iterator in range(len(my_list)):
#         print(my_list[iterator])    

# list=[]
# for iterator in range(10):
#         list.append(iterator+1)
# print(list)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
# for count in range (10):
#     list[count]+=1
# print(list)
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# total = 0
# for sum in list:
#     total+=sum
# print(total)

# variable1 = 10
# variable2 = 20

# print("variable1:", variable1)
# print("variable2:", variable2)

# variable1, variable2 = variable2, variable1

# print("variable1:", variable1)

# print("variable2:", variable2)

# print("variable2:", variable2)

# my_list = [8 , 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)



# my_list = [1, 2, 3, 4, 5]#[8, 10, 6, 2, 4]
# print(my_list) 
# count = 0
# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):
#         count += 1
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i] 
# print(my_list)
# print(count)
        


# my_list = [1, 2, 3, 4, 5]#[8, 10, 6, 2, 4]
# count = 0
# swapped = True
# count = 0
# while swapped:
#       swapped = False
#       for i in range(len(my_list) - 1):
#           count += 1
#           if my_list[i] > my_list[i + 1]:
#               swapped = True
#               my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print(my_list)
# print(count)

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
# print(list_1)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1] 
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[-1:1]
# new_list = my_list[-5:3]
# new_list = my_list[:3]
# print(new_list)
# new_list = my_list[2:]
# print(new_list)
# del my_list[1:3]

# print(my_list)

# del my_list[:]
# print(my_list)

# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)
# print(5 not in my_list)
# print(12 in my_list)


# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# to_find = 5
# found = False
# for i in range(len(my_list)):
#     if my_list[i] == to_find:
#         found = True
#         print("Element found at index:", i)
#         break
#     if found: 
#            print("Element found at index", i)
#     else:  
#            print("absent")    

# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")

# row =["WHITE_PAWN" for i in range(8)]

# print(row)

# row = []
# for i in range(8):
#      row.append("WHITE_PAWN")

# row =["WHITE_PAWN" for i in range(8)]
# squares = [x ** 2 for x in range(1, 11)]
# twos = [2 ** x for x in range(8)]
# print(row)
# print(squares)
# print(twos)
        
# board = []
# for i in range(8):
#      row = ["EMPTY" for i in range(8)]  
#      board.append(row)

# print(board)

     
# board[0][0]="ROOK"
# board[0][7]="ROOK"
# board[7][0]="ROOK"
# board[7][7]="ROOK"

# print("------------")

# for element in board:
#     print(element)

#     board[0][1] = "HORSE"
#     board[0][6] = "HORSE"
#     board[7][1] = "HORSE"
#     board[7][6] = "HORSE"

# print("------------")
# for element in board:
#     print(element)

# temps = [[0.0 for h in range(24)] for d in range(31)]

# temp1 = 19
# temp2 = 32
# count = 0
# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2
#         count = 0

# for element in temps:
#     print(element)

# total = 0.0
# for days in temps:
#     total += days[11]
# average = total / 31
# print("Average temperature at noon:", average)

# highest = -100.0
# for days in temps:
#     for temp in days:
#         if temp > highest:
#             highest = temp
# print("The highest temperature was:", highest)

# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days, "days were hot days in the month.")

# rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# print(rooms)

# rooms[1][9][13] = True

# rooms[1][9][1] = True

# vacancy = 0
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1
# print(vacancy, "vacancies in the third floor and 15th floor of 3rd Building.")

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# var = 1
# while var < 10:
#     print("#")
#     var = var << 

# z = 10
# y = 0
# x = y < z and z > y or y > z and z > y
# print(x)    

# a = 1
# b = 0 
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)
 
# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# def scope_test():
#     x =123
# scope_test()
# print(x)

# def my_function():
#     print("Do I Know that variable?",var)

# var =1
# my_function()
# print(var)

# def mult(x): 
#    var = 7
#    return x * var 
# var = 3 
# print(mult(7))

# def my_function():
#     global var
#     var = 2
#     print("Do I Know that variable?",var)


# var = 1
# my_function()
# print(var)

# var = 2
# print(var)

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var())
# print(var)

# def my_function(n): 
#    print("I got", n)
#    n += 1 
#    print("I have", n)
   
# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#         print("Print #1:", my_list_1)
#         print("Print #2:", my_list_2)
#         my_list_1 = [0, 1] 
#         print("Print #3:", my_list_1) 
#         print("Print #4:", my_list_2) 
        
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def my_function(my_list_1):
#         print("Print #1:", my_list_1)
#         print("Print #2:", my_list_2) 
#         del my_list_1[0] # Pay attention to this line.
#         print("Print #3:", my_list_1)
#         print("Print #4:", my_list_2)
        
# my_list_2 = [2, 3] 
# my_function(my_list_2) 
# print("Print #5:", my_list_2)


# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)

# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)
      
# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2, 4, 6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type(tup)) 

var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3,var)

# t1, t2, t3 = t2, t3, t1

# print(t1)
# print(t2)
# print(t3)
# print(type(t1))
# print(type(t2))
# print(type(t3)) 

# dictionary = {
# "cat": "chat", 
# "dog": "chien", 
# "horse": "cheval"
#    }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary["cat"])
# print(phone_numbers["Suzy"])
# print(phone_numbers['president'])
  

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse  ']
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print("----", word, "is not in the dictionary", "----")

#         print(dictionary.keys())

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# pol_eng_dictionry = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# print("pol_eng_dictionry:", pol_eng_dictionry)
# copy_dictionary = pol_eng_dictionry.copy()

# print("copy_dictionary:", copy_dictionary)

# pol_eng_dictionry["zamek"] = "lock"
# item = pol_eng_dictionry["zamek"]
# print(item)
 

# phonebook = {} 
# print(phonebook)
# phonebook["Adam"] = 345678958
# print(phonebook)

# del phonebook["Adam"]
# print(phonebook)

# pol_eng_dictionry = {"kwiat": "flower"}

# pol_eng_dictionry.update(
#     {
#         "gleba": "soil"
#     })
# print(pol_eng_dictionry)

# pol_eng_dictionry.popitem()
# print(pol_eng_dictionry)

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item) 

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# if "zamek" in pol_eng_dictionary:
#     print("Yes!'zamek' is in the dictionary.")
# else:
#     print("No!'zamek' is not in the dictionary.")


# students = {}

# while True:
#     name = input("Enter student name")
#     if name == " ":
#         break   
#     grade = input("Enter student grade")
#     students[name] = grade
#     print(students)
# score = input("Enter student name to get grade")
# if score in students:
#     print(score, "->", students[score])
# else:
#     print("Student not found.")

# students = {}

# while True:
#     name = input("Enter student name: ")
#     if name == " ":
#         break   
#     score = int(input(f"Enter {name}'s score: "))
#     if score not in range(1,11):
#         break
#     if name in students:
#         students[name] += (score, )
#     else:
#         students[name] = (score, )
        
#         for mark in students:
#             print(mark, "->", students[mark])
#             input("Enter student name to get score: ")
#             name = input("Enter student name: ")
#             if name in students:
#                 print(name, "->", students[name])
#             else:
#                 print("Student not found.")


# students = {}

# while True:
#     name = input("Enter student name: ")
#     if name == "":
#         break   
#     score = int(input(f"Enter {name}'s score:"))
#     if score not in range(1,11):
#         break
#     if name in students:
#         students[name] += (score, )
#     else:
#         students[name] = (score, )


# print(students)
# for name, marks in students.items():
#     sum = 0
#     for mark in marks:
#         sum += mark
#         print(name, "->", sum / len(marks))


# class ThisIsMyFirstClass:
#     name = "Rishuu"
#     age = 21

#     def getName(self):
#        print(self.name)
       

# first_object = ThisIsMyFirstClass()
# print(first_object)

# # first_object.getName()
# # print(first_object.name)

# class Student:
#     def __init__(self, name, age, grades, gender):
#         self.name = name
#         self.age = age
#         self.grades = grades
#         self.gender = gender

  
#     def printDetails(self):
#         print("name:", self.name)
#         print("age:", self.age)
#         print("grades:", self.grades)
#         print("gender:", self.gender)
    
        

# rishuu = Student("Rishuu", 21, "A", "Male")
# print(rishuu)

# # rishuu.name = "Rishuu"
# # rishuu.age = 21 
# # rishuu.grades = "A"
# # rishuu.gender = "Male"

# rishuu.printDetails()  

# # print(rishuu.name)
# # print(rishuu.age)
# # print(rishuu.grades)
# # # print(rishuu.gender)
    

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

'''use super class and super method '''
class super:
    def __init__(self,name):
        self.name = name
    def __str__(self): #end user also use repr method but str is for internal use 
        return "my name is " +self.name+"."
class Sub(super):
    def __init__(self,name):
        super.__init__(self,name)

obj = Sub("Andy")
print(obj)
print(obj.__dict__)#also custamise the dict format #use for explaining 
    
'''multiple inheritance'''

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):
#     pass

# obj = Sub()

# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# '''multilevel inheritance'''
# # in python it checks from bottom-to-top
# class Level1: 
#     var = 100
#     def fun(self):
#         return 101
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
    
# class Level3(Level2):
#    pass
   
    # var = 303
    # def fun(self):
    #     return 333
    

# obj = Level3()
# print(obj.var,obj.fun())


#here about on same level left right
'''multiple inheritance'''

# class Left:
#     var = "L"
#     var_left="LL"
#     def fun(self):
#         return "left"
# class Right:
#     var= "R"
#     var_right="RR"
#     def fun(self):
#         return "right"
# class Sub(Right,Left): #(left,right)
#     pass

# obj = Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())

# MRO method resolution order precidence and order both in multilevel and multiple inheritance

'''polymorphism one name many forms'''

# class One: 
#     def do_it(self):
#         print("do it from one")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it  from Two")

#  class Three(Two):
#        super.do_it(self):
#        print():  #try with super

# one = One()
# two = Two()
# one.doanything()
# two.doanything()   


# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#         return n
#     else:
#         print("evenrything is fine")
#         return
# print("-----------------")
# print("reciprocal(2)",reciprocal(2))

# print("-----------------")
# print("reciprocal(0)",reciprocal(0))
# print("-----------------")

'''finally'''

# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#         return n
#     else:
#         print("evenrything is fine")
#         return
#     finally:
#         print("its time to exit")
#         return n


# print("-----------------")
# print("reciprocal(2)",reciprocal(2))

# print("-----------------")
# print("reciprocal(0)",reciprocal(0))
# print("-----------------")




# try:
#     i = int("hello")
# except Exception as e:

#     print(e)
#     print(e.__str__())



'''create ur own exception/using base_keyword'''

# class MyZeroDivisionError(ZeroDivisionError):
#     pass
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("SOME WORSE NEWS")#raise is use to rise an error
#     else:
#         raise ZeroDivisionError("some bad news")

# do_the_division(False)
# do_the_division(True)

'''CLASS CONTAINS  parameter method constructor
obj = Theclass() ()-> the contructor for creating the obj
implicit automatically receivie
self is kis obj pr work ho rha h self obj

'''

'''class varible /static variable wrk with class not with obj'''
# class ExampleClass:
#     counter = 0
#     def __init__(self,val =1):
#         self.__first = val
#         ExampleClass.counter +=1  #class name with counter {static variable ****} 

# example_object_1  = ExampleClass()
# example_object_2  = ExampleClass(2)
# example_object_3  = ExampleClass(4)


# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)


'''we can put any logic inside our __init__ constructor rather then always intanciation'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
        
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# print(example_obj.a)
# print(example_obj.b)

'''exception handling try except'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1  #try with method
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# #nested exection try catch 
# try: 
#     print("a=",example_obj.a)
# except AttributeError:
#     try:
#         print("b=",example_obj.b)
#     except AttributeError:
#        print("Error has occurs!slightly pass it") 

'''hasattr function(2 argumetn to be pas clsname,key/prop) ** checking the property exist inside the obj or not the result in form of true fales'''

# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)

# if hasattr(example_obj,'a'):
#     print("a=",example_obj.a)
# if hasattr(example_obj,'b'):
#     print("b=",example_obj.b)


'''passing class'''
# class ExampleCls:
#     counter = 0
#     def __init__(self,val=1):
#         #self.__first = val
#         ExampleCls.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1  #get an error for no attribute inside b 
# example_obj = ExampleCls(1)
# print(example_obj.a)
# print(example_obj.b)


# if hasattr(example_obj,'a'):
#     print("a=",example_obj.a)
# if hasattr(example_obj,'b'):
#     print("b=",example_obj.b)

# print(hasattr(ExampleCls,'b'))
# print(hasattr(ExampleCls,'a'))
'''__name for make is hidden'''

# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myobj.population",myObj.population)

# print("myobj.victims",myObj.victims)
# print("myobj.length_fr",myObj.length_ft)
# # print("myobj.__venomous",myObj.__venomous)
# print("myobj.venomous",myObj.venomous)

'''now accesing the hidden variable __name by using class name '''
# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False
# myObj = Python()

# print("myobj.population",myObj.population)
# print("myobj.victims",myObj.victims)
# print("myobj.length_fr",myObj.length_ft)
# # print("myobj.__venomous",myObj.__venomous)
# print("myobj.venomous",myObj._python.__venomous)

# class Python:
#     population = 1
#     victims = 0
#     version_2 =2
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False

# myObj = Python()
# print("myobj.population",myObj.population)
# print(hasattr(myObj.version_2))#***
# print("myobj.victims",myObj.victims)

'''abstraction'''
'''hidden method is also possible (hidden is abstraction)'''
'''name mangling in methods (accsesing hidden prop)'''
# class Classy:
#   def visible(self):
#     print("visible")

#   def __hidden(SELF):
#     print("hidden")

# obj =Classy()
# obj.visible()
# try:
#    obj.__hidden()
# except:
#   print("failed")
# obj._Classy__hidden()

# obj = Classy()
# print(type(obj))
# '''use to print the main class name'''
# print(type(obj).__name__)

'''is instance check whether the obj is blongs to the class or not'''
# class vehicle:
#     pass
# class LandVehicle(vehicle):
#     pass
# class trackedVechile(LandVehicle):
#     pass
# my_vehicle = vehicle()
# my_land_vehicle = LandVehicle()
# my_track_vehicle = trackedVechile()

# for obj in [my_vehicle,my_land_vehicle,my_track_vehicle]:
#     for cls in [vehicle,LandVehicle,trackedVechile]:
#         print(isinstance(obj,cls),end="\t") #*** check it belongs to the same clss the obj
#     print()

'''reference check using is'''

# class SampelClass:
#     def __init__(self,val):
#         self.val =val

# object_1 = SampelClass(0)
# object_2 = SampelClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1 = "Mary had a little "
# string_2 ="Mary had a little lamb"
# string_1 += "lamb"

# print(string_1 == string_2 , string_1 is string_2)

# city = "Indore"
# print(city[0])
# print(city[1])

# print(city[-1])
# print(city[-5])

# print(city[-3])
# print(city[3])

'''slicing'''

# name = "Rishu"
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])


# print(len(city))
# print(len(name))      

'''string methods'''

# text = "   Hello python world!   "
# # Case

# print(text.upper())
# print(text.lower())
# print(text.title()) 
# print(text.capitalize())

# # Strip Whitespace
# print(text.strip())

# # Search 
# print('python' in text)
# print(text.find('python'))
# print(text.count('l'))

# '''split and join'''

# csv = "Rishu,22,Indore,Engineer"
# parts = csv.split(",")
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# # Check content
# print('hello'.isalpha())
# print('12345'.isdigit())
# print('python'.isalpha())
# print(' '.isspace())

# #start/end check
# email ='student@example.com'
# print(email.startswith('student'))
# print(email.endswith('.com'))

'''special strings at , 62'''

# name, marks, rank = 'Rishu', 92.567, 3

# # Basic
# print(f'Marks: {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'Count: {1000000:,}')

# #padding padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank{rank}')
# #Rishu         |   92.57|Rank3

# #expression inside {}
# price, gst = 500, 0.18
# print(f'Total price: {price * (1 + gst):.2f}')

# string = "Hello, How are you doing today?"
# count = 0
# for char in string:
#     if char in "aeiouAEIOU":
#         count += 1
# print("vowel count:", count)
# print(string[15:19])
# print(string[::-1])
# non_palin = string != string[::-1]
# print("Is the string a palindrome?", not non_palin)

# with open("Data.txt", "r") as file:
#     data = file.read()
# print(data)
 
'''reading and writing  and updating files'''
# with open("students.txt", "w") as file:
#     file.write("Rishuu, 92.5, Indore, Engineer\n")
#     file.write("Raghav, 88.0, Mumbai, Designer\n")
#     file.write("Monish, 95.0, Delhi, Developer\n")

# with open("students.txt", "a") as file:
#     file.write("Isha, 90.0, Bangalore, Analyst\n")

#     with open("students.txt", "r") as file:
#         data = file.read()
# print(data)

# with open("students.txt", "r") as file:
#             for line in file:
#                 name, score, city, profession = line.strip().split(", ")
#                 print(f"Name: {name}, Score: {score}, City: {city}, Profession: {profession}")
#                 print(f"{name} lives in {city} and works as a {profession}.")
#                 print("-----------------------------")


