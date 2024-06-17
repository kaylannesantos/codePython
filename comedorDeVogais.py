"""
teste1
message = input('Digite uma palavra: ')

while message != 'chupacabra':
    message = input('Digite uma palavra: ')
print("'You've successfully left the loop.")

teste2
while True:
    keyword = input('Digite uma palavra: ')

    if keyword == 'chupacabra':
        print("'You've successfully left the loop.")
        break
"""

consoantes = ""
stringInput = input('Digite uma palavra: ')
user_word = stringInput.upper()

for letter in user_word: 
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue 
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else: 
        consoantes += letter
print(consoantes)