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
    - This program takes user input and checks to see if it follows proper case conventions through the use of regular expressions. It finds the path between two stations with at most one transfer. Since the fare changes based on peak hours, the program accounts for the current time in DC, regardless of where the user is, to calculate the precise fare for the trip and gives a rough estimate for the time taken. For a neater display, the terminal is cleared after execution and will leave only the vital information like lines to take, place to transfer, time taken, total cost, and stations list. To ensure a higher degree of precision, this program will work if more stations and transfer stations are added in the future.

<h3 align="center">Metro Map</h3>
<p align="center">
   <img src="https://github.com/johann017/API_Projects/blob/9fde986c9c92d25bd5ee1111af20e23a9e1e588b/Metro_Details/Metro_Map.PNG" width = "600" height = "600"/>
</p>

<h3 align="center">All Stations</h3>

| Red Line  | Yellow Line | Green Line | Blue Line | Orange Line | Silver Line |
| --------- | ----------- | ---------- | --------- | ----------- | ----------- |
| Metro Center | Pentagon | Mt Vernon Sq 7th St-Convention Center | Metro Center | Metro Center | Metro Center |
| Farragut North | Pentagon City | Shaw-Howard U | McPherson Square | McPherson Square | McPherson Square |
| Dupont Circle | Crystal City | U Street/African-Amer Civil War Memorial/Cardozo | Farragut West | Farragut West | Farragut West | 
| Woodley Park-Zoo/Adams Morgan | Ronald Reagan Washington National Airport | Columbia Heights| Foggy Bottom-GWU | Foggy Bottom-GWU | Foggy Bottom-GWU |
| Cleveland Park | Braddock Road | Georgia Ave-Petworth | Rosslyn | Rosslyn | Rosslyn |
| Van Ness-UDC | King St-Old Town | Fort Totten | Arlington Cemetery | Federal Triangle | Federal Triangle |
| Tenleytown-AU | Eisenhower Avenue | West Hyattsville | Pentagon | Smithsonian | Smithsonian |
| Friendship Heights | Huntington | Prince George's Plaza| Pentagon City | L'Enfant Plaza | L'Enfant Plaza |
| Bethesda | Mt Vernon Sq 7th St-Convention Center | College Park-U of Md | Crystal City | Federal Center SW | Federal Center SW |
| Medical Center | Shaw-Howard U | Greenbelt | Ronald Reagan Washington National Airport | Capitol South | Capitol South |
| Grosvenor-Strathmore | U Street/African-Amer Civil War Memorial/Cardozo | Gallery Pl-Chinatown | Braddock Road | Eastern Market | Eastern Market |
| White Flint | Columbia Heights | Archives-Navy Memorial-Penn Quarter | King St-Old Town | Potomac Ave | Potomac Ave |
| Twinbrook | Georgia Ave-Petworth | L'Enfant Plaza | Federal Triangle | Stadium-Armory | Stadium-Armory |
| Rockville | Fort Totten | Waterfront | Smithsonian | Minnesota Ave | Benning Road |
| Shady Grove | Gallery Pl-Chinatown | Navy Yard-Ballpark | L'Enfant Plaza | Deanwood | Capitol Heights |
| Gallery Pl-Chinatown | Archives-Navy Memorial-Penn Quarter | Anacostia | Federal Center SW | Cheverly | Addison Road-Seat Pleasant |
| Judiciary Square | L'Enfant Plaza | Congress Heights | Capitol South | Landover | Morgan Boulevard |
| Union Station | | Southern Avenue | Eastern Market | New Carrollton | Largo Town Center |
| Rhode Island Ave-Brentwood | | Naylor Road | Potomac Ave | Court House | Court House |
| Brookland-CUA | | Suitland | Stadium-Armory | Clarendon | Clarendon | 
| Fort Totten | | Branch Ave | Benning Road | Virginia Square-GMU | Virginia Square-GMU |
| Takoma | | | Capitol Heights | Ballston-MU | Ballston-MU | 
| Silver Spring | | | Addison Road-Seat Pleasant | East Falls Church | East Falls Church |
| Forest Glen | | | Morgan Boulevard | West Falls Church-VT/UVA | McLean |
| Wheaton | | | Largo Town Center | Dunn Loring-Merrifield | Tysons Corner |
| Glenmont | | | Van Dorn Street | Vienna/Fairfax-GMU | Greensboro |
| NoMa-Gallaudet U | | | Franconia-Springfield | | Spring Hill |
| | | | | | Wiehle-Reston East |


## Setup
- Install [GitHub CLI](https://cli.github.com/) and connect to GitHub account
- Open Git CMD
- Run `gh repo clone johann017/API_Projects` in the command line
- Move into the API_Projects directory

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
