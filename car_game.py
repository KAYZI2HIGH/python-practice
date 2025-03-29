while 1<3:
  command = input('> ')
  if command.lower() == 'help':
    print('''
start - to start the car
stop - to stop the car
quit - to exit
      ''')
  elif command.lower() == 'start':
    print('Car started... Ready to go!')
  elif command.lower() == 'stop':
    print('Car stopped.')
  elif command.lower() == 'quit':
    break
  else:
    print("I don't understand that command")