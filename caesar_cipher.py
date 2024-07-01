letters = "abcdefghijklmnopqrstuvwxyz"
numletters = len(letters)
def encryption(plaintext, key):
   ciphertext = ''
   for letter in plaintext:
       letter = letter.lower()
       if not letter ==' ':
           index = letters.find(letter)
           if index == -1:
               ciphertext += letter
           else:
               newindex = index + key
               if newindex >= numletters:
                   newindex -= numletters
               ciphertext +=letters[newindex]
   return ciphertext

def decryption(ciphertext, key):
   plaintext = ''
   for letter in ciphertext:
       letter = letter.lower()
       if not letter ==' ':
           index = letters.find(letter)
           if index == -1:
               plaintext += letter
           else:
               newindex = index - key
               if newindex < 0:
                   newindex += numletters
               plaintext +=letters[newindex]
   return plaintext

print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

print("Do you want to encrypt or decrypt?")
userinput = input("e/d: ").lower()
print()

if userinput == 'e':
    print("ENCRYPTION SELECTED")
    print()
    key = int(input("Enter the key from 1-26: "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encryption(text, key)
    print(f"CIPHER TEXT: {ciphertext}")

elif userinput == 'd':
    print("DECRYPTION SELECTED")
    print()
    key = int(input("Enter the key from 1-26: "))
    text = input("Enter the text to decrypt: ")
    plaintext = decryption(text, key)
    print(f"ORIGINAL TEXT: {plaintext}")

