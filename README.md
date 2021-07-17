# API_Projects

## Setup
To run `UMD_Employee_Salary_API.py`:
- `python UMD_Employee_Salary_API.py`

To run `News_API.py`:
- `python News_API.py`

To run `UMD_DC_Metro_Path_API.py`:
- `python DC_Metro_Path_API.py`

## Description

- ### `UMD_Employee_Salary_API.py`
  - #### Overview: 
    - Analyze UMD's newspaper to retrieve employee with the highest salary information.
  - #### Details: 
    - Utilize API calls to extract the University employee's salary details. It provides the highest paid employee's name, position and salary.

- ### `News_API.py`
  - This program uses a news API to get the top news from various popular news sites. This will include the source's name and a brief desciption of the article.

- ### `DC_Metro_Path_API.py`
  - This program utilizes the DC Metro System's API to collect information about stations. It will find the path between two stations with at most 1 transfer. This program takes user input and checks to see if it follows proper case conventions through the use of regular expressions. Since the fare changes based on peak hours, the program accounts for the current time in DC, regardless of where the user is, to calculate the precise fare for the trip and rough estimate for the time taken. To keep the results clean, the program clears the terminal after eecution and will leave only the vital information (lines to take, place to transfer, time taken, total cost, stations list) displayed.
