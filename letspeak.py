# configuration
user_input = input('Type a word: ')
user_input = user_input.upper()
alphabet = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
num = [4, 3, 6, 1, 0, 5, 7]

# process
for i in user_input:
  if i in alphabet:
      print (num[alphabet.index(i)])
  else:
        print(i)
