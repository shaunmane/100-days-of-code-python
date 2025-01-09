import art 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
print(art.logo)

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "yes":
        main()
    elif restart == "no":
        print("Goodbye")

def caesar(cipher_direction, start_text, shift_amount):
    
    output_text = ""
    
    if cipher_direction == "decode":
        shift_amount *= -1  

    for i in start_text:
        if i == " " or not i.isalpha():  
            output_text += i 
        else:
            shifted = alphabet.index(i) + shift_amount
            shifted = shifted % len(alphabet)  
            output_text += alphabet[shifted]

    print(f"Here is the {cipher_direction}d result: {output_text}")


main()