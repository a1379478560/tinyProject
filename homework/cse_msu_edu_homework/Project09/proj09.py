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
    while True:   #Loop until user input a valid file name.
        file_name=input(message)
        try:
            f=open(file_name,"r",encoding ="windows-1252")
            return f
        except:
            print("File is not found! Try Again!")
            continue


def read_stopwords(fp):
    '''
    Read stop word from a given file.
    :param fp: An file pointer.
    :return: A set of stop words.
    '''
    file_content=fp.readlines()
    stopwords=set()
    for x in file_content:
        stopwords.add(x.lower().replace("\n",""))
    return stopwords


def validate_word(word, stopwords):
    '''
    Verify if a given word can be a "search word".
    :param word: Word to be verify.
    :param stopwords: A set of stop word read from given file.
    :return: A boolean value .
    '''

    return False if(word in stopwords or not word.isalpha()) else True


def process_lyrics(lyrics, stopwords):
    '''
    Extract word from lyrics.
    :param lyrics: A string of lyrics.
    :param stopwords: Stopword.
    :return: A set of word can be search.
    '''
    processed_word=set()
    words=lyrics.split()
    for word in words:
        temp=word.lower().strip()
        while True:
            try:
                if temp[-1] in string.punctuation:
                    temp=temp[:-1]
                elif temp[0] in string.punctuation:
                    temp=temp[1:]
                else:
                    break
            except:
                break
        if temp=="":
            continue
        if validate_word(temp,stopwords):
            processed_word.add(temp)

    return processed_word


def read_data(fp, stopwords):
    '''
    Read data from a given file.
    :param fp: An file pointer.
    :param stopwords: Stopword.
    :return: A dict of songs data.
    '''
    data_dict={}
    reader=csv.reader(fp)
    next(reader)
    for row in reader:
        artist=row[0]
        song=row[1]
        text=row[2].lower()
        words=process_lyrics(text,stopwords)
        update_dictionary(data_dict,artist,song,words)
    return data_dict


def update_dictionary(data_dict, singer, song, words):
    '''
    Insert data to dara_dict.
    :param data_dict: Songs data.
    :param singer: A string of singer.
    :param song: A string of songs.
    :param words:A set of words of this song.
    :return:None.
    '''
    if not singer in data_dict:
        data_dict[singer]={}
    data_dict[singer][song]=words


def calculate_average_word_count(data_dict):
    '''
    Calculate average word of a singer's songs.
    :param data_dict: All singger and his songs.
    :return:A dict of singer's average words number in his song.
    '''
    average_word_count={}
    for x in data_dict:
        songs_num=len(data_dict[x])
        words_num=0
        for y in data_dict[x]:
            words_num+=len(data_dict[x][y])
        average_word_count[x]=words_num/songs_num
    return average_word_count


def find_singers_vocab(data_dict):
    '''
    Find singer's all vocabulary in his songs.
    :param data_dict:A dict of singer and his songs.
    :return:A dict of singer's all vocabulary in his songs.
    '''
    singers_vocab={}
    for x in data_dict:
        vocab=set()
        for y in data_dict[x]:
            vocab=vocab.union(data_dict[x][y])
        singers_vocab[x]=vocab
    return singers_vocab


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
    for i in range(10):
        try:
            print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(combined_list[i][0], combined_list[i][1], combined_list[i][3],
                                                            combined_list[i][2]))
        except:
            break


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
    songs=[]
    for x in data_dict:
        for y in data_dict[x]:
            if words.issubset(data_dict[x][y]):
                songs.append((x,y))
    songs=sorted(songs,key=itemgetter(0,1))

    return songs


def main():
    ''' Main function.'''
    message_stopwords= 'Enter a filename for the stopwords: '       #prompt message
    message_song_data= 'Enter a filename for the song data: '

    stopwords=read_stopwords(open_file(message_stopwords))
    song_data = read_data(open_file(message_song_data), stopwords)
    average_word_count_of_all_singer=calculate_average_word_count(song_data)
    singers_vocab=find_singers_vocab(song_data)
    singers_list=[]
    for singer in song_data:     #generate  thr content of singers_list
        singer_name=singer
        number_of_songs=len(song_data[singer])
        average_word_count=average_word_count_of_all_singer[singer]
        vocabulary_size=len(singers_vocab[singer])
        singers_list.append((singer_name,average_word_count,number_of_songs,vocabulary_size))
    display_singers(singers_list)
    num_songs=[]
    vocab_counts=[]
    for x in singers_list:
        num_songs.append(x[2])
        vocab_counts.append(x[3])
    while True:
        yes_or_no=input('Do you want to plot (yes/no)?: ')
        if (yes_or_no=="yes"):
            vocab_average_plot(num_songs,vocab_counts)
            break
        elif(yes_or_no=="no"):
            break
        else:
            continue
    print("Search Lyrics by Words\n")
    while True:
        words=input("Input a set of words (space separated), press enter to exit: ")
        if words=="":
            break
        words=words.lower()
        words=words.split(" ")
        flag=0        #check if all word are valid.
        for word in words:
            if not validate_word(word,stopwords):
                print("Error in words!")
                print("1-) Words should not have any digit or punctuation")
                print("2-) Word list should not include any stop-word")
                flag=1
                break
        if flag:
            continue
        songs_search=search_songs(song_data,set(words))
        print("There are {} songs containing the given words!".format(len(songs_search)))
        if len(songs_search):
            print("{:<20s} {:<s}".format("Singer", "Song"))
        for i,songs in enumerate(songs_search):
            print("{:<20s} {:<s}".format(songs[0],songs[1]))
            if i>=4:
                break

if __name__ == '__main__':
    main()