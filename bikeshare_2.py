
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input('Enter City name:\n>').lower()
            try:
                if city in CITIES:
                    break
                else:
                    raise ValueError
            except:
                print("Please enter a Valid City Name from the following: chicago, new york city, washington\n>")      
            
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month name Or enter all to display the entire year statistics:\n>').lower()
        try:
            if month in MONTHS:
               break
            elif month == "all".lower():
               break 
            else:    
                raise ValueError
        except:
            print("Please enter a Valid Month Name such as: january, february, ... , june\nOr enter all to display the entire year statistics\n>")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day name Or enter all to diplay entire month statistics:\n>').lower()
        try:        
            if day in DAYS:
                break
            elif day == "all":
                break
            else:
                raise ValueError
        except:
            print("Please enter a valid day name such as: monday, tuesday, ... sunday\nOr enter all to diplay entire month statistics")
    print('-'*40)
    return city, month, day

            

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        df = df[ df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # display the most common month
    
    popular_month = df['month'].mode()[0]
    print("Most common month: " , popular_month)

    # display the most common day of week
    
    
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week: ", popular_day)
    
    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Common start hour: " , popular_hour)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start Station: " , popular_start_station)
    # display most commonly used end station
    popular_End_station = df['End Station'].mode()[0]
    print("Most common End Station: " , popular_End_station)

    # display most frequent combination of start station and end station trip
    df['combination_of_stations'] = "From station>> " + df['Start Station']+ " \nTo station>> "+df['End Station']
    popular_combination_of_stations = df['combination_of_stations'].mode()[0]
    
    print("Most common Trip:\n" , popular_combination_of_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Travel_Time']= df['End Time'] - df['Start Time']
    Total_Travel_Time = df['Travel_Time'].sum()
    print('Total_Travel_Time: ' , Total_Travel_Time)
    # display mean travel time
    Average_Travel_Time = df['Travel_Time'].mean()
    print('Average travel time: ' , Average_Travel_Time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types= df['User Type'].value_counts()
    print('Number of users per type: \n' , user_types)

    # Display counts of gender
    while True:
        try:
            gender_type= df['Gender'].value_counts()
            print('Number of users per gender:\n' , gender_type)
            break
        except:
            print("No Gender Data found!")
            break
    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            Min_birth = df['Birth Year'].min()
            Max_birth = df['Birth Year'].max()
            Common_birth = df['Birth Year'].mode()[0]
            print('Earliset birth year: ', Min_birth)
            print('Most recent birth year: ', Max_birth)
            print('Most common birth year: ', Common_birth)
            break
        except:
            print("No Birth Year Data found!")
            break
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays row data form the selcted data frame"""
    start_time = time.time()
    
    
    Answer = ['yes', 'no']
    row_table = ''
    
    counter = 0
    while row_table not in Answer:
        print("Do you wish to view the raw data? Enter yes or no.\n>")
        
        row_table = input().lower()
        #the raw data from the df is displayed if user opts for it
        if row_table == "yes":
            print(df.head())
        elif row_table not in Answer:
            print("Please check your input.")
            print("Input does not seem to match any of the accepted responses.")
            

    
    while row_table == 'yes':
        print("Do you wish to view more raw data? Enter yes or no.\n>>")
        counter += 5
        row_table = input().lower()
        
        if row_table == "yes":
             print(df[counter:counter+5])
        elif row_table != "yes":
             break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('Would you like to restart? Enter yes or no.\n<<>>')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
