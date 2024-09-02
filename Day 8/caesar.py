alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter

        else:   
            shifted_position = alphabet.index(letter) + shift_amount 
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position] 
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
    if direction != "encode" and direction != "decode":
       direction = input("You typed wrong input. Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower() 

    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    #if shift != int():
        #shift = int(input("You did not type number. Please type the shift number: \n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    go_again = input("Type 'Yes' if you want to go again. Otherwise, type 'No'.\n ").lower()
    if go_again != "yes" and go_again != "no":
       go_again = input("You typed wrong input. Type 'yes' to continue or 'no' to finish.\n").lower()
    elif go_again == "no":
        should_continue = False
        print("Good Bye!")
    else:
        continue

#else:
#   direction = input(print("You typed wrong input. Type 'encode' to encrypt, type 'decode' to decrypt.\n")).lower()

