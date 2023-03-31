import json
import random

with open("EDMTDictionary.json") as json_dict:
    words_dict = json.load(json_dict)
    #print(type(words_dict))
    #print('There are {0} words in the file.'.format(len(words_dict)))
    #print(words_dict[2584])
    #print(type(words_dict[2584]))
    choice = random.choice(words_dict)
    print('{}\n{}\n{}'.format(choice['word'], \
        choice['type'], choice['description']))
    

