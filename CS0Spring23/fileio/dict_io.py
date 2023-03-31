import random

def open_dict():
    file = 'dict-words.txt' # a file containing one word per line, works on mac/linux
    with open(file) as f:
        data = f.read()
        # If data is a big list of words, the next print statement takes a while
        #print(data)  
        words = data.split('\n') #words is a list of the words
        print('There are {0} words in the file.'.format(len(words)))
        
        word = random.choice(words)
        print(word)

        letter = 'a'

        if word.find('a') != -1:
            print("Found an a...or more?")
        
        f.close()

    return word

def main():
    random_word = open_dict()
    print("Random Word: ",random_word)
    
if __name__ == "__main__":
    main()