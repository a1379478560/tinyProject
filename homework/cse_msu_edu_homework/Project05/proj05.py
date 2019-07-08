###########################################################
#  Programming Project 05
#
#  Algorithm
#    prompt for an file name.
#    input an file name.
#    keep prompting until a valid file is entered
#    loop 6 times
#       read a line from this file.
#           extract vvalues in this line.
#           find the maximum growth rate.
#       format and output the maximux growth rate.
#       output the maximux growth in all lines.
###########################################################

def open_file():
    '''
    Returns the file pointer to the file opened by asking user for the file
    name.  keep prompting until a valid file is entered.
    Return : The file pointer of data file.
    '''
    while True:
        file_name=input("Enter a file name:")
        try:
            f=open(file_name,"r")
            return f
        except:
            print("Error. Please try again.")
            continue

def print_headers():
    '''Print the headers for the output. '''
    print("\n\tMaximum Population Change by Continent\n")
    print("{:<26s}{:>9s}{:>10s}".format("Continent", "Years", "Delta"))

def calc_delta(line, col):
    '''
    Calculate the change between two  number(int) that extract from given line(string).
    line:The string that contain population number data.
    col:The address that population number in given string(line).
    Return:  a float type change of given numbers.
    '''

    start_year_num = int(line[9+6*col:9+6*(col+1)])
    stop_year_num = int(line[9+6*(col+1):9+6*(col+2)])
    return (stop_year_num-start_year_num)/start_year_num

def format_display_line(continent, year, delta):
    '''
    Format given arguments to a string.
    continent: A string need to be format.
    year: A int type data need to be format.
    delta: The change between to given years,float.
    Return The formated string.
    '''
    period_string=str(year-50)+"-"+str(year)
    delta_string=str(int(delta*100+0.5))+"%"
    return "{:<26s}{:>9s}{:>10s}".format(continent, period_string, delta_string)


def main():
    '''
    The main function in this program. Takes no input. Returns nothing.
    Call the functions from here. Close the file here.
    '''
    file_pointer=open_file()
    print_headers()
    file_pointer.readline() #Read and discard the first two lines in the data text.
    file_pointer.readline()

    max_of_all_continents_delta = 0    # record the maximux change of continents.
    max_of_all_continents_display_line = ""
    for i in range(2,8):
        file_line_string=file_pointer.readline()
        max_delta = 0    # record the maximux change of years.
        max_delta_col = 0
        for j in range(1,6):
            delta_float=calc_delta(file_line_string,j)
            if delta_float>max_delta:
                max_delta=delta_float
                max_delta_col=j
        display_line=format_display_line(file_line_string[:15].replace(" ",""),1700+50*(max_delta_col+1),max_delta)
        print(display_line)
        if max_delta>max_of_all_continents_delta:
            max_of_all_continents_delta=max_delta
            max_of_all_continents_display_line=display_line
    print("\nMaximum of all continents:")
    print(max_of_all_continents_display_line)
    file_pointer.close()          #Close the fata file.

if __name__ == "__main__":
    main()