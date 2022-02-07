8

# fruits = ['apples','oranges','bananas','peaches','grades']8
# print(fruits)
# # def addFruit(self,fruit):
# #     self.fruit= fruit
# for fruit in fruits:
#     print(fruit)

# #dictionary 
# studentsRecord={"student1":"patrick clark","student2":"Alphonse kip","student3":"Charles Ngugi"}
# print(type(studentsRecord))
# for student in studentsRecord:
#     print(student ,"is called",studentsRecord[student])

# def solution(N):
#     return " {1:b}".format(int(N))

def solution(N):
    return "{0:b}".format(int(N))
if __name__=='__main__':
    print("Enter number:")
    number=int(input())
    print("The binary of input is:",solution(number))
    # converting into a list of strings
    list1 = list(solution(number))
    print(list1)
    #typecasting the individual elements of the string into integer using the map () method
    list2=list(map(int,list1))
    print("list of integers:",list2)
  
 