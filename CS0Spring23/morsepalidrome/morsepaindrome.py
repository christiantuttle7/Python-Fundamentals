def ispali(code):
    pali = True
    r_code = code[::-1]
    #print(r_code)
    for i in range(len(code)):
        if( code[i] != r_code[i]):
            pali = False
    return pali

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '0':'-----'}

line = input()
code = ''
for l in line:
    if(l.upper().isalnum() ):
        code = code + MORSE_CODE_DICT[l.upper()]
        
ans = True
if(code == ''):
    ans = False
else:
    #print(code)
    ans = ispali(code)
if(ans == True):
    final_ans = 1
else:
    final_ans = 0

print(final_ans)


