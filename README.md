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

| Red Line  | Yellow Line | Green Line | Blue Line | Orange Line | Silver Line |
| --------- | ----------- | ---------- |
| Metro Center | Pentagon | Mt Vernon Sq 7th St-Convention Center |
| Farragut North | Pentagon City | Shaw-Howard U |
| Dupont Circle | Crystal City | U Street/African-Amer Civil War Memorial/Cardozo |
| Woodley Park-Zoo/Adams Morgan | Ronald Reagan Washington National Airport | Columbia Heights| 
| Cleveland Park | Braddock Road | Georgia Ave-Petworth |
| Van Ness-UDC | King St-Old Town | Fort Totten |
| Tenleytown-AU | Eisenhower Avenue | West Hyattsville |
| Friendship Heights | Huntington | Prince George's Plaza|
| Bethesda | Mt Vernon Sq 7th St-Convention Center | College Park-U of Md |
| Medical Center | Shaw-Howard U | Greenbelt |
| Grosvenor-Strathmore | U Street/African-Amer Civil War Memorial/Cardozo | Gallery Pl-Chinatown |
| White Flint | Columbia Heights | Archives-Navy Memorial-Penn Quarter |
| Twinbrook | Georgia Ave-Petworth | L'Enfant Plaza |
| Rockville | Fort Totten | Waterfront |
| Shady Grove | Gallery Pl-Chinatown | Navy Yard-Ballpark |
| Gallery Pl-Chinatown | Archives-Navy Memorial-Penn Quarter | Anacostia |
| Judiciary Square | L'Enfant Plaza | Congress Heights |
| Union Station | | Southern Avenue |
| Rhode Island Ave-Brentwood | | Naylor Road |
| Brookland-CUA | | Suitland |
| Fort Totten | | Branch Ave |
| Takoma | | |
| Silver Spring | | |
| Forest Glen | | |
| Wheaton | | |
| Glenmont | | |
| NoMa-Gallaudet U | | |


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
