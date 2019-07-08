###########################################################
#  Programming Project 08
#
#  Algorithm
#    prompt for an file name.
#    input an file name.
#    keep prompting until a valid file is entered
#
#    loop until user input a string euqal to "quit".
#       read a line from this file.
#           extract vvalues in this line.
#           prompt for an regioe.
#       format and output the data in this region.
#       prompt for "yes" or "no".
#       if user input yes,plot figure using the data in this region.
###########################################################
import pylab

# from operator import itemgetter   # optional, if you use itemgetter when sorting

REGIONS = {'MENA': 'Middle East and North Africa', 'EUR': 'Europe', \
           'AFR': 'Africa', 'NAC': 'North America and Caribbean', \
           'SACA': 'South and Central America', \
           'WP': 'Western Pacific', 'SEA': 'South East Asia'}


def open_file():
    '''
    Returns the file pointer to the file opened by asking user for the file
    name.  keep prompting until a valid file is entered.
    Return : The file pointer of data file.
    '''
    while True:   #Loop until user input a valid file name.
        file_name=input("Please enter a file name: ")
        try:
            f=open(file_name,"r",encoding ="windows-1252")
            return f
        except:
            print("File not found. Please enter a valid file name: ")
            continue


def create_dictionary(fp):
    '''
    This function receives the opened file object, reads the file, and
    creates the dictionary containing the diabetes prevalence information.
    :param fp:The opened file object.
    :return:A dictionary containing the diabetes prevalence information.
    '''

    DD={}
    file_content=fp.readlines()
    for i in range(1,len(file_content)):
        line_list=file_content[i].split(",")
        country = line_list[1]
        region = line_list[2]
        age_group = line_list[3]
        gender = line_list[4]
        geographic_area = line_list[5]
        diabetes = int(float(line_list[6]) * 1000)
        population = int(float(line_list[7]) * 1000)

        tup = (gender, geographic_area, diabetes, population)

        if region not in DD :    # Check for presence before use.
            DD[region]={}
        if  country not in  DD[region]:
            DD[region][country]={}
        if age_group not in DD[region][country]:
            DD[region][country][age_group]=[]
        DD[region][country][age_group].append(tup)

    return DD


def get_country_total(data):
    '''
        This function receives a dictionary from a specific region, and returns a new
    dictionary of tuples with the number of people with diabetes and the total
    population for each country.
    :param data: A dictionary from a specific region.
    :return:A dictionary of tuples with the number of people with diabetes and the total
    population for each country.
    '''
    res={}

    for x in data:
        people_with_diabetes=0
        total_population=0
        for y in data[x]:
            for z in data[x][y]:
                people_with_diabetes+=z[2]
                total_population+=z[3]
        res[x]=(people_with_diabetes,total_population)
    return res


def display_table(data, region):
    '''
        This function receives a dictionary with the diabetes data for a specific region ,
    and the full name of the region. This function returns nothing. It displays  the
    country name, number of people with diabetes, and the total population of
    that country.
    :param data: A dictionary with the diabetes data for a specific region
    :param region: The name of the region.
    :return: None
    '''
    region=region.upper()
    region_dict={
        'MENA':'Middle East and North Africa',
        'EUR':'Europe',
        'AFR':'Africa',
        'NAC':'North America and Caribbean',
        'SACA':'South and Central America',
        'WP':'Western Pacific',
        'SEA':'South East Asia',
    }
    print('\tDiabetes Prevalence in '+region_dict[region])
    print("{:<25s}{:>20s}{:>16s}\n".format("Country Name","Diabetes Prevalence","Population"))
    diabetes_Prevalence=0
    population=0
    data_list=list(data.keys())    #sort  keys of the data.
    data_list.sort()
    for x in data_list:
        print("{:<25s}{:>20,d}{:>16,d}".format(x[:24], data[x][0], data[x][1]))   #x[:24]  truncate the country names to 24 characters.
        diabetes_Prevalence+=data[x][0]
        population+=data[x][1]
    print()
    print("{:<25s}{:>20,d}{:>16,d}".format("TOTAL", diabetes_Prevalence, population))


