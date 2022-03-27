text = input("Enter a text:")
key = int(input("Enter key:"))
encrypted = " "
for letter in text:
    encrypted += chr(ord(letter)+key)
    
print(encrypted)
