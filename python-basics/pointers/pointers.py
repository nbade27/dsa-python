num1 = 11
num2 = num1

print('Before num1 and num2 values are updated:')
print('num1=',num1)
print('num2=',num2)

print('num1 points to:',id(num1))
print('num2 points to:',id(num2))

num2 = 22

print('After num1 and num2 values are updated:')
print('\nnum1=',num1)
print('num2=',num2)

print('\nnum1 points to:',id(num1))
print('num2 points to:',id(num2))


# Let us check same with dict 

dict1 = {
    'value':11
    }
dict2 = dict1

print("Before value is updated:")
print("\ndict1 = ",dict1)
print("dict2 = ",dict2)

print('\ndict1 points to ',id(dict1))
print('dict2 points to ',id(dict2))

dict2['value'] = 22

print('After dict1 and dict2 are updated')

print("\ndict1 = ",dict1)
print("dict2 = ",dict2)

print('\ndict1 points to ',id(dict1))
print('dict2 points to ',id(dict2))

# In dict after updating the values both are pointing to same address
# but in int values both are pointing to different addresses
# because int is immutable in python
