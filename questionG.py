'''
Takes a string of characters as input, and plots their letter frequency.
No greater than 250 chars
Author : Gina

'''

def chart_letters(letters_string):
    letters_dict = {"A": 0, "B": 0,"C" : 0, "D": 0, "E": 0,"F" : 0,
                    "G": 0, "H": 0,"I" : 0, "J": 0, "K": 0,"L" : 0,
                    "M": 0, "N": 0,"O" : 0, "P": 0, "Q": 0,"R" : 0,
                    "S": 0, "T": 0,"U" : 0, "V" : 0, "W": 0, "X": 0,
                    "Y" : 0,"Z": 0}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in alphabet: 
        frequency = letters_string.count(letter)
        letters_dict[letter] = frequency

    return letters_dict



def display_letters(freq_dict):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in alphabet:
        
        stars = "*" * freq_dict[i]
        print(i, "|", stars)
    
    
    
def main():
    letters_string = input()
    letters_string = letters_string.upper()
    print(letters_string)
    letters_dict = chart_letters(letters_string)
    display_letters(letters_dict)
    


main()
