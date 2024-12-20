# computer_infrastructure_assessment
Repository for Semester 2 Computer Infrastructure assessment

## Installation & Usage Instructions

### Clone the repository from GitHub

1. Copy the following URL:
https://github.com/Ange-Dvs/computer_infrastructure_assessment.git

1. Open CMDER or if using VS Code open the terminal pane

1. Navigate to the folder where you want to clone the repository to on your machine and type git pull
``git clone`` https://github.com/Ange-Dvs/computer_infrastructure_assessment.git

1. Set merge as the mode for the pull
``git config pull.rebase false``

1. Initiate the pull of the GitHub repository
``git pull``

If the pull has been successful, you should see   
- ``.github`` directory 
- ``weather-data.yml``
- ``data`` directory 
- ``timestamps`` sub-directory 
- ``weather`` sub-directory
- ``images`` directory
- ``myfunctions.py`` file
- ``README.md`` file
- ``.gitignore`` file
- ``requirements.txt`` file
- ``weather.ipynb`` notebook
- ``weather.sh`` script

### Install dependencies

Ensure you have Python installed and the required libraries. 
Dependencies can be installed using the ``requirements.txt`` file by running the below command either in the command line or in the terminal in VS Code.
``pip install -r requirements.txt``

The libraries can also be installed individually as specified in the ``weather.ipynb`` notebook.

### Run the Notebook

1. Launch Jupyter Notebook on your system and navigate to ``weather.ipynb`` file in the directory and open it.
1. Execute the cells sequentially, by clicking **Run all**. This will load the weather dataset, render the markdown cells and generate the plots.

If any errors occur, check your dependencies and ensure all libraries are installed correctly.

## GitHub Codespaces

For the automation of the ``weather.sh`` script GitHub Codespaces was used.  

## Dependencies

## Dataset

The data used for the weather.ipynb notebook originates from a platform owned by Met Éireann.  
Met Éireann runs various weather stations across the country, the data used in this project comes from their Athenry location.  
The data is downloaded using their API to download the data in ``.json`` format.  
The file is then read into the notebook to be analysed using the ``pandas`` function ``read_json()``.  

## Walkthrough of code

### Functions created

``def colours_for_pie(counted_cardinalWindDirection, counted_weather_descriptions)``
This function handles deciding how many unique colours are needed for the pie chart depending on the length of the ``counted_weather_descriptions`` vs ``counted_cardinalWindDirection``. This is done to avoid issues with colours repeating in the pie chart if one of the charts has a larger amount of slices than the other. 

``colormap = plt.colormaps['tab20']``
The colours to use are generated using the ``tab20`` colormap. This contains 20 unique colours to avoid having colours repeated in pie chart. 
    
``if len(counted_cardinalWindDirection) > len(counted_weather_descriptions):``
An if/else statement is used to determine the length of the two variables separately. The variables are then compared to see which one is longer to ensure no colours are repeated. 

``colours_to_use = [colormap(i / len(counted_cardinalWindDirection)) for i in range(len(counted_cardinalWindDirection))]``
First an empty list is created, ``i`` is used to loop through a range as long as the length of the ``counted_cardinalWindDirection``. The iteration number is divided by the length of the variable, in the above code snippet this is the counted_cardinalWindDirection. This value is then mapped to a specific colour. After the for loop has completed the empty list will contain the colours to be used for the pie chart. 


``def check_common_wind_direction(data)``
This function is used to return the full word for the most common cardinal wind direction for the day instead of just the initials recorded in the ``.json`` file.

``wind_direction = data['cardinalWindDirection'].mode()[0]``
The ``cardinalWindDirection`` column is checked in this step for the dataset specified when the function is called. The most common value in the data is then found using ``.mode()``, ``[0]`` refers to the index to be used to locate which value to pull as 0 is the first value in a Series.

``if wind_direction == 'N': most_common_wind_direction = 'North'``
The next section of the function uses ``if``, ``elif`` and ``else`` statements to determine what value matches the mode and then set a string to the ``most_common_wind_direction`` variable.  This value is then returned to the notebook. 

``def preprocess_data(data, rename_columns, numeric_fields, date_col, datetime_format)``
Function to take in the datasets and prepare the data to be used for various calculations 

``if rename_columns is not None:
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
    plt.figure(figsize=(10, 6))

    for i, df in enumerate(datasets):
        if column_name not in df.columns:
            print(f'Warning: "{column_name}" not found in DataFrame {i+1}. Skipping.')
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

