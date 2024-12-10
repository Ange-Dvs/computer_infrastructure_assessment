# importing libaries needed for use within the functions
import matplotlib.pyplot as plt

def colours_for_pie(counted_cardinalWindDirection, counted_weather_descriptions): # function which handles deciding how many unique colours are needed for the pie chart depending on the length of the counted_weather_descriptions vs counted_cardinalWindDirection
    colormap = plt.colormaps['tab20'] # generating colours using 'tab20' colormap as it contains 20 unique colours to avoid having colours repeated in pie chart
    if len(counted_cardinalWindDirection) > len(counted_weather_descriptions): # if/else statement to ensure no colours are repeated using by first comparing the length of the two variables and ensuring the longer len value is used to set the number of colours
        colours_to_use = [colormap(i / len(counted_cardinalWindDirection)) for i in range(len(counted_cardinalWindDirection))]
        #print(f'colour weather') used for testing if the if else statement was working correctly
    else:
        colours_to_use = [colormap(i / len(counted_weather_descriptions)) for i in range(len(counted_weather_descriptions))]
        #print(f'colour weather') used for testing if the if else statement was working correctly
    return colours_to_use

def check_common_wind_direction(df): # function called to find the most common cardinal wind direction for the day and return full word instead of initials 
    wind_direction = df['cardinalWindDirection'].mode()[0]

    if wind_direction == 'N':
        most_common_wind_direction = 'North'

    elif wind_direction == 'NW':
        most_common_wind_direction = 'Northwest'

    elif wind_direction == 'NE':
        most_common_wind_direction = 'Northeast'

    elif wind_direction == 'E':
        most_common_wind_direction = 'East'

    elif wind_direction == 'SE':
        most_common_wind_direction = 'Southeast'

    elif wind_direction == 'S':
        most_common_wind_direction = 'South'

    elif wind_direction == 'SW':
        most_common_wind_direction = 'Southwest'

    elif wind_direction == 'W':
        most_common_wind_direction = 'West'

    else: # else statement added in case any unconsidered values are the most common in a file 
        most_common_wind_direction =  wind_direction # if the value for the wind direction doesn't match one of the conditions above the function passes back the most commonly occurring value as it is displayed in the file

    return most_common_wind_direction 

def classifying_temperature (df): # function checking the average temperature of the day and classifying it with a general description 
    # determining the average temperature of the day
    av_temp = df['temperature'].mean()

    #print(av_temp) used for testing the temperature classification.

    if av_temp <= 0:
        temp_classification = 'Freezing day'

    elif av_temp >= 1 and av_temp <= 13:
        temp_classification = 'Cold day'

    elif av_temp >= 14 and av_temp <= 20:
        temp_classification = 'Cool day'

    elif av_temp >= 21 and av_temp <= 23:
        temp_classification = 'Warm day'

    else:
        temp_classification = 'Hot day'
    
    return temp_classification
