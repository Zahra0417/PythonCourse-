text = input("Enter a text:")
encrypted = " "
for letter in text:
    encrypted += chr(ord(letter)+3)
    
print(encrypted)
