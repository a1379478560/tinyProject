###########################################################
#  Programming Project 09
#
#  Algorithm
#    prompt for an file name of stopwords.
#    read stopwords in this file.
#    prompt for an file name of song data.
#    read songs data in this file.
#    question if plot.
#     if user input "yes",plot the average vocabulary suze.
#
#    loop until user input a string euqal to "".
#       prompt for a string contain several words.
#           extract words in this string.
#           search which songs contain this several words.
#       format and output how many songs contains that words.
#       format and output top 5 of that songs.
###########################################################
import csv
import string
import pylab
from operator import itemgetter


def open_file(message):
    '''
    Returns the file pointer to the file opened by asking user for the file
    name.  keep prompting until a valid file is entered.
    :param message the prompt string for in put.
    Return : The file pointer of data file.
    '''
    file_name_string = input(message)
    while True:   #Loop until user input a valid file name.
        try:
            fp=open(file_name_string,"r",encoding ="windows-1252")
            return fp
        except:
            print("File is not found! Try Again!")
            file_name_string = input(message)


def read_stopwords(fp):
    '''
    Read stop word from a given file.
    :param fp: An file pointer.
    :return: A set of stop words.
    '''
    file_list=fp.readlines()
    stopwords_set=set()
    for line in file_list:
        tmp=line.lower()
        tmp=tmp.replace("\n","")
        stopwords_set.add(tmp)
    return stopwords_set


def validate_word(word, stopwords):
    '''
    Verify if a given word can be a "search word".
    :param word: Word to be verify.
    :param stopwords: A set of stop word read from given file.
    :return: A boolean value .
    '''
    if word!=word.replace("-",""):
        print(word)
    return word not in stopwords and word.isalpha()


def process_lyrics(lyrics, stopwords):
    '''
    Extract word from lyrics.
    :param lyrics: A string of lyrics.
    :param stopwords: Stopword.
    :return: A set of word can be search.
    '''
    lyrics_word_set=set()
    words=lyrics.split(" ")
    for word in words:
        tmp=word.lower()
        tmp=tmp.strip()
        punctuation_string=string.punctuation
        for i in range(10):
            try:
                if tmp[-1] in punctuation_string:
                    tmp=tmp[:-1]
                elif tmp[0] in punctuation_string:
                    tmp=tmp[1:]
                else:
                    break
            except:
                break
        if tmp=="":
            continue
        if validate_word(tmp,stopwords):
            lyrics_word_set.add(tmp)

    return lyrics_word_set


def read_data(fp, stopwords):
    '''
    Read data from a given file.
    :param fp: An file pointer.
    :param stopwords: Stopword.
    :return: A dict of songs data.
    '''
    songs_dict={}
    reader=csv.reader(fp)
    next(reader)
    for line in reader:
        singer=line[0]
        song=line[1]
        lyrics=line[2]
        lyrics=lyrics.lower()
        words=process_lyrics(lyrics,stopwords)
        update_dictionary(songs_dict,singer,song,words)
    return songs_dict


def update_dictionary(data_dict, singer, song, words):
    '''
    Insert data to dara_dict.
    :param data_dict: Songs data.
    :param singer: A string of singer.
    :param song: A string of songs.
    :param words:A set of words of this song.
    :return:None.
    '''
    if singer in data_dict:
        data_dict[singer][song]=words
    else:
        data_dict[singer] = {}
        data_dict[singer][song] = words


def calculate_average_word_count(data_dict):
    '''
    Calculate average word of a singer's songs.
    :param data_dict: All singger and his songs.
    :return:A dict of singer's average words number in his song.
    '''
    average_count_dict={}
    for singer in data_dict:
        songs_count_int=len(data_dict[singer])
        words_count_int=0
        for song in data_dict[singer]:
            words_count_int=words_count_int+len(data_dict[singer][song])
        average_count_dict[singer]=words_count_int/songs_count_int
    return average_count_dict