def stats_single_field(dataset, field, unit):
    max_value = dataset[field].max()
    max_times = dataset[dataset[field] == max_value].index
    max_value_times_formatted = [time.strftime('%H:%M') for time in max_times]

    min_value = dataset[field].min()
    min_times = dataset[dataset[field] == min_value].index
    min_value_times_formatted = [time.strftime('%H:%M') for time in min_times]

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


### Cleaning the data 

During testing of the notebook it was seen that occasionally there would be missing data in the ``.json`` file, which is not uncommon when using real data.  
The way in which the missing entries were shown was inconsistent with blank values sometimes being represented as empty quotation marks or by using a hyphen.  

From a review of the ``.json`` file it appeared that the empty quotation marks were how the blank entries in a text field was represented while the hyphen appeared to be used for the cases where the a numeric value would be expected. The blank string fields would cause issues when generating the various plots. The "-" string being in place instead of a numeric value in some fields would cause issues when attempting to do calculations where a numeric value would be expect.  

Examples of occurrences of malformed or missing data:  
![Example of empty field with empty quotation marks](images/blank_empty_value_quotations.png)   
![Example of empty field with empty hyphen](images/blank_empty_value_hyphen.png)    

To avoid this at the beginning of the notebook the data is checked and corrected to avoid issues in calculations when the cells are executed.  
The fields which are used for calculations are specified in a variable called ``numeric_field_to_convert``.  
This variable is then used to cycle through these values in the DataFrame for each field and convert the field to a numeric data type.  
If a string is in place of a numeric value, for example the hyphen shown in the screenshot above an error is thrown.  
With this, ``errors='coerce'`` is used to take any values causing an error and change the value of the field for that entry to NaN to avoid issues.

After this the entire dataset is check for the occurrence of empty quotation marks in a field. This is then also replaced with NaN using ``numpy.nan`` with ``inplace`` set to ``True``.  

## Historical data 
ATHENRY
date:Date and Time (utc)
rain:Precipitation Amount (mm)
temp:Air Temperature (C)
rhum:Relative Humidity (%)
wdsp:Mean Wind Speed (kt)
wddir:Predominant Wind Direction (deg)
msl:Mean Sea Level Pressure (hPa) (pressure) 


## Additional resources & reading

### Libraries used

Within the project various external libraries are used including: 

- ``Pandas``
- ``Matplotlib.pyplot``
- ``Seaborn``
- ``Matplotlib.dates``
- ``NumPy``


###

chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cli.fusio.net/cli/stormcenter/PDF/Elin.pdf > storm elin 2023
https://www.met.ie/climate/climate-of-ireland#:~:text=It's%20a%20zone%20of%20transition,typical%20of%20the%20Irish%20climate.

plt.colormaps['tab20']`` function
range(len(
    ``.mode()``
enumerate()
idxmin()
.strftime('%H:%M')
.abs()
https://seaborn.pydata.org/generated/seaborn.heatmap.html
https://seaborn.pydata.org/generated/seaborn.pairplot.html
https://seaborn.pydata.org/tutorial/distributions.html#kernel-density-estimation
https://seaborn.pydata.org/generated/seaborn.histplot.html
https://seaborn.pydata.org/generated/seaborn.kdeplot.html
https://www.analyticsvidhya.com/blog/2023/12/mastering-tabulate/
https://stackoverflow.com/questions/70630387/saving-functions-into-package-in-jupyter-notebooks
https://www.w3schools.com/python/pandas/ref_df_describe.asp
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc
https://www.codecademy.com/resources/docs/pandas/dataframe/loc





### External resources links
https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas-read-json
https://www.w3schools.com/python/pandas/pandas_json.asp
https://www.geeksforgeeks.org/visualizing-json-data-in-python/
https://scales.arabpsychology.com/stats/how-do-i-combine-two-date-and-time-columns-into-one-in-a-pandas-dataframe/
https://sparkbyexamples.com/pandas/pandas-drop-last-column-from-dataframe/#:~:text=To%20drop%20the%20last%20column,pop()%20%2C%20and%20del%20functions.
https://stackoverflow.com/questions/45196965/pandas-drop-last-column-of-dataframe
https://matplotlib.org/stable/users/explain/colors/colormaps.html#qualitative
https://matplotlib.org/stable/api/dates_api.html#matplotlib-dates
https://matplotlib.org/stable/api/dates_api.html#date-formatters