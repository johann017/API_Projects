# API_Projects

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

<h3 align="center">Metro Map</h3>
<p align="center">
   <img src="https://github.com/johann017/API_Projects/blob/9fde986c9c92d25bd5ee1111af20e23a9e1e588b/Metro_Details/Metro_Map.PNG" width = "600" height = "600"/>
</p>

<h3 align="center">All Stations</h3>

| Red Line  |  
| --------- |
| Metro Center |
| Farragut North |
| Dupont Circle |
| Woodley Park-Zoo/Adams Morgan |
| Cleveland Park |
| Van Ness-UDC |
| Tenleytown-AU |
| Friendship Heights |
| Bethesda |
| Medical Center |
| Grosvenor-Strathmore |
| White Flint |
| Twinbrook |
| Rockville |
| Shady Grove |
| Gallery Pl-Chinatown |
| Judiciary Square |
| Union Station |
| Rhode Island Ave-Brentwood |
| Brookland-CUA |
| Fort Totten |
| Takoma |
| Silver Spring |
| Forest Glen |
| Wheaton |
| Glenmont |
| NoMa-Gallaudet U |


## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect to GitHub account
- Open Git CMD
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
