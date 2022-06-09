from email import message
from unittest import result


MORSE_DICT = {  'A':'.-', 'B':'-...',
				'C':'-.-.', 'D':'-..', 'E':'.',
				'F':'..-.', 'G':'--.', 'H':'....',
				'I':'..', 'J':'.---', 'K':'-.-',
				'L':'.-..', 'M':'--', 'N':'-.',
				'O':'---', 'P':'.--.', 'Q':'--.-',
				'R':'.-.', 'S':'...', 'T':'-',
				'U':'..-', 'V':'...-', 'W':'.--',
				'X':'-..-', 'Y':'-.--', 'Z':'--..',
				'1':'.----', '2':'..---', '3':'...--',
				'4':'....-', '5':'.....', '6':'-....',
				'7':'--...', '8':'---..', '9':'----.',
				'0':'-----', ', ':'--..--', '.':'.-.-.-',
				'?':'..--..', '/':'-..-.', '-':'-....-',
				'(':'-.--.', ')':'-.--.-'}


#converting sentence into morse
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # if space present 
            cipher += MORSE_DICT[letter] + ' '
        else :
            cipher += ' '
    return cipher

def decrypt(message):
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i +=1
            if i==2:
                decipher += ' '
            else:
                decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                citext =''
    return decipher

def main():
    print("Enter\n 1 for encryption \n2 for decryption")
    choice = input()
    if choice == "1":
        print("Enter the message to encrypt : ")
        message = input()
        result = encrypt(message.upper())
        print(result)
    elif choice == "2":
        print("Enter morse code to decrypt : ")
        message = input()
        result = decrypt(message)
        print(result)
    else:
        print("Wrong input")

if __name__ == '__main__':
	main()