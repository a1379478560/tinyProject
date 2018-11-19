from proj09 import *
stu={'Adele': {'All I Ask': {'lesson', 'sure', 'word', 'speak', 'night', 'cause', 'leave', 'friend', 'need', 'play', 'run', 'vicious', 'give', 'eyes', 'wanna', 'hold', 'tell', 'left', 'last', 'next', 'said', 'lovers', 'one', 'knows', 'ends', 'take', 'honesty', 'use', 'look', 'love', 'since', 'pretend', 'memory', 'forgiveness', 'matters', 'get', 'door', 'remember', 'asking', 'wrong', 'coming', 'say', 'scared', 'let', 'cruel', 'tomorrow', 'way', 'hand', 'like', 'heart', 'ask', 'know'}, "Can't Let Go": {'platter', 'cold', 'hard', 'hid', 'lump', 'thought', 'truth', 'faked', 'much', 'thrill', 'feel', 'note', 'life', 'tell', 'gave', 'sometimes', 'like', 'coat', 'said', 'dark', 'heaven', 'told', 'throat', 'yet', 'slow', 'die', 'lied', 'wanted', 'go', 'save', 'love', 'thinking', 'oooh', 'went', 'baby', 'kill', 'seam', 'loved', 'wrong', 'round', 'arms', 'write', 'let', 'find', 'hope', 'even', 'everything', 'wrote', 'time', 'know'}}, 'Bob Dylan': {'4Th Time Around': {'forget', 'back', 'hummed', 'give', 'waited', 'screamed', 'till', 'filled', 'drawer', 'piece', 'tried', 'got', 'threw', 'hallway', 'make', 'went', 'loved', 'boot', 'shirt', 'floor', 'face', 'something', 'thumbs', 'clear', 'thought', 'drum', 'tapped', 'jamaican', 'spit', 'last', 'cried', 'sense', 'deaf', 'better', 'dirt', 'stood', 'get', 'crutch', 'knocked', 'walked', 'finding', 'words', 'suit', 'leaned', 'handed', 'asked', 'much', 'covered', 'forced', 'come', 'wheelchair', 'said', 'picture', 'mine', 'gum', 'must', 'felt', 'straightened', 'time', 'ask', 'hands', 'breaking', 'buttoned', 'leave', 'fell', 'waste', 'eyes', 'worked', 'outside', 'rum', 'everybody', 'look', 'go', 'else', 'forgotten', 'wasted', 'red', 'gallantly', 'pockets', 'brought', 'took', 'shoe'}, 'A Satisfied Mind': {'lost', 'heard', 'little', 'happened', 'richer', 'ones', 'certain', 'world', 'game', 'ten', 'things', 'mind', 'leave', 'run', 'life', 'know', 'doubt', 'wading', 'dreamed', 'suddenly', 'hmm', 'lifes', 'times', 'old', 'satisfied', 'one', 'many', 'money', 'man', 'far', 'fortune', 'comes', 'friends', 'get', 'loved', 'someone', 'say', 'find', 'way', 'everything', 'fame', 'start', 'time', 'dime', 'hard'}}}
newstu=read_data(open("songdata_small.csv"),read_stopwords(open("stopwords.txt")))
b={'Adele': {'All I Ask': {'lesson', 'sure', 'word', 'speak', 'night', 'need', 'friend', 'leave', 'bridge', 'play', 'run', 'vicious', 'give', 'chorus', 'cause', 'eyes', 'wanna', 'hold', 'tell', 'left', 'last', 'one', 'lovers', 'said', 'next', 'verse', 'knows', 'ends', 'take', 'honesty', 'use', 'look', 'since', 'love', 'pretend', 'memory', 'forgiveness', 'matters', 'get', 'door', 'remember', 'asking', 'wrong', 'coming', 'say', 'scared', 'let', 'cruel', 'tomorrow', 'way', 'hand', 'like', 'heart', 'ask', 'know'}, "Can't Let Go": {'platter', 'cold', 'hid', 'thought', 'lump', 'truth', 'much', 'faked', 'time', 'thrill', 'feel', 'bridge', 'note', 'chorus', 'life', 'know', 'tell', 'gave', 'sometimes', 'coat', 'said', 'dark', 'told', 'heaven', 'verse', 'throat', 'slow', 'die', 'lied', 'wanted', 'go', 'wrote', 'save', 'love', 'thinking', 'oooh', 'went', 'baby', 'kill', 'seam', 'loved', 'outro', 'wrong', 'arms', 'round', 'write', 'let', 'find', 'hope', 'even', 'everything', 'like', 'yet', 'hard'}}, 'Bob Dylan': {'4Th Time Around': {'forget', 'back', 'hummed', 'give', 'waited', 'screamed', 'till', 'left', 'lies', 'filled', 'drawer', 'piece', 'tried', 'threw', 'make', 'hallway', 'got', 'went', 'loved', 'boot', 'shirt', 'floor', 'face', 'something', 'thumbs', 'clear', 'thought', 'drum', 'tapped', 'jamaican', 'spit', 'last', 'sense', 'cried', 'deaf', 'better', 'dirt', 'stood', 'shoe', 'get', 'crutch', 'knocked', 'walked', 'finding', 'words', 'suit', 'leaned', 'handed', 'asked', 'much', 'cute', 'covered', 'forced', 'wheelchair', 'said', 'picture', 'mine', 'gum', 'must', 'felt', 'straightened', 'time', 'ask', 'hands', 'dear', 'breaking', 'buttoned', 'leave', 'fell', 'waste', 'eyes', 'worked', 'outside', 'rum', 'everybody', 'look', 'go', 'else', 'forgotten', 'wasted', 'red', 'gallantly', 'pockets', 'brought', 'took', 'come'}, 'A Satisfied Mind': {'lost', 'heard', 'little', 'ones', 'richer', 'happened', 'certain', 'world', 'game', 'ten', 'things', 'mind', 'leave', 'run', 'life', 'know', 'doubt', 'wading', 'dreamed', 'suddenly', 'hmm', 'lifes', 'times', 'old', 'satisfied', 'one', 'many', 'man', 'money', 'far', 'fortune', 'comes', 'friends', 'get', 'loved', 'someone', 'say', 'find', 'way', 'everything', 'fame', 'start', 'time', 'dime', 'hard'}}}

