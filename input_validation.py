username = input('Enter your username: ')

no_of_spaces = username.count(' ')
is_alphabet = username.isalpha()

if(len(username) > 12):
  print('Username must not exceed 12 characters')
elif(username.count(" ") != 0):
  print('Username can not contain a space')
elif(not is_alphabet):
  print('Username cannot include a digit')
else:
  print("username Accepeted")

credit_card = '1234-532-563426-23432'

credit_card= credit_card[::-1]

print(credit_card)