import re

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }



def english_to_morse(input_file: str = "lorem.txt",output_file: str = "lorem_morse.txt"):

    #open the input and output files, read the input and convert all letters to uppercase
    with open(input_file, "r") as input, open(output_file, "w") as output:
        content = input.read().upper()

        #replace all . and - with their morse code because these are the morse building blocks
        #avoid looping over these later and continuously replacing the morse letters with morse for . and -
        content = re.sub(r'[.]', MORSE_CODE['.'], content) or re.sub(r'[-]', MORSE_CODE['-'], content)

        # loop over the morse code and replace each letter in the input file with its morse code except . - and space
        for char, morse in MORSE_CODE.items():
            content = content.replace(char, morse) if char != '.' and char != '-' and char != ' ' else content

        #replace all spaces with new lines to separate the words
        sep_lines = content.replace(" ", "\n")

        #write the output to the output file
        output.write(sep_lines)



if __name__ == '__main__':
        english_to_morse()
   