
dict = {
  "one": "Uno",
  "two": "Dos",
  "three": "Tres",
  "four": "cuatro",
  "five": "cinco",
  "Hello": "Hola",
  "Bye": "Adios",
  "Yan": "Chico",
  "skinny": "Flaco",
  "million": "milliones",
  "ugly": "feo",
  "I": "Yo",
  "am": "soy"
}

def my_join(words):
  print(words)
  attach = ''
  for word in words:
    attach += ' ' + word
    
  print(attach.strip() + '!')

my_join(["I", "am", "really", "ugly"])


word = "   hello world!     "
print(word.strip())

  
# def eng2spanish(text):
#   words = text.split(' ')
#   print(words)

#   spanish_words = []
#   try:
#     for word in words:
#       ret = dict[word] 
#       spanish_words.append(ret)
    
#   except:
#     print("Unrecognized word!")

#   print(spanish_words)
#   print(' '.join(spanish_words) + '!')

# eng2spanish("I am ugly")




# board = [1,2,3,4,5,6,7,8,9]

# print(board[1])

# car = {
#   "brand": "Totyota",
#   "model": "Camry",
#   "color": "white",
#   "type": "gas"
# }

# print(f'My car is a { car["brand"] }')

# print(f'My car is a {car["brand"]} {car["model"]} with {car["color"]} color. An it\'s a {car["type"]} car')


# print("I'm a student")
# print('I\'m a student')
# print("special characters like ,#\\'?")