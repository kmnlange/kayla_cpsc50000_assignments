'''
Kayla Lange
2/21/2026
population_explorer.py

Description:
A menu-driven program that reads a CSV file of world population data,
stores the data in a list of dictionaries, and allows users to perform a
case-insensitive country search, view the top and bottom five countries by
2024 population using built-in sorting, and generate a dictionary-based
report of countries grouped by their starting letter. The program runs
until the user chooses to exit.
'''
import csv
from pathlib import Path

def get_csv_path_from_user():   #User input for file
    print("\n-----Welcome to the Population Explorer Tool-----\n") 

    while True:
        file = input("\nPlease enter the full path and  name of the text file to begin (example.txt):\n")

        path = Path(file)

        if path.is_file(): return path
        else:
            print("\nFile does not exist. Please try again." \
                  "\nAn example of the file pathway is: C:\\Users\\username\\Documents\\file.txt\n") 

def display_menu():     #Menu Options
    print('\n-----Population Explorer-----\n')
    print('s -- Search by Country Name')
    print('t -- List Top 5 Countries by 2024 Population')
    print('b -- List Bottom 5 Countries by 2024 Population')
    print('r -- View Countries by First Letter Report')
    print('x -- Exit the Program')

def would_you_like_to_continue():   # To repeat or not to repeat
        user_input = input('\nSearch another country? y/n ').lower()
        if user_input == 'y': return True
        else: return False
        
def bool_to_yes_no(boolean_value):
    if boolean_value: return "Yes"
    else: return "No"
    
def load_rows(path): #Reads file and returns list of countries and their associated values
    countries = []

    with open(path, 'r') as file:
        read_file = csv.DictReader(file)

        try:
            for row in read_file:
                countries.append({'country': row['country'].strip().casefold(),
                              'country_id': row['TwoLetterID'],
                              'un_membership_status': bool_to_yes_no(row['unMember']),
                              'population_in_2024': int(row['pop2024']),
                              'land_area_km': float(row['landAreaKm']),
                              'world_percentage_2024': float(row['2024WorldPercentage'])})  
            return countries

        except Exception as e:
            print(f'oops--we have an error with the file. \n The error is {e}')

def linear_search_country(countries, country_name): #Searches List of countries based on user input
        for country in countries:
            if country['country'] == country_name:
                return country
            else: continue 
        return None
            
            

def print_country_details(countries): #Prints country details
    while True:
        country_name = input('\nPlease Enter the Name of the Country you would like to Search: ').strip().casefold()

        search = linear_search_country(countries, country_name)
        
        if search is not None:
            print(f"\nHere are some details about {search['country'].capitalize()}:\n")
            print(f"Country ID: {search['country_id'].upper()}")
            print(f"UN Membership Status: {search['un_membership_status'].capitalize()}")
            print(f"Population in 2024: {search['population_in_2024']:,}")
            print(f"Land Area(Km): {search['land_area_km']:,}")
            print(f"2024 World Perecentage: {search['world_percentage_2024']:.2%}")
        else:
            print(f'\nCountry Name: {country_name} is not found.') 

        if would_you_like_to_continue() == False: break
    
def print_top_n(countries): #Sorts top 5 countries and prints them
    sorted_countries = sorted(countries, key = lambda countries: countries['population_in_2024'], reverse=True)
    print('\nThe top 5 most populated countries are: \n')
    for country in sorted_countries[:5]:
        print(f"          {country['country'].capitalize()} - {country['population_in_2024']:,}")

    input('\nPress Enter to Continue: \n')

def print_bottom_n(countries): 
    sorted_countries = sorted(countries, key = lambda countries: countries['population_in_2024'])
    print('\nThe top 5 least populated countries are: \n')

    for country in sorted_countries[:5]:
        print(f"{country['country'].capitalize()} - {country['population_in_2024']:,}")

    input('\nPress Enter to Continue: \n')

def build_letter_counts(countries):
    countries_by_first_letter = {}
    
    for country in countries:
        letter = country['country'][0]

        if letter not in sorted(countries_by_first_letter):
            countries_by_first_letter[letter] = 0
        
        countries_by_first_letter[letter] += 1
        
    return countries_by_first_letter
    
def print_letter_counts(countries_by_first_letter):
    print('\nThe number of countries that start with a given letter:\n')

    for letter in sorted(countries_by_first_letter):
        print(f'{letter.upper()} - {countries_by_first_letter[letter]}')

    input('\nPress Enter to Continue: \n')

def main_menu_loop(): 
    path = get_csv_path_from_user()
    countries = load_rows(path)
    countries_by_first_letter = build_letter_counts(countries)

    while True:
        display_menu()
        menu_option = input('\nSelect an Option>> ').strip().casefold()

        if menu_option == 's': print_country_details(countries)
        if menu_option == 't': print_top_n(countries)
        if menu_option == 'b': print_bottom_n(countries)
        if menu_option == 'r': print_letter_counts(countries_by_first_letter)
        if menu_option == 'x': break

if __name__=='__main__':
    main_menu_loop()

    print("\nThank you for using the Population Explorer Tool. Goodbye!")

'''
End
'''