from alphabet import alphabet

def ceasar(direction, text, shift):
  coded_word = ""

  shift = shift % 26
  if direction == "decode":
    shift *= -1
    
  for char in text:    
    if char in alphabet:
      encrypt_index = alphabet.index(char) + shift

      if encrypt_index > 25:
        encrypt_index = encrypt_index - 25
      elif encrypt_index < 0:
        encrypt_index = encrypt_index + 25
        
      coded_word += alphabet[encrypt_index]

    else:
      coded_word += char
  
  print(f"The {direction}d text is {coded_word}")