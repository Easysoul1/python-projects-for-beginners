# Pratice Exercises
# Question 1 Week 5

# Implementing a contact book
contact_book = {
       "contact1":{
              "name": "Adejumo Ezekiel Adedayo",
              "school" : "University Of Ibadan",
              'hobbies' : 'Programming'
       },
       "contact2": {
              "name": "Adejumo Adedayo",
              "school" : "UI",
              'hobbies' : 'Coding'
       },
       'contact3' : {
              "name": " Ezekiel Adedayo",
              "school" : "University Of Ibadan",
              'hobbies' : 'Solving Problem'
       }
}
print(contact_book.get('contact2', {}).get('name'))
print(f'My name is {contact_book["contact1"]["name"]}, I am a student at {contact_book["contact3"]["school"]}. I love {contact_book["contact1"]["hobbies"]}')

# Question 2
# Highest score checker and Name sorter
scores = {
       "John": 90,
       "Jane": 95,
       "Adedayo": 100,
       "Bodmas": 97,
       "Femi": 70,
       "Tolu": 60,
       "Fola": 50,
       "Tola": 45,
       "Adejumo": 75,
       "Timothy": 95,
       "Damilola": 65,
       "Bola": 55,
       "Caleb": 98,
       "Segun": 78
}
highest_score = max(scores.values())
names_sort = sorted(scores.keys())
print(f'The highest score is {highest_score}')
print(f'The names of the student in alphabetical  are {names_sort}')