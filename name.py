#Liliana Cantero
def encode(password):
  pwEncoded = ""                      # empty string to store new pw

  for i in password:                  # iterates through each digit in password
    newNum = int(i) + 3               # adds 3 to each digit  
    if newNum == 10:
      newNum = 0                      # accounting for double digits (10, 11, 12)
    elif newNum == 11:
      newNum = 1
    elif newNum == 12:
      newNum = 2
    pwEncoded += str(newNum)          # adding each new digit to pwEncoded

  return pwEncoded

if __name__ == "__main__":

  print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
  option = int(input('Please enter an option: '))      # user input
  while option != 3:
    if option == 1: # encode password
      password = input("Please enter your password to encode: ")
      encodedPW = encode(password)
      print('Your password has been encoded and stored!')
    if option == 2:
      pass
    if option == 3: #quit
      break