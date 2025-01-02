# Pratice Exercises
# Question 1 Week 7
# Squared root number 
def number(s):
       print([x**2 for x in s])
number_squared = [1,2,3,4,5,6]
number(number_squared)

# Question 3
#List sort using lambda fuction
list_of_dict = [
       {
              "name":"Adejumo",
              "age":50
       },
       {
              "name":"Ezekiel",
              "age": 22
       },
       {
              "name":"Adedayo",
              "age": 23
       },
       {
              "name":"Bodmas",
              "age": 32
       }
]
sort_list = sorted(list_of_dict, key=lambda x: x["age"])
print(sort_list)


