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

    # Loop until user input a valid file name.
    while 1:
        file=input("Please enter a file name: ")
        try:
            fp=open(file,"r",encoding ="windows-1252")
            break
        except:
            print("File not found. Please enter a valid file name: ")
            continue

    return fp


def create_dictionary(fp):
    '''
    This function receives the opened file object, reads the file, and
    creates the dictionary containing the diabetes prevalence information.
    :param fp:The opened file object.
    :return:A dictionary containing the diabetes prevalence information.
    '''

    file_list=fp.readlines()
    file_list=file_list[1:]
    file_dict = {}
    for line in file_list:
        line_list=line.split(",")

        country = line_list[1]
        region = line_list[2]
        age_group = line_list[3]
        gender = line_list[4]
        geographic_area = line_list[5]
        diabetes = int(float(line_list[6]) * 1000)
        population = int(float(line_list[7]) * 1000)
        tup = (gender, geographic_area, diabetes, population)

        if not region  in file_dict :    # Check for presence before use.
            file_dict[region]={}
        if  not country  in  file_dict[region]:
            file_dict[region][country]={}
        if  not age_group  in file_dict[region][country]:
            file_dict[region][country][age_group]=[]
        file_dict[region][country][age_group].append(tup)

    return file_dict


def get_country_total(data):
    '''
        This function receives a dictionary from a specific region, and returns a new
    dictionary of tuples with the number of people with diabetes and the total
    population for each country.
    :param data: A dictionary from a specific region.
    :return:A dictionary of tuples with the number of people with diabetes and the total
    population for each country.
    '''
    total_dict={}
    for country in data:
        diabetes_people=total_people=0
        for age in data[country]:
            for lis in data[country][age]:
                diabetes_people=diabetes_people+lis[2]
                total_people=total_people+lis[3]
        total_dict[country]=(diabetes_people,total_people)

    return total_dict


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

    data_keys=data.keys()
    keys_list=list(data_keys)    #sort  keys of the data.
    keys_list=sorted(keys_list,reverse=False)

    region_str=REGIONS[region.upper()]
    print('\tDiabetes Prevalence in '+region_str)
    print("{:<25s}{:>20s}{:>16s}".format("Country Name","Diabetes Prevalence","Population"))
    print()
    total_diabetes=total_population=0
    for key in keys_list:
        # key[0:24]  truncate the country names to 24 characters.
        country_str=key[0:24]
        print("{:<25s}{:>20,d}{:>16,d}".format(country_str, data[key][0], data[key][1]))
        total_diabetes=total_diabetes+data[key][0]
        total_population=total_population+data[key][1]
    print()
    print("{:<25s}{:>20,d}{:>16,d}".format("TOTAL", total_diabetes, total_population))

    return None

def prepare_plot(data):
    '''
    Extract some useful data from a dictionary and return them.
    :param data: A dictionary for a specific region.
    :return Returns a new dictionary with the age group and gender as its keys.
    '''
    #print(data)
    plot_data_dict={}
    for country in data:
        for age in data[country]:
            if not age  in plot_data_dict:
                plot_data_dict[age]={}
            for lis in data[country][age]:
                gender=lis[0].upper()
                if not gender  in plot_data_dict[age]:
                    plot_data_dict[age][gender]=0
                plot_data_dict[age][gender]=plot_data_dict[age][gender]+lis[2]

    return plot_data_dict


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
    file_content_dic=create_dictionary(fp)
    while 1:         #Loop until user input quit.
        print(MENU)
        region_code_str=input("Enter region code ('quit' to terminate): ")
        region_code_str=region_code_str.upper()
        if region_code_str.upper()=="QUIT":
            break
        if  not region_code_str.upper()  in REGIONS:
            print("Error with the region key! Try another region")
            continue
        region_str = REGIONS[region_code_str]
        region_dict=file_content_dic[region_code_str.upper()]
        country_total_dict=get_country_total(region_dict)
        display_table(country_total_dict,region_code_str)
        flag=1
        while flag:                      #Loop until user input "yes" or no.
            yes_or_no=input("Do you want to visualize diabetes prevalence by age group and gender (yes/no)?: ")
            if yes_or_no=="yes":
                prepare_plot_data=file_content_dic[region_code_str.upper()]
                data_to_plot = prepare_plot(prepare_plot_data)
                plot_data("PIE", data_to_plot,
                          'Diabetes prevalence in ' + region_str + " by Age Group and Gender")
                plot_data("BAR", data_to_plot,
                          'Diabetes prevalence in ' + region_str + " by Age Group and Gender")
                flag=0
            elif yes_or_no=="no":
                flag=0
            else:
                print("Incorrect Input! Try Again!")



###### Main Code ######
if __name__ == "__main__":
    main()