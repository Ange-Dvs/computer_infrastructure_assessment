# computer_infrastructure_assessment
Repository for Semester 2 Computer Infrastructure assessment

## Installation

## Usage

## Dependancies

## External resources links
https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas-read-json
https://www.w3schools.com/python/pandas/pandas_json.asp
https://www.geeksforgeeks.org/visualizing-json-data-in-python/
https://scales.arabpsychology.com/stats/how-do-i-combine-two-date-and-time-columns-into-one-in-a-pandas-dataframe/
https://sparkbyexamples.com/pandas/pandas-drop-last-column-from-dataframe/#:~:text=To%20drop%20the%20last%20column,pop()%20%2C%20and%20del%20functions.
https://stackoverflow.com/questions/45196965/pandas-drop-last-column-of-dataframe
https://matplotlib.org/stable/users/explain/colors/colormaps.html#qualitative
https://matplotlib.org/stable/api/dates_api.html#matplotlib-dates
https://matplotlib.org/stable/api/dates_api.html#date-formatters

## Cleaning the data 

During testing of the notebook it was seen that occasionally there would be missing data in the ``.json`` file. 
The way in which the misisng entry was inconsistent with blank values sometimes being represented as empty quotation marksor the blank field is representing using a hyphen.  

From a review of the .json file it appeared that the empty quotation marks were how the blank entries in a text field was represented while the hyphen appeared to be used for the cases where the a numeric value would be expected.  

The blank string fields would cause issues when ploting the pie chart for the wind direction throughout the day.  
The string being in place instead of a numeric value in some fields would cause issues when attempting to do calculations where a numeric value would be expect.  

Examples of occurances of malformed or missing data:
![Example of empty field with empty quotation marks](images/blank_empty_value_quotations.png) 
![Example of empty field with empty hyphen](images/blank_empty_value_hyphen.png)  

To avoid this at the beginning of the notebook the data is checked and corrected to avoid issues in calculations throughtout the project. 

The fields which are used for calculations are specified in a variable called "numeric_field_to_convert" is defined and used to cycle through these values in the dataframe for each field and convert the field to a numeric dtype.  
If a string is in place of a numeric value, for example the hyphen shown in the screenshot above and error is thrown.  
With this, ``errors='coerce'`` is used to take any values causing an error and change the value of the field for that entry to NaN to avoid issues.

After this the entire dataset is check for the occurance of empty quotation marks in a field. This is then also replaced with NaN using ``numpy.nan`` with ``inplace`` set to ``True``.  