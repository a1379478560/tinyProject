###########################################################
#  Programming Project 06
#
#  Algorithm
#    prompt for two file name.
#    input two file name.
#    keep prompting until a valid file is entered
#    read data from files.
#    extract useful data from files.
#    caculate and format the data.
#    show the data at command line.
#    prompt if you want plot.
#    if user input "yes" then plot.
#    quit.
###########################################################

import operator
import pylab  # for plotting
from operator import itemgetter  # useful for sorting


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


def find_index(header_lst, s):
    '''
    Find a string`s index in a list.
    :param header_lst: The header row split into a list of strings.
    :param s: A string in head_lst.
    :return:Return the index (int) of the string s in the header row list. This index is the column index of the string in the
data file.
    '''
    for i,ss in enumerate(header_lst):
        if ss==s:
            return i
    return None
    pass  # replace this placeholder with your code


def read_2016_file(fp):
    '''
    Read data from given file pointer .
    :param fp: A file pointer.
    :return: The data read from the file.
    '''
    data=fp.readlines()
    for i,x in enumerate(data):   #convert string to list
        data[i]=x.split(",")
    state_index=2
    native_index=find_index(data[0],"EST_VC197")
    naturalized_index=find_index(data[0],'EST_VC201')
    non_citizens_index=find_index(data[0],'EST_VC211')
    unsorted_list=[]
    for x in data[2:]:
        state=x[state_index]
        native=int(x[native_index])
        naturalized=int(x[naturalized_index])
        non_citizens=int(x[non_citizens_index])
        total_residents_num=native+naturalized+non_citizens
        ratio_of_naturalized=naturalized/total_residents_num
        ratio_of_non_citizens=non_citizens/total_residents_num
        unsorted_list.append((state,native,naturalized,ratio_of_naturalized,non_citizens,ratio_of_non_citizens))
    get_sort_num=operator.itemgetter(-1)
    return sorted(unsorted_list,key=get_sort_num,)


def read_2000_file(fp2):
    '''
    Read data from given file pointer .
    :param fp: A file pointer.
    :return: The data read from the file.
    '''
    data2=fp2.readlines()
    for i,x in enumerate(data2):  #convert string to list
        data2[i]=x.split(",")
    total_population=int(data2[2][find_index(data2[0],"HC01_VC02")])
    count_of_native=int(data2[2][find_index(data2[0],'HC01_VC03')])
    count_of_naturalized=int(data2[2][find_index(data2[0],'HC01_VC05')])
    count_of_non_citizens = int(data2[2][find_index(data2[0], 'HC01_VC06')])
    return (total_population,count_of_native,count_of_naturalized,count_of_non_citizens)


def calc_totals(data_sorted):
    '''
    Calculate the toltal number of three kind of people.
    :param data_sorted:A list to calculate.
    :return: Returns one tuple of values.
    '''
    total_native=0        #initial 4 various with 0.
    total_natualized=0
    total_non_citizens=0
    total_residents=0
    for x in data_sorted:
        total_native+=x[1]
        total_natualized+=x[2]
        total_non_citizens+=x[4]
    total_residents=total_non_citizens+total_natualized+total_native
    return (total_native,total_natualized,total_non_citizens,total_residents)


def make_lists_for_plot(native_2000, naturalized_2000, non_citizen_2000, native_2016, naturalized_2016,
                        non_citizen_2016):
    '''Ensure your data is organized for plotting.'''
    return ([native_2000, native_2016],[ naturalized_2000, naturalized_2016],[ non_citizen_2000, non_citizen_2016])


def plot_data(native_list, naturalized_list, non_citizen_list):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(2)  # create 2 containers to hold the data for graphing
    # assign each list's values to the 3 items to be graphed, include a color and a label
    pylab.bar(X, native_list, color='b', width=0.25, label="native")
    pylab.bar(X + 0.25, naturalized_list, color='g', width=0.25, label="naturalized")
    pylab.bar(X + 0.50, non_citizen_list, color='r', width=0.25, label="non-citizen")

    pylab.title("US Population")
    # label the y axis
    pylab.ylabel('Population (hundred millions)')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2000", "2016"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")


def int2str(num):
    '''
    Format Int type number to string.
    '''
    result_str=""
    while num>999:
        temp=""
        if num%1000<10:
            temp="00"
        elif num%1000<100:
            temp="0"
        result_str=temp+str(num%1000)+","+result_str
        num=num//1000
    result_str = str(num) + "," + result_str
    return result_str[:-1]


def float2percentage(num):
    '''
    Format float to percentage.
    '''
    return str(round(num*100,1))+"%"


def auto_format(x):
    if type(x)==int:
        return int2str(x)
    if type(x)==float:
        return float2percentage(x)
    return x


def main():
    '''Insert DocString here.'''
    file_2016=open_file()
    file_2000=open_file()
    data_2016=read_2016_file(file_2016)
    data_2000=read_2000_file(file_2000)
    data_total_2016=calc_totals(data_2016)
    plot_list=make_lists_for_plot( \
        data_2000[1],data_2000[2],data_2000[3],data_total_2016[0],data_total_2016[1],data_total_2016[2])
    print("\n\t\t\t\t\t\t\t\t2016 Population: Native, Naturalized, Non-Citizen\n")
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format("State","Nati" \
            "ve","Naturalized","Percent Naturalized", "Non-Citizen","Percent Non-Citizen"))
    for x in data_2016:
        print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format( \
            auto_format(x[0]),auto_format(x[1]),auto_format(x[2]),auto_format(x[3]), auto_format(x[4]),auto_format(x[5])))
    print("="*112)
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format( \
        "Total 2016", auto_format(data_total_2016[0]), auto_format(data_total_2016[1]), \
        auto_format(data_total_2016[1]/data_total_2016[3]), auto_format(data_total_2016[2]), auto_format(data_total_2016[2]/data_total_2016[3])))
    print("{:<20s}{:>15s}{:>17s}{:>22s}{:>16s}{:>22s}".format( \
        "Total 2000", auto_format(data_2000[1]), auto_format(data_2000[2]), auto_format(data_2000[2]/data_2000[0]), \
        auto_format(data_2000[3]), auto_format(data_2000[3]/data_2000[0])))
    if input("Do you want to plot? ")=="yes":
        plot_data(plot_list[0],plot_list[1],plot_list[2])
if __name__ == "__main__":
    main()