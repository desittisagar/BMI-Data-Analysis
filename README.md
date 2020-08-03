# BMI-Data-Analysis
BMI Data Analysis of different countries


Data Analysis

Download this zip package ( https://doms.csu.edu.au/csu/file/8ecc7393-0664-44fc-8288- 8a5a29de687b/1/ITC558_202030_A3_dataset.zip ) which contains three dataset files: ‘life.csv’, ‘bmi_men.csv’ and ‘bmi_women.csv’. First file contains data about average life expectancy (in years) for most countries worldwide. Other two files contain data about men and women average Body Mass Index (BMI) for the same set of countries. These are plain text files with all data separated by commas. You can also open the files in a spreadsheet application to better understand their contents. All three files have a similar structure — first row contains the year headers and first column contains the country names. There is data about 186 countries for a period of 1980 to 2008.

Your program should perform the following steps.

    (1) Read all the data from files and save into a 2D list and two dictionaries.

The life expectancy data should be stored in the form of two dimensional list where the outer list has 186 elements. Each inner list contains data for specific countries.

The BMI data from both files should be stored in two dictionaries which map country names to a list of data values. Both dictionaries will contain 186 keys, with each key associated with a list of 29 values (BMI data from 1980 to 2008).

Following diagram illustrates the required data structures. Note that all numbers have been converted from string to float data types.



You should use these collections for the next five steps — do not read the files again.
