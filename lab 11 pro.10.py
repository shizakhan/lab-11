print('shiza khan','18B-130-CS')
print('lab 11','program 10')
print('\n')
#write a program that will operate on phonebook1 and phonebook3
#for union,intersection,difference and symmetric difference
phonebook1 = {'123-45-67','234-56-78','345-67-89','123-45-67','345-67-89'}
phonebook3 = {'345-67-89','456-78-90'}
print('phonebook1 is:',phonebook1)
print('phonebook3 is:',phonebook3)
print('the union of phonebook1 and phonebook3:',phonebook1 | phonebook3 )
print('the union of phonebook3 and phonebook1:',phonebook3 | phonebook1 )
print('the intersection of phonebook1 and phonebook3:',
      phonebook1 & phonebook3)
print('the intersection of phonebook3 and phonebook1:',
      phonebook3 & phonebook1)
print('the difference between phonebook1 and phonebook3:',
      phonebook1 - phonebook3)
print('the difference between phonebook3 and phonebook1:',
      phonebook3 - phonebook1)
print('the symmetric difference between phonebook1 and phonebook3:',
      phonebook1 ^ phonebook3)
print('the symmetric difference between phonebook3 and phonebook1:',
      phonebook3 ^ phonebook1)