def find_singers_vocab(data_dict):
    '''
    Find singer's all vocabulary in his songs.
    :param data_dict:A dict of singer and his songs.
    :return:A dict of singer's all vocabulary in his songs.
    '''
    singers_vocab_dict={}
    for singer in data_dict:
        vocab_set=set()
        for song in data_dict[singer]:
            vocab_set=vocab_set.union(data_dict[singer][song])
        singers_vocab_dict[singer]=vocab_set
    return singers_vocab_dict


def display_singers(combined_list):
    '''
    Format and display singers by average word acount.
    :param combined_list: A list of singer and his average word count.
    :return: None.
    '''
    combined_list=sorted(combined_list,key=itemgetter(1,3),reverse=True)     #sort the given data.
    print("{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print( '-' * 80)
    loop_num=10
    if len(combined_list)<10:
        loop_num=len(combined_list)
    for i in range(loop_num):
            print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(combined_list[i][0], combined_list[i][1],
                                                          combined_list[i][3],combined_list[i][2]))


def vocab_average_plot(num_songs, vocab_counts):
    """
    Plot vocab. size vs number of songs graph
    num_songs: number of songs belong to singers (list)
    vocab_counts: vocabulary size of singers (list)

    """
    pylab.scatter(num_songs, vocab_counts)
    pylab.ylabel('Vocabulary Size')
    pylab.xlabel('Number of Songs')
    pylab.title('Vocabulary Size vs Number of Songs')
    pylab.show()


def search_songs(data_dict, words):
    '''
    Search songs that contains given words.
    :param data_dict: Songs data.
    :param words:A set of given words.
    :return:A list of songs that contains given words.
    '''
    songs_list=[]
    for singer in data_dict:
        for song in data_dict[singer]:
            if words.issubset(data_dict[singer][song]):
                songs_list.append((singer,song))
    songs_list=sorted(songs_list,key=itemgetter(0,1))

    return songs_list


def main():
    ''' Main function.'''
    stopwords_set=read_stopwords(open_file('Enter a filename for the stopwords: '  ))
    songs_dict = read_data(open_file('Enter a filename for the song data: '), stopwords_set)
    average_word_count_dict=calculate_average_word_count(songs_dict)
    singers_vocab_dict=find_singers_vocab(songs_dict)
    singers_songs_list=list()
    for singer in songs_dict:     #generate  thr content of singers_list
        singer_name=singer
        songs_count=len(songs_dict[singer])
        average_word_count=average_word_count_dict[singer]
        vocabulary_size=len(singers_vocab_dict[singer])
        singers_songs_list.append((singer_name,average_word_count,songs_count,vocabulary_size))
    display_singers(singers_songs_list)
    num_songs=list()
    vocab_counts=list()
    for singer in singers_songs_list:
        num_songs.append(singer[2])
        vocab_counts.append(singer[3])
    while 1:
        choice=input('Do you want to plot (yes/no)?: ')
        if (choice=="yes"):
            vocab_average_plot(num_songs,vocab_counts)
            break
        elif(choice=="no"):
            break
        else:
            continue
    print("Search Lyrics by Words\n")
    while 1:
        words_string=input("Input a set of words (space separated), press enter to exit: ")
        if words_string=="":
            break
        words_string=words_string.lower()
        words_list=words_string.split(" ")
        flag=0        #check if all word are valid.
        for word in words_list:
            if not validate_word(word,stopwords_set):
                print("Error in words!")
                print("1-) Words should not have any digit or punctuation")
                print("2-) Word list should not include any stop-word")
                flag=1
                break
        if flag:
            continue
        songs_search_list=search_songs(songs_dict,set(words_list))
        print("There are {} songs containing the given words!".format(len(songs_search_list)))
        print("{:<20s} {:<s}".format("Singer", "Song"))
        loop_num=5
        if len(songs_search_list)<5:
            loop_num=len(songs_search_list)
        for i in range(loop_num):
            print("{:<20s} {:<s}".format(songs_search_list[i][0],songs_search_list[i][1]))

if __name__ == '__main__':
    main()