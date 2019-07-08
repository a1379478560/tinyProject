###########################################################
#  Programming Project 07
#
#  Algorithm
#    Prompt for a file name.
#    Input a file name.
#    Keep prompting until a valid file is entered
#    Read data from file.
#    Extract useful data from the file.
#    Caculate and format the data.
#    Show the data at command line.
#    Prompt if you want plot.
#    If user input "yes" then plot.
#    Quit.
###########################################################

import pylab  # needed for plotting
STATUS = ['Approved', 'Denied', 'Settled']


def open_file():
    '''
    Returns the file pointer to the file opened by asking user for the file
    name.  keep prompting until a valid file is entered.
    Return : The file pointer of data file.
    '''
    file_name = input("Please enter a file name: ")
    while True:
        try:
            f=open(file_name,"r")
            return f
        except:
            file_name=input("File not found. Please enter a valid file name: ")


def read_file(fp):
    '''
    Read data from a given file pointer .
    :param fp: A file pointer.
    :return: The data read from the file.
    '''
    data_list=[]
    file_data=fp.readlines()[1:]
    for row in file_data:
        row_list=row.split(",")
        if len(row_list)<12:
            continue
        for i in range(len(row_list)):
            row_list[i]=row_list[i].strip()
        if row_list[1]=="" or row_list[4]=="" or row_list[9]=="" \
            or row_list[10]=="" or row_list[11]=="":
            continue
        if row_list[1][-2:] in ["02","03","04","05","06","07","08","09",]:
            date_received=row_list[1]
        else:
            continue
        airport_name=row_list[4]
        claim_amount=float(row_list[9].replace("$","").replace(";",""))
        status=row_list[10]
        close_amount=float(row_list[11].replace("$","").replace(";",""))
        data_list.append((date_received,airport_name,claim_amount,status,close_amount))
    return data_list


def process(data):
    '''
    Extract useful data from given data.
    :param data: The data read from file.
    :return: Return a list that content useful data.
    '''
    total=0
    max_claim=0
    max_claim_airport=""
    all_close_amount=0
    all_close_num=0
    total_cases=[0,0,0,0,0,0,0,0]
    total_denied = [0, 0, 0, 0, 0, 0, 0, 0]
    total_settled_approved =[0,0,0,0,0,0,0,0]
    for row in data:
        if row[2]>max_claim:
            max_claim=row[2]
            max_claim_airport=row[1]
        if row[3]=="Settled" or row[3]=="Approved":
            total+=1
            if row[4]!=0:
                all_close_amount+=row[4]
                all_close_num+=1
            year=int(row[0][-1])
            total_cases[year-2]+=1
            total_settled_approved[year-2]+=1
        if row[3]=="Denied":
            year = int(row[0][-1])
            total+=1
            total_cases[year - 2] += 1
            total_denied[year-2]+=1
    average=all_close_amount/all_close_num
    return (total_cases,total_settled_approved,total_denied,total,average,max_claim,max_claim_airport)


def display_data(tup):
    '''
    Print formated data.
    :param tup:A list type data will be print.
    :return:Returns nothing.
    '''
    temp=[]
    for i in range(3):
        tmp=[]
        for j in range(8):
            tmp.append( format(tup[i][j], ","))
        temp.append(tmp)
    print("TSA Claims Data: 2002 - 2009")
    print("\nN =", format(tup[3],","))
    print()
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format(" ", '2002', '2003', '2004', '2005', '2006',
                                                                          '2007', '2008', '2009'))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Total", temp[0][0], temp[0][1], temp[0][2], temp[0][3],
                                                                          temp[0][4], temp[0][5], temp[0][6], temp[0][7], ))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Settled", temp[1][0], temp[1][1], temp[1][2], temp[1][3],
                                                                          temp[1][4], temp[1][5], temp[1][6], temp[1][7], ))
    print("{:<8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Denied", temp[2][0], temp[2][1], temp[2][2],
                                                                          temp[2][3], temp[2][4], temp[2][5], temp[2][6], temp[2][7], ))
    print()
    print("Average settlement: ${:<10s}".format(format(round(tup[4], 2),',')))
    print("The maximum claim was ${} at {} Airport".format(format(tup[5],",.2f"), tup[6]))


def plot_data(accepted_data, settled_data, denied_data):
    '''Plot the three lists as bar graphs.'''

    X = pylab.arange(8)  # create 8 items to hold the data for graphing
    # assign each list's values to the 8 items to be graphed, include a color and a label
    pylab.bar(X, accepted_data, color='b', width=0.25, label="total")
    pylab.bar(X + 0.25, settled_data, color='g', width=0.25, label="settled")
    pylab.bar(X + 0.50, denied_data, color='r', width=0.25, label="denied")

    # label the y axis
    pylab.ylabel('Number of cases')
    # label each bar of the x axis
    pylab.xticks(X + 0.25 / 2, ("2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009"))
    # create a legend
    pylab.legend(loc='best')
    # draw the plot
    pylab.show()
    # optionally save the plot to a file; file extension determines file type
    # pylab.savefig("plot.png")


def main():
    '''
    The main function in this program. Takes no input. Returns nothing.
    Call the functions from here. Close the file here.
    '''
    file_data=read_file(open_file())
    calculated_data=process(file_data)
    display_data(calculated_data)
    if input("Plot data (yes/no): ")=="yes":
        plot_data(calculated_data[0],calculated_data[1],calculated_data[2])

if __name__ == "__main__":
    main()