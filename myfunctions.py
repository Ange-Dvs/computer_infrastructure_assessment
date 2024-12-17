# importing libaries needed for use within the functions
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.dates as mdates


def colours_for_pie(counted_cardinalWindDirection, counted_weather_descriptions): # function which handles deciding how many unique colours are needed for the pie chart depending on the length of the counted_weather_descriptions vs counted_cardinalWindDirection
    colormap = plt.colormaps['tab20'] # generating colours using 'tab20' colormap as it contains 20 unique colours to avoid having colours repeated in pie chart
    if len(counted_cardinalWindDirection) > len(counted_weather_descriptions): # if/else statement to ensure no colours are repeated using by first comparing the length of the two variables and ensuring the longer len value is used to set the number of colours
        colours_to_use = [colormap(i / len(counted_cardinalWindDirection)) for i in range(len(counted_cardinalWindDirection))]
        #print(f'colour weather') used for testing if the if else statement was working correctly
    else:
        colours_to_use = [colormap(i / len(counted_weather_descriptions)) for i in range(len(counted_weather_descriptions))]
        #print(f'colour weather') used for testing if the if else statement was working correctly
    return colours_to_use

def check_common_wind_direction(data): # function called to find the most common cardinal wind direction for the day and return full word instead of initials 
    wind_direction = data['cardinalWindDirection'].mode()[0]

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

def classifying_temperature (data): # function checking the average temperature of the day and classifying it with a general description 
    # determining the average temperature of the day
    av_temp = data['temperature'].mean()

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

def preprocess_data(data, rename_columns, numeric_fields, date_col, datetime_format): # function to take in the datasets prepare the data to be used for various calculations 

    if rename_columns is not None:
        data.rename(columns=rename_columns, inplace=True) # renaming the columns of the dataset
    
    for col in numeric_fields: # cycling through the dataset to ensure fields are of dtype 
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # replacing empty strings with NaN
    data.replace("", np.nan, inplace=True)

    # converting date column to datetime and set as index
    data['datetime'] = pd.to_datetime(data[date_col], format=datetime_format, errors='coerce')
    data.set_index(data['datetime'], inplace=True)
    data.drop(['datetime', date_col], axis=1, inplace=True)

    return data

def get_mean_min_max(field, datasets, years): # calculating the mean, min and max of a value depending on the field passed into the function
    print(f"{'Year':<6} {'Mean':<10} {'Min':<10} {'Max':<10}") # info is displayed in a table like view, the alignment and width is set by defining the number of characters space for the headers after the '<' symbol
    print("-" * 35)
    results = []  # To store results
    for year, dataset in zip(years, datasets): # the years & datasets lists are cycled through and the mean, min and max are calculated
        mean_val = dataset[field].mean()
        min_val = dataset[field].min()
        max_val = dataset[field].max()

         # Append results to the list
        results.append({
            'year': year,
            'mean': mean_val,
            'min': min_val,
            'max': max_val
        })

        print(f"{year:<6}{mean_val:<10.2f}{min_val:<10.2f}{max_val:<10.2f}") # results are printed in the Jupyter notebook for the user
    return results

def line_plot_overview (selected_column, dataset24): # function created to generate a line plots when called at once to reduce repeated code throughout the notebook
    plt.figure(figsize=(10,2))
    sns.lineplot(data=dataset24, x=dataset24.index, y=selected_column)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M')) 
    plt.xlabel('Date & time')
    plt.ylabel(f'{selected_column.capitalize()}')
    plt.title(f'{selected_column.capitalize()}')
    plt.show()


def plot_column(datasets, column_name, labels):
    plt.figure(figsize=(10, 6))

    for i, df in enumerate(datasets):
        if column_name not in df.columns:
            print(f"Warning: '{column_name}' not found in DataFrame {i+1}. Skipping.")
            continue
        if labels and i < len(labels): 
            label= labels[i]
            plt.plot(df.index.hour, df[column_name], marker='o', linestyle='-', label=label)
            
    plt.xlabel('Time (24 hr clock)')
    plt.ylabel(f'{column_name.capitalize()}')
    plt.title(f'{column_name.capitalize()} across the years', y=1.1, fontsize=16)
    plt.legend(loc='upper center', bbox_to_anchor = (0.5, 1.10), ncols = 5)
    plt.grid(True)
    plt.show()














