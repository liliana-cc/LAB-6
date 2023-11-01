#Liliana Cantero
def encode(password):
  pwEncoded = ""

  for i in password:
    newNum = int(i) + 3
    if newNum == 10:
      newNum = 0
    elif newNum == 11:
      newNum = 1
    elif newNum == 12:
      newNum = 2
    pwEncoded += str(newNum)

  return pwEncoded

if __name__ == "__main__":

  print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
  option = int(input('Please enter an option: '))
  while option != 3:
    if option == 1:
      password = input("Please enter your password to encode: ")
      encodedPW = encode(password)
      print('Your password has been encoded and stored!')
    if option == 2:
      pass
    if option == 3:
      break