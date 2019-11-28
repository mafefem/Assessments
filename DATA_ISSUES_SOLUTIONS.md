#------------------------------Data Issues---------------------------------------------#

The dirty file have the following issues comparing to the clean file
0. Columns were reorder.
1. The first name,last name, tran_date, value and tran_type  have some null values.
2. tran_value column was rename to value.
3. Gender contents was change to 'F' and 'M' values.
4. Date format was change mm/dd/yyy.
5. The field tran_value lost its decimal place of 2 to 6.
6. Cell tran_type has corrupted data.
7. Values in tran_status are 1-20 instead of 1-5


#-----------------------------Data Solutions------------------------------------------#
The solutions that need to be applied resolve data issues in a dirty file

1. We can use the column tran_status to filter status above 5 out from dirty file. Because status field look   like flag to categorize. In this case we will remove statuses not mapping to the clean file.

2. The columns need to be reorder to original state to make reading of the file easy when comparing to the clean file.

3. The decision need to be made about null values. 
	-We can drop null values from missing columns. We are going work with missing data, data analysis should be done check if data will not present baised results since data is missing.
	-None values can default to the known value for audit purpose. It will be a good to have stats about  missing values from colums. To see if there's a pattern in terms of them missing values.

4. The rename column need to be name as field  in clean file, if column is not will break model since model might be expecting tran_value instead of value.

5. Gender contents 'F' and 'M' must be chamge to its original state becuase they can all break the model if model expect male and single instead of 'F' and 'M' for mapping purpose.

6. The field tran_value should be convert to 2 decimal places.

7.The tran_date must be convert to yyyy/mm/dd to avoid breaking code.

8. Corrupted cell tran_status we need to decode using unicode.




