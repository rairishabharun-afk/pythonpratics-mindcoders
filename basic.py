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

pol_eng_dictionry = {"kwiat": "flower"}

pol_eng_dictionry.update(
    {
        "gleba": "soil"
    })
print(pol_eng_dictionry)

pol_eng_dictionry.popitem()
print(pol_eng_dictionry)