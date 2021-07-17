# API_Projects

## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect it with GitHub account
- Open up Git CMD
- Run `gh repo clone johann017/API_Projects` in the command line



`UMD_Employee_Salary_API.py`:
- To run this, type the following in to the command line:
  ```
  python UMD_Employee_Salary_API.py
  ```
  
`News_API.py`:
- To run this, type the following in to the command line:
  ```
  python News_API.py
  ```

To run `UMD_DC_Metro_Path_API.py`:
- To run this, type the following in to the command line:
  ```
  python DC_Metro_Path_API.py
  ```

## Description

- ### `UMD_Employee_Salary_API.py`
  - #### Overview: 
    - Analyze UMD's newspaper to retrieve employee with the highest salary information.
  - #### Details: 
    - Utilize API calls to extract the University employee's salary details. It provides the highest paid employee's name, position and salary.

- ### `News_API.py`
  - #### Overview: 
    - Analyze newsapi.org to get news headlines from popular news sites.
  - #### Details: 
    - API calls extract the top 10 news sites along with a brief desciption of the articles.

- ### `DC_Metro_Path_API.py`
  - #### Overview: 
    - Utilizes the DC Metro System's API to collect information about stations.
  - #### Details: 
    - This program takes user input and checks to see if it follows proper case conventions through the use of regular expressions. It finds the path between two stations with at most one transfer. Since the fare changes based on peak hours, the program accounts for the current time in DC, regardless of where the user is, to calculate the precise fare for the trip and gives a rough estimate for the time taken. For a neater display, the terminal is cleared after execution and will leave only the vital information like lines to take, place to transfer, time taken, total cost, and stations list.