def prepare_plot(data):
    '''
    Extract some useful data from a dictionary and return them.
    :param data: A dictionary for a specific region.
    :return Returns a new dictionary with the age group and gender as its keys.
    '''

    res={}
    for x in data:
        for y in data[x]:
            if y not in res:
                res[y]={}
            for z in data[x][y]:
                sex=z[0].upper()
                if sex not in res[y]:
                    res[y][sex]=0
                res[y][sex]+=z[2]
    return res


def plot_data(plot_type, data, title):
    '''
        This function plots the data.
            1) Bar plot: Plots the diabetes prevalence of various age groups in
                         a specific region.
            2) Pie chart: Plots the diabetes prevalence by gender.

        Parameters:
            plot_type (string): Indicates what plotting function is used.
            data (dict): Contains the dibetes prevalence of all the contries
                         within a specific region.
            title (string): Plot title

        Returns:
            None

    '''

    plot_type = plot_type.upper()

    categories = data.keys()  # Have the list of age groups
    gender = ['FEMALE', 'MALE']  # List of the genders used in this dataset

    if plot_type == 'BAR':

        # List of population with diabetes per age group and gender
        female = [data[x][gender[0]] for x in categories]
        male = [data[x][gender[1]] for x in categories]

        # Make the bar plots
        width = 0.35
        p1 = pylab.bar([x for x in range(len(categories))], female, width=width)
        p2 = pylab.bar([x + width for x in range(len(categories))], male, width=width)
        pylab.legend((p1[0], p2[0]), gender)

        pylab.title(title)
        pylab.xlabel('Age Group')
        pylab.ylabel('Population with Diabetes')

        # Place the tick between both bar plots
        pylab.xticks([x + width / 2 for x in range(len(categories))], categories, rotation='vertical')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        # pylab.savefig("plot_bar.png")


    elif plot_type == 'PIE':

        # total population with diabetes per gender
        male = sum([data[x][gender[1]] for x in categories])
        female = sum([data[x][gender[0]] for x in categories])

        pylab.title(title)
        pylab.pie([female, male], labels=gender, autopct='%1.1f%%')
        pylab.show()
        # optionally save the plot to a file; file extension determines file type
        # pylab.savefig("plot_pie.png")


def main():
    "\nDiabetes Prevalence Data in 2017"
    MENU = \
        '''
                    Region Codes
        MENA: Middle East and North Africa
        EUR: Europe
        AFR: Africa
        NAC: North America and Caribbean
        SACA: South and Central America
        WP: Western Pacific
        SEA: South East Asia
        '''

    fp=open_file()
    dic=create_dictionary(fp)
    while True:         #Loop until user input quit.
        print(MENU)
        region_code=input("Enter region code ('quit' to terminate): ")
        region_code=region_code.upper()
        if region_code.upper()=="QUIT":
            break
        if region_code.upper() not in REGIONS:
            print("Error with the region key! Try another region")
            continue
        country_total=get_country_total(dic[region_code.upper()])
        display_table(country_total,region_code)
        while True:                      #Loop until user input "yes" or no.
            choice=input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: ")
            if choice!="yes" and choice!="no":
                print("Incorrect Input! Try Again!")
                continue
            if choice=="yes":
                data_to_plot = prepare_plot(dic[region_code.upper()])
                plot_data("PIE", data_to_plot,
                          'Diabetes prevalence in ' + REGIONS[region_code] + " by Age Group and Gender")
                plot_data("BAR", data_to_plot,
                          'Diabetes prevalence in ' + REGIONS[region_code] + " by Age Group and Gender")
            break


###### Main Code ######
if __name__ == "__main__":
    main()