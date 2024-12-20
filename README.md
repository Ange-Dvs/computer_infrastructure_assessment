# computer_infrastructure_assessment
This repository contains the code and documentation for my Weather Analysis Notebook. The notebook was created as part of the Semester 2 Computer Infrastructure Assessment, focusing on analysing and visualizing weather data collected from Met Éireann's Athenry weather station.

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
The notebook uses the following Python libraries:

- ``Pandas``
- ``NumPy``
- ``Matplotlib``
- ``Seaborn``

Install these via the requirements.txt file.

## Dataset

The data used for the weather.ipynb notebook originates from a platform owned by Met Éireann.  
Met Éireann runs various weather stations across the country, the data used in this project comes from their Athenry location.  
The data is downloaded using their API to download the data in ``.json`` format.  
The file is then read into the notebook to be analysed using the ``pandas`` function ``read_json()``.  

## Walkthrough of code

### 1. Setup and Configuration
Imports: Libraries like ``Pandas``, ``NumPy``, ``Matplotlib``, and ``Seaborn`` are imported here.
Custom Functions: Utility functions like clean_data or plot_heatmap are loaded from myfunctions.py.

### 2. Data Loading
Dataset: The ``.json`` file is read into a pandas DataFrame.
Preview: The first few rows of the dataset are displayed to understand its structure and check for immediate issues.

### 3. Data Cleaning
Replacing Missing Values: Converts invalid entries into NaN for easier handling.
Data Type Conversions: Ensures numeric columns are properly formatted for analysis.

### 4. Exploratory Data Analysis
Descriptive Statistics: Uses ``.describe()`` to get key metrics for numeric fields.
Initial Visualizations: Quick plots to identify trends and anomalies.

### 5. Visualization Creation
Heatmaps: Correlation analysis to see how variables relate.
Line Graphs: Show trends in temperature, rainfall, or wind speed over time.

### 6. Conclusion and Findings
Summary: Key insights from the analysis are highlighted.
Next Steps: Suggestions for further analysis or improvements.

### **Functions Summary**

#### ``colours_for_pie``
Determines the appropriate number of unique colours for a pie chart based on the lengths of the `counted_cardinalWindDirection` and `counted_weather_descriptions` variables. Uses the `tab20` colormap to ensure distinct, non-repeating colours.

#### ``check_common_wind_direction``
Finds the most common cardinal wind direction in the dataset and converts its abbreviation into the full word, for example N to North.

#### ``preprocess_data``
Prepares the dataset for analysis by:
- Renaming columns specified when calling the function.
- Converting specified fields to numeric types.
- Replacing empty strings with `NaN`.
- Converting a date column into a datetime format and setting it as the index.

#### ``get_mean_min_max``
Calculates and prints the mean, minimum and maximum values for a specified field across multiple datasets. Displays the results in a formatted table for clarity.

#### ``line_plot_overview``
Generates a line plot for a selected column in the dataset. Formats the x-axis to display dates and times for improved readability.

#### ``plot_column``
Creates a plot for a specific column from multiple datasets, showing values against a 24-hour time format. Handles missing columns gracefully and supports customizable labels.

#### ``stats_single_field``
Calculates and prints detailed statistics for a specific field in the dataset, including:
- Maximum and minimum values (with the times recorded).
- The range of values for the day.
- The average hourly rate of change.
- The largest observed rate of change.

## Additional resources & reading

### Libraries used

The notebook makes extensive use of the following Python libraries. Below is a brief introduction to each, followed by the specific methods and functions utilized:
- ``Pandas``
- ``Matplotlib.pyplot``
- ``Seaborn``
- ``Matplotlib.dates``
- ``NumPy``

