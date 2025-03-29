weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'k':
  print(f'Your weight is {int(weight)/ 0.454} Pounds')
elif unit.lower() == 'l':
  print(f'Your weight is {int(weight) * 0.454} Kilogram')
else:
  print('Please provide a valid unit.')