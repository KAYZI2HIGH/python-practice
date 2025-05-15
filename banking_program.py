total_balance = 0
is_running = True

def show_balance():
  print(f"Your current balance is ${total_balance: .2f}")

def deposit():
  global total_balance
  amount = int(input('Enter the amount to deposit: '))
  total_balance += amount
  print(f"Your balance is now ${total_balance: .2f}")

def withrawal():
  global total_balance
  amount = int(input('Enter an amount to withraw: '))
  total_balance -= amount
  print(f"Your balance is now ${total_balance: .2f}")

def exit():
  global is_running
  print('Thank you for banking with us!')
  is_running = False

bank_operations = [
  {
  'option': '1',
  'value': 'Show Balance',
},
  {
  'option': '2',
  'value': 'Deposit',
},
  {
  'option': '3',
  'value': 'Withdraw',
},
  {
  'option': '4',
  'value': 'Exit',
},
]



def startProgram():
  print("***********************")
  print('    Banking Program    ')
  print("***********************")

  for operations in bank_operations:
    for key, value in operations.items():
      print(value, end='. ')
    print()

  print("***********************")
  
  selected_operation = input('Enter your choice (1-4): ')

  return selected_operation



while is_running:
  selected_operation = startProgram()

  match selected_operation:
    case '1':
      show_balance()
    case '2':
      deposit()
    case '3':
      withrawal()
    case '4':
      exit()