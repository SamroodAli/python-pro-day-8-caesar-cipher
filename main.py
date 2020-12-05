import art
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# cipher function
def cipher(text,shift,direction):
        output=''
        # if decode => shift = -shift
        if direction=='decode':
                    shift *= -1
        for letter in text:
            if letter in alphabet:
                index_letter = alphabet.index(letter)
                shift_index = index_letter + shift #here shift is negative if decoding
                if shift_index < 0 or shift_index > 26:
                    remainder_index= shift_index % 26
                    output += alphabet[remainder_index]
                else:
                    output += alphabet[shift_index]
            else:
                    output += letter
        print(f"the {direction}d text is {output} ")
        return output


#start ciphering
playing=True
encodedTextHistory =[]
decodedTextHistory =[]

while playing:
    clear()
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or view to view history:\n").lower()

    if direction !='view':    
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        output=cipher(text,shift,direction)
        save = input(f'Do you want to save the {direction}d text ?\n press yes or y to save\n')

        if save =='y' or save == 'yes':
            if direction =='encode':

                encodedTextHistory.append(output)
            else:
                decodedTextHistory.append(output)

    else:
        direction_of_history = input('Which history do you need to see ? \n encoded or decoded\n type e for encoded  or d for decoded\n')
        if direction_of_history =='e':
            for text in encodedTextHistory:
                print(text)
        else:
            for text in decodedTextHistory:
                print(text)
    
    playing_again= input('Press any key to quit, type y or yes to continue again. \n').lower()
    if playing_again =='yes' or playing_again =='y':
        playing = True
    else:
        playing = False