print('shiza khan','18B-130-CS')
print('lab 11','program 06')
print('\n')
#write a program which add some new values inside a set,using add method
my_topstudents = {'Bassam','Usman','Rafeh','Ahad','Wadood','Yusra','Asma'}
print('my top scoring students in programming fundamentals are:',my_topstudents)
print('oh, i guess i miss one student, let me add his name too')
print('previously i have added :' + str(len(my_topstudents)) + 'students in my list')
my_topstudents.add('khurrum khalil')
my_topstudents.add('khurrum khan')
print('thanks,i have remember him')
print('now my top scoring students name are:',my_topstudents)
print('now after adding i have:' + str(len(my_topstudents)) + 'students in my list')
print('oh, i guess i have added one student with similar name, let me remove his name')
my_topstudents.remove('khurrum khalil')
print('now my top scoring students name after removing extra name are:',my_topstudents)
print('now after removing i have:' + str(len(my_topstudents)) + 'students in my list')

