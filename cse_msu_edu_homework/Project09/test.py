from proj09 import *
stu={'Adele': {'All I Ask': {'lesson', 'sure', 'word', 'speak', 'night', 'cause', 'leave', 'friend', 'need', 'play', 'run', 'vicious', 'give', 'eyes', 'wanna', 'hold', 'tell', 'left', 'last', 'next', 'said', 'lovers', 'one', 'knows', 'ends', 'take', 'honesty', 'use', 'look', 'love', 'since', 'pretend', 'memory', 'forgiveness', 'matters', 'get', 'door', 'remember', 'asking', 'wrong', 'coming', 'say', 'scared', 'let', 'cruel', 'tomorrow', 'way', 'hand', 'like', 'heart', 'ask', 'know'}, "Can't Let Go": {'platter', 'cold', 'hard', 'hid', 'lump', 'thought', 'truth', 'faked', 'much', 'thrill', 'feel', 'note', 'life', 'tell', 'gave', 'sometimes', 'like', 'coat', 'said', 'dark', 'heaven', 'told', 'throat', 'yet', 'slow', 'die', 'lied', 'wanted', 'go', 'save', 'love', 'thinking', 'oooh', 'went', 'baby', 'kill', 'seam', 'loved', 'wrong', 'round', 'arms', 'write', 'let', 'find', 'hope', 'even', 'everything', 'wrote', 'time', 'know'}}, 'Bob Dylan': {'4Th Time Around': {'forget', 'back', 'hummed', 'give', 'waited', 'screamed', 'till', 'filled', 'drawer', 'piece', 'tried', 'got', 'threw', 'hallway', 'make', 'went', 'loved', 'boot', 'shirt', 'floor', 'face', 'something', 'thumbs', 'clear', 'thought', 'drum', 'tapped', 'jamaican', 'spit', 'last', 'cried', 'sense', 'deaf', 'better', 'dirt', 'stood', 'get', 'crutch', 'knocked', 'walked', 'finding', 'words', 'suit', 'leaned', 'handed', 'asked', 'much', 'covered', 'forced', 'come', 'wheelchair', 'said', 'picture', 'mine', 'gum', 'must', 'felt', 'straightened', 'time', 'ask', 'hands', 'breaking', 'buttoned', 'leave', 'fell', 'waste', 'eyes', 'worked', 'outside', 'rum', 'everybody', 'look', 'go', 'else', 'forgotten', 'wasted', 'red', 'gallantly', 'pockets', 'brought', 'took', 'shoe'}, 'A Satisfied Mind': {'lost', 'heard', 'little', 'happened', 'richer', 'ones', 'certain', 'world', 'game', 'ten', 'things', 'mind', 'leave', 'run', 'life', 'know', 'doubt', 'wading', 'dreamed', 'suddenly', 'hmm', 'lifes', 'times', 'old', 'satisfied', 'one', 'many', 'money', 'man', 'far', 'fortune', 'comes', 'friends', 'get', 'loved', 'someone', 'say', 'find', 'way', 'everything', 'fame', 'start', 'time', 'dime', 'hard'}}}
newstu=read_data(open("songdata_test.csv"),read_stopwords(open("stopwords.txt")))
b={'Adele': {'All I Ask': {'coming', 'pretend', 'like', 'honesty', 'bridge', 'need', 'way',
'speak', 'take', 'love', 'scared', 'let', 'sure', 'hand', 'said', 'forgiveness', 'verse',
'run', 'vicious', 'say', 'tomorrow', 'word', 'cruel', 'wrong', 'one', 'memory', 'left',
'tell', 'since', 'next', 'night', 'lesson', 'wanna', 'eyes', 'know', 'remember', 'cause',
'ask', 'door', 'matters', 'chorus', 'hold', 'lovers', 'heart', 'use', 'last', 'give',
'play', 'asking', 'friend', 'ends', 'knows', 'look', 'get', 'leave'}, "Can't Let Go":
{'kill', 'like', 'hope', 'throat', 'lump', 'bridge', 'wrote', 'find', 'told', 'time',
'dark', 'thought', 'faked', 'sometimes', 'truth', 'love', 'lied', 'much', 'even', 'let',
'yet', 'die', 'said', 'heaven', 'write', 'verse', 'went', 'life', 'hard', 'coat', 'go',
'wrong', 'arms', 'oooh', 'save', 'everything', 'thrill', 'platter', 'tell', 'wanted',
'outro', 'seam', 'loved', 'know', 'cold', 'chorus', 'thinking', 'feel', 'round', 'slow',
'hid', 'baby', 'note', 'gave'}}, 'Bob Dylan': {'4Th Time Around': {'filled', 'wheelchair',
'thought', 'handed', 'much', 'covered', 'said', 'red', 'tried', 'screamed', 'deaf',
'hallway', 'left', 'shoe', 'outside', 'till', 'eyes', 'gallantly', 'ask', 'crutch',
'threw', 'suit', 'leave', 'words', 'come', 'breaking', 'mine', 'cried', 'went', 'pockets',
'fell', 'dear', 'go', 'forgotten', 'back', 'jamaican', 'floor', 'face', 'gum', 'buttoned',
'spit', 'picture', 'give', 'stood', 'get', 'must', 'dirt', 'tapped', 'waited', 'waste',
'drawer', 'felt', 'something', 'knocked', 'thumbs', 'wasted', 'finding', 'worked', 'drum',
'shirt', 'better', 'look', 'forced', 'time', 'walked', 'clear', 'rum', 'cute', 'everybody',
'took', 'leaned', 'sense', 'asked', 'brought', 'straightened', 'hummed', 'else', 'loved',
'make', 'piece', 'boot', 'last', 'got', 'forget', 'lies', 'hands'}, 'A Satisfied Mind':
{'man', 'things', 'time', 'find', 'little', 'way', 'lost', 'certain', 'happened', 'wading',
'suddenly', 'heard', 'times', 'satisfied', 'ones', 'old', 'start', 'run', 'ten', 'life',
'game', 'say', 'hmm', 'hard', 'comes', 'richer', 'one', 'everything', 'fame', 'many',
'far', 'world', 'friends', 'loved', 'know', 'mind', 'dreamed', 'lifes', 'someone',
'fortune', 'dime', 'money', 'doubt', 'get', 'leave'}}}

for x in stu :
    for y in stu[x]:
        print(stu[x][y].symmetric_difference(b[x][y]))

print("*"*80)

for x in newstu :
    for y in newstu[x]:
        print(newstu[x][y].symmetric_difference(b[x][y]))


# print(string.punctuation,)
# print(string.digits)
# print(string.ascii_lowercase)

#print(newstu)

# print(calculate_average_word_count(data_dict))
#
# print(newstu["Katy Perry"])
# print(calculate_average_word_count({"test":newstu["Katy Perry"]}))