<font size="4"><b>Pandas</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Pandas` is a library in Python used for data analysis which enables the use of two-dimensional tables called DataFrames.  
Within the project the ``Pandas`` library is used to read in the data from the various ``CSV`` files.  
It is also used to convert date information in the ``CSV`` file to a datetime series.

>``.read_json()`` (Function): Reads a JSON file into a DataFrame.

>``.head()`` (Method): Displays the first few rows of the DataFrame.

>``.describe()`` (Method): Summarizes statistics of numerical columns.

> ``.to_datetime`` (Function) - Converts a string or other formats to a ``datetime`` object.  

>``.loc[]`` (Method): Accesses a group of rows and columns by labels or a Boolean array.

>``.isna()`` (Method): Detects missing values in the DataFrame.

>``.fillna()`` (Method): Fills missing values with a specified value or method.

<font size="4"><b>NumPy</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A library for numerical computing. It supports arrays and operations on them, as well as tools to handle missing or invalid data.

>``numpy.nan`` (Object): Represents missing values.

>``astype()`` (Method): Converts a DataFrame column to a specified data type.

<font size="4"><b>Matplotlib</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A library for creating visualizations in Python. It is the foundation for many other visualization libraries.

>``plt.plot()`` (Function): Creates a line plot.

>``plt.xlabel()`` and ``plt.ylabel()`` (Functions): Sets labels for x and y axes.

>``plt.title()`` (Function): Adds a title to the plot.

>``plt.show()`` (Function): Displays the plot.

>``matplotlib.dates.DateFormatter`` (Class): Formats datetime axes in plots.

>``matplotlib.dates`` (Module): Provides tools for manipulating and formatting datetime data in plots.

<font size="4"><b>Seaborn</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A Python visualization library built on matplotlib, designed for making statistical graphics easier to create and interpret.

>``sns.heatmap()`` (Function): Creates a heatmap for visualizing correlations.[^]

>``sns.histplot()`` (Function): Generates a histogram for data distribution.

>``sns.pairplot()`` (Function): Produces pairwise scatterplots and KDE.[^]

>``sns.lineplot()`` (Function): Creates a line plot with additional styling options.


### **References and Resources**

During the creation of the project a number of various online resources and documentation we used as background for the analysis, visualisation, and understanding of weather data. Below is a list of the references, along with a brief explanation of the information within:

#### **Pandas Documentation**
- [pandas.read_json](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas-read-json)  
  Used for loading JSON weather data into a DataFrame for analysis.  

- [pandas.DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)  
  Used to compute summary statistics for numerical fields.

- [pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc)  
  Used to filter and access specific rows and columns in the DataFrame.  

---

#### **Data Cleaning and Manipulation**
- [W3Schools - Handling JSON in Pandas](https://www.w3schools.com/python/pandas/pandas_json.asp)  
  Served as a guide for handling JSON data in Pandas efficiently.  

- [Combining Date and Time Columns in Pandas](https://scales.arabpsychology.com/stats/how-do-i-combine-two-date-and-time-columns-into-one-in-a-pandas-dataframe/)  
  Used for combining `date` and `reportTime` into a single datetime column.  

- [Drop Last Column from DataFrame](https://sparkbyexamples.com/pandas/pandas-drop-last-column-from-dataframe/)  
  Helped in understanding how to drop unnecessary columns during pre-processing.

---

#### **Matplotlib and Seaborn Visualization**
- [Matplotlib - Colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#qualitative)  
  Used for selecting colormaps to ensure distinct colours in visualizations.  

- [Matplotlib Dates API](https://matplotlib.org/stable/api/dates_api.html#matplotlib-dates)  
  Provided guidance on formatting and customizing date axes in plots.  

- [Seaborn Heatmap Documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html)  
  Used for creating heatmaps to visualize correlations in weather data.  

- [Seaborn Pairplot Documentation](https://seaborn.pydata.org/generated/seaborn.pairplot.html)  
  Helped generate scatterplots to examine relationships between variables.

---

#### **Weather Science**
- [NCAS - What Causes Weather?](https://ncas.ac.uk/learn/what-causes-weather/#:~:text=the%20earth%E2%80%99s%20temperature)  
  Provided insight into atmospheric pressure and its relationship to weather.  

- [Interpreting Weather Charts](https://www.rmets.org/metmatters/how-interpret-weather-chart)  
  Served as a reference for understanding weather data and pressure systems.  

- [Beaufort Wind Scale](https://www.rmets.org/metmatters/beaufort-wind-scale)  
  Used to understand wind speed classifications and their impact on weather.

---

#### **Climate and Meteorological Data**
- [Met Éireann Climate Data](https://www.met.ie/climate/available-data/monthly-data)  
  Source of historical weather data for the Athenry station.  

- [Storm Barra Report (2021)](https://cli.fusio.net/cli/stormcenter/PDF/Barra.pdf)  
  Reviewed as an example of detailed storm documentation.  

- [Climate of Ireland](https://www.met.ie/climate/climate-of-ireland#:~:text=It's%20a%20zone%20of%20transition)  
  Provided a summary of Ireland's climate for context in analysis.

---

#### **Additional Tutorials**
- [Saving Functions in Jupyter](https://stackoverflow.com/questions/70630387/saving-functions-into-package-in-jupyter-notebooks)  
  Used for organizing helper functions into reusable modules.  

- [Visualizing JSON Data in Python](https://www.geeksforgeeks.org/visualizing-json-data-in-python/)  
  Helped in understanding how to visualize JSON-formatted weather data.  

---
# End 

