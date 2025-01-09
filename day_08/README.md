# Day 8 - Function Parameters & Caesar Cipher

## Concepts
- Functions with Inputs
- Positional vs. Keyword Arguments

## Project: Caesar Cipher

### 1. Encode

**TODO-1**: Create a function called `encrypt` that takes the `'text'` and `'shift'` as inputs.

**TODO-2**: Inside the `encrypt` function, shift each letter of the `'text'` forwards in the alphabet by the shift amount and print the encrypted text. 
e.g.
```py
    plain_text = "hello"
    shift = 5
    print output: "The encoded text is mjqqt" 
```

**HINT**: How do you get the index of an item in a list: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

🐛Bug alert: What happens if you try to encode the word `civilization`?🐛

**TODO-3**: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

### 2. Decode

**TODO-1**: Create a different function called `decrypt` that takes the `'text'` and `'shift'` as inputs.

**TODO-2**: Inside the `decrypt` function, shift each letter of the `'text'` *backwards* in the alphabet by the shift amount and print the decrypted text.  
e.g.
```py 
  cipher_text = "mjqqt"
  shift = 5
  plain_text = "hello"
  print output: "The decoded text is hello"
```

**TODO-3**: 
- Combine `encrypt()` and `decrypt()` functions into a single function called `caesar()`.
- Use the value of the user chosen `'direction'` variable to determine which functionality to use.
- Call the `caesar()` function instead of `encrypt/decrypt` and pass in all three variables - `'direction'`/`'text'`/`'shift'`.

### 3. Reorganising our Code

**TODO-1**: Import and print the logo from art.py when the program starts.

**TODO-2**: What happens if the user enters a number/symbol/space that's not in the list alphabet?

Can you the code to keep the number/symbol/space when the text is encoded/decoded?
e.g.
```py 
  original_text = "meet me at 3!"
  cipher_text = "XXXX XX XX 3!"
```

**TODO-3**: 
Can you figure out a way to restart the cipher program?

e.g.

Type `yes` if you want to go again. Otherwise, type `no`.

If they type 'yes' then ask them for direction/text/shift again and call the `caesar()` function again.

### 4. Demo

[demo](https://appbrewery.github.io/python-day8-demo/)
