"""
ex 1:

dishes = ['idli', 'biryani', 'pizza', 'pasta']

food = input('Enter a dish')
for food in dishes:
    if food =='idli' or 'biryani':
        print('Indian')
        break
    else:
        print('Italian')
        break
        
        """

#ex 2:
"""
expense = [500,600,799,1990]
total = 0 
for i in range(len(expense)):
    print(f'Month {i+1} and expense is {expense[i]}')
    total+=expense[i]
print(f'Total expense is {total}')

"""
"""
#ex 3:
keylocation = 'kitchen'
locations = ['bedroom', 'kitchen', 'hall', 'bathroom']
for i in locations:
    if i == keylocation:
        print('Key found in', i)
        break
    else:
        print('Key not found')
        
    """

#ex 4:

"""
for i in range(1,6, 2):
    print(i**2)

    also: for i in range(1,6):
    if i % 2 = 0:
       continue
    else:
        print(i**2)

    """