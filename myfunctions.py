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

def preprocess_data(data, rename_columns, numeric_fields, datetime_format): # function to take in the datasets prepare the data to be used for various calculations 

    if rename_columns is not None: # converting date column to datetime skipping for 2024 df as ths is done outside of the function
        data['datetime'] = pd.to_datetime(data['date'], format=datetime_format, errors='coerce')
        #data['datetime'] = data['datetime'].dt.strftime('%Y-%m-%d')
        data.rename(columns=rename_columns, inplace=True) # renaming the columns of the dataset
        # converting date column to datetime and set as index
        data.set_index(data['datetime'], inplace=True, drop=True)
        # removing duplicated datetime column if it's still there after setting the datetime as the index
        if 'datetime' in data.columns:
            data.drop(columns=['datetime'], inplace=True)
    
    else:

        # Split the date column into parts
        data['date'] = data['date'].astype(str)
        parts = data['date'].str.split('-', expand=True)
        # Rearrange the parts to create the desired format
        data['formatted_date'] = parts[0] + '-' + parts[2] + '-' + parts[1]
        data['datetime'] = pd.to_datetime(data['formatted_date'].astype(str) + ' ' + data['reportTime'].astype(str)) # merging the date and reportTime columns from the .json file as strings and converting to a pandas datetime series to enable it to be used as the index for the DataFrame
        # converting date column to datetime and set as index
        # removing duplicated unneccessary columns
        data.set_index(data['datetime'], inplace=True, drop=True)
        data = data.drop((['reportTime', 'date', 'formatted_date']),axis =1) 
        if 'datetime' in data.columns:
            data.drop(columns=['datetime'], inplace=True)
      

    for col in numeric_fields: # cycling through the dataset to ensure fields are of dtype 
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # replacing empty strings with NaN
    data.replace("", np.nan, inplace=True)

   

    return data

def get_mean_min_max(field, datasets, years,unit): # calculating the mean, min and max of a value depending on the field passed into the function
    print(f'{field.capitalize()} in {unit}\n')
    print(f'{'Year':<5} {'Mean':<9} {'Min':<9} {'Max':<9}') # info is displayed in a table like view, the alignment and width is set by defining the number of characters space for the headers after the '<' symbol
    print('-' * 35)
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

        print(f'{year:<6}{mean_val:<10.2f}{min_val:<10.2f}{max_val:<10.2f}') # results are printed in the Jupyter notebook for the user
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
    # setting the size of the plot
    plt.figure(figsize=(10, 6))

    # iterating over each dataset in the list
    for i, df in enumerate(datasets):
        # checking if the column exists in the current DataFrame
        if column_name not in df.columns:
            print(f'Warning: "{column_name}" not found in DataFrame {i+1}. Skipping.')
            continue
        # If labels are provided, assign the current label to the line plot
        if labels and i < len(labels): 
            label= labels[i]
            plt.plot(df.index.hour, df[column_name], marker='o', linestyle='-', label=label)
    # setting the labels, title, legend, adding a grid and showing the plot
    plt.xlabel('Time (24 hr clock)')
    plt.ylabel(f'{column_name.capitalize()}')
    plt.title(f'{column_name.capitalize()} across the years', y=1.1, fontsize=16)
    plt.legend(loc='upper center', bbox_to_anchor = (0.5, 1.10), ncols = 5)
    plt.grid(True)
    plt.show()

def stats_single_field(dataset, field, unit):
    # finding the maximum value in the field and the corresponding times
    max_value = dataset[field].max()
    max_times = dataset[dataset[field] == max_value].index
    max_value_times_formatted = [time.strftime('%H:%M') for time in max_times]

    # finding the minimum value in the field and the corresponding times
    min_value = dataset[field].min()
    min_times = dataset[dataset[field] == min_value].index
    min_value_times_formatted = [time.strftime('%H:%M') for time in min_times]

    # calculating the range of values (max - min), average and rate of change for the field
    full_range = max_value - min_value

    avg_field = dataset[field].mean()

    dataset[f'{field}_rate_of_change'] = dataset[field].diff()

    av_rate_change = dataset[f'{field}_rate_of_change'].mean()
    largest_change_rate = dataset[f'{field}_rate_of_change'].abs().max()

    # printing the time of max, min and temperature range for the day
    print(f'Highest {field.capitalize()}:\t\t {max_value}{unit} at {', '.join(max_value_times_formatted)}')
    print(f'Lowest {field.capitalize()}:\t\t {min_value}{unit} at {', '.join(min_value_times_formatted)}')
    print(f'Average {field.capitalize()}:\t\t {avg_field:.2f}{unit}')
    print(f'Range for day:\t\t\t {max_value}{unit} - {min_value}{unit} = {full_range}{unit}')
    print(f'Average hourly rate of change:\t {av_rate_change:.2f}{unit}')
    print(f'Largest rate of change was:\t {largest_change_rate:.2f}{unit}')