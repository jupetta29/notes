import caesar_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ''
  if cipher_direction == 'decode':
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount) % 26
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f'Here\'s the {cipher_direction}d result: {end_text}')


continue_caesar = True

print(caesar_cipher_art.logo)

while continue_caesar:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  should_continue = input('\nWould you like to restart the cipher program? Type "yes" or "no"\n').lower()
  
  if should_continue == 'no':
    continue_caesar = False
    print('Goodbye!')