# for x in stu :
#     for y in stu[x]:
#         print(stu[x][y].symmetric_difference(b[x][y]))
#
# print("*"*80)
#
# for x in newstu :
#     for y in newstu[x]:
#         print(newstu[x][y].symmetric_difference(b[x][y]))




data_dict={'Adele': {'All I Ask': {'use', 'honesty', 'scared', 'hand', 'tell', 'door',
'pretend', 'last', 'sure', 'lovers', 'leave', 'forgiveness', 'say', 'ask', 'night',
'vicious', 'ends', 'love', 'coming', 'left', 'knows', 'asking', 'lesson', 'memory',
'wanna', 'heart', 'eyes', 'let', 'take', 'matters', 'give', 'way', 'play', 'cruel',
'friend', 'run', 'since', 'get', 'cause', 'hold', 'one', 'said', 'next', 'wrong', 'like',
'remember', 'tomorrow', 'need', 'speak', 'know', 'word'}, "Can't Let Go": {'lied', 'write',
'lump', 'truth', 'even', 'baby', 'tell', 'gave', 'die', 'save', 'dark', 'heaven',
'thinking', 'round', 'platter', 'go', 'went', 'feel', 'everything', 'hid', 'seam', 'loved',
'let', 'sometimes', 'throat', 'hope', 'yet', 'thought', 'wanted', 'oooh', 'time', 'kill',
'find', 'note', 'told', 'coat', 'slow', 'said', 'much', 'faked', 'life', 'like', 'hard',
'arms', 'know'}}, 'Bob Dylan': {'4Th Time Around': {'threw', 'else', 'filled', 'dirt',
'forgotten', 'waste', 'wasted', 'last', 'must', 'leave', 'words', 'worked', 'breaking',
'handed', 'ask', 'back', 'pockets', 'gallantly', 'go', 'went', 'picture', 'crutch',
'jamaican', 'loved', 'stood', 'better', 'screamed', 'till', 'tapped', 'waited', 'give',
'got', 'straightened', 'sense', 'brought', 'cried', 'covered', 'thought', 'forced', 'took',
'get', 'rum', 'finding', 'something', 'spit', 'make', 'buttoned', 'tried', 'look', 'face',
'wheelchair', 'hands', 'drum', 'felt', 'shoe', 'fell', 'piece', 'everybody', 'leaned',
'asked'}, 'A Satisfied Mind': {'fame', 'ones', 'money', 'start', 'old', 'certain',
'dreamed', 'leave', 'say', 'game', 'things', 'someone', 'suddenly', 'man', 'world',
'lifes', 'comes', 'everything', 'dime', 'loved', 'richer', 'ten', 'little', 'way', 'run',
'lost', 'fortune', 'get', 'time', 'one', 'far', 'times', 'satisfied', 'find', 'wading',
'life', 'doubt', 'hard', 'friends', 'heard', 'happened', 'know', 'many'}}}



print(newstu)

#print(calculate_average_word_count(data_dict))