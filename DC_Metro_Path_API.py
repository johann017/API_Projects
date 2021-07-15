import http.client, urllib.request, urllib.parse, json, os, re, time, datetime, pytz

#Header to be used by all API calls
headers = {
    'api_key': '579beb0d63df4e159cb686f8d41f5ad0',
}

#Variable to hold the one transfer station
transfer_station = None

#Clears the terminal screen to ensure a clear display of information
def clear():
    os.system('cls||clear')


def main():
    #Gets all stations from this API call
    req = http.client.HTTPSConnection('api.wmata.com')
    req.request("GET", "/Rail.svc/json/jStations?%s", "{body}", headers)
    response = req.getresponse()
    
    #Converts the binary data to UTF-8 and into a json format
    lines = response.read().decode('UTF-8')
    data = json.loads(lines)
    
    #Gets user input for starting station
    start_station = input("Start Station: ")
    
    #Makes sure it follows the first letter uppercase and rest lower case per word
    while re.search("^([A-Z][a-z]+ ?)+", str(start_station)) == None:
        print("Bad Input, Try Again")
        time.sleep(1)
        clear()
        start_station = input("Start station: ")
        
    #Gets user input for end station
    end_station = input("End Station: ")
    
    #Makes sure it follows the first letter uppercase and rest lower case per word
    while re.search("^([A-Z][a-z]+ ?)+", str(end_station)) == None:
        print("Bad Input, Try Again")
        time.sleep(1)
        end_station = input("End Station: ")
        
    #Variables to use
    start_id = None
    start_line = None
    end_id = None
    end_line = None
    
    #Goes through all the stations and if they match the starting and ending station
    #it will get the station code and the line color.
    for i in data.get("Stations"):
        if i.get("Name") == start_station:
            start_id = i.get('Code')
            start_line = i.get('LineCode1')
        if i.get("Name") == end_station:
            end_id = i.get('Code')
            end_line = i.get('LineCode1')
    req.close()
    
    #Clears the screen
    clear()
    print("Calculating Route From " + start_station + " to " + end_station + "...")
    
    #Checks to see if it's on the same path and gets the path
    if start_line == end_line:
        ret = one_path(start_id,end_id)
    else :
        ret = route(start_station, end_station, start_line, end_line, start_id, end_id)
    counter = 1
    
    #Checks if the path exists. It then clears the screen and then prints all relevant information
    #and then the station list and the number of stations to take.
    if ret != None:
        clear()
        path_info(start_id,end_id, start_station, end_station, start_line, end_line)
        print("Stations List: ")
        for i in ret:
            print("\t" + str(counter) + ". " + i)
            counter += 1
        print("Total Number of Stations: " + str(len(ret)))
    else:
        print("Error in computing path. Check input.")

  
#This function checks if a station is transfer code and returns all lines that runs through
#this station
def transfers(code):
    
    #Array of lines
    ret = []
    
    #Gets the station information
    r = http.client.HTTPSConnection('api.wmata.com')
    p = urllib.parse.urlencode({
        'StationCode': code,
    })
    r.request("GET", "/Rail.svc/json/jStationInfo?%s" % p, "{body}", headers)
    resp = r.getresponse()
    
    #Converts the binary code to UTF-8 and then into JSON format
    station = resp.read().decode('UTF-8')
    data = json.loads(station)
    
    #Checks if the station is a transfer station
    if data.get("StationTogether1") != "":
        
        #Gets the station information the current station's other code
        r2 = http.client.HTTPSConnection('api.wmata.com')
        p2 = urllib.parse.urlencode({
            'StationCode': data.get("StationTogether1"),
        })
        r2.request("GET", "/Rail.svc/json/jStationInfo?%s" % p2, "{body}", headers)
        resp2 = r2.getresponse()
        
        #Converts the binary code to UTF-8 and then into JSON format
        station2 = resp2.read().decode('utf8')
        data2 = json.loads(station2)
        
        #Double checks if the station is a transfer station
        if data2.get("StationTogether1") != "":
            
            #Goes through all the lines and adds their color to the return list
            for i in data2:
                if (re.search("LineCode[123]",i)) and (data2.get(i) != None) and (data2.get(i) not in ret):
                    ret.append(data2.get(i))
        r2.close()
        
    #Goes through all the lines and adds their color to the return list
    for i in data:
        if (re.search("LineCode[123]",i)) and (data.get(i) != None) and (data.get(i) not in ret):
            ret.append(data.get(i)) 
    r.close()
    
    #Checks if it is a transfer station and returns the current station code and the color line list
    if data.get("StationTogether1") != "":
        return (data.get("StationTogether1"),ret)
    
    #Returns the transfer station's other code and color line list
    return (data.get("Code"),ret)


#This function get all possible routes and decides which one is the correct one to take
def route(start_station, end_station, start_line_code, end_line_code, start_code, end_code):
    
    #Gets all the lines
    req = http.client.HTTPSConnection('api.wmata.com')
    req.request("GET", "/Rail.svc/json/jLines?%s", "{body}", headers)
    response = req.getresponse()
    
    #Converts the binary code to UTF-8 and then into JSON format
    lines = response.read().decode('UTF-8')
    data = json.loads(lines)
    line_start = None
    line_end = None
    
    #Goes through all the lines and finds the starting line code and gets the start
    #and end station for that line 
    for i in data.get("Lines"):
        if i.get("LineCode") == start_line_code:
            line_start = i.get("StartStationCode")
            line_end = i.get("EndStationCode")
    req.close()
    
    #Gets the path from the starting line station
    x = paths(line_start,end_line_code, start_code, end_code)
    
    #Gets the path from the ending line station
    y = paths(line_end, end_line_code, start_code, end_code)
    
    #Checks if the inputted start and end stations are in both paths 
    #then checks which path is shorter
    if (start_station in x) and (end_station in x):
        if (start_station in y) and (end_station in y):
            if len(x) > len(y):
                return y
            else:
                return x
        else:
            return x
    elif (start_station in y) and (end_station in y):
        return y
    else:
        return None

    
#This function get the paths to go from start station to the end
def paths(line_code, end_line_code, start_code, end_code):
    global transfer_station
    
    #Holds all the stations that are being passed through
    ret = []
    
    #Gets the path from the start station to either the start or end of the line station
    req = http.client.HTTPSConnection('api.wmata.com')
    params1 = urllib.parse.urlencode({
        'FromStationCode': start_code,
        'ToStationCode': line_code,
    })
    req.request("GET", "/Rail.svc/json/jPath?%s" % params1, "{body}", headers)
    response1 = req.getresponse()
    
    #Converts the binary code to UTF-8 and then into JSON format
    path1 = response1.read().decode('UTF-8')
    data_path1 = json.loads(path1)
    
    #Goes through all the stations and get the transfer station or station that connects with
    #line code of the end station.
    for i in data_path1.get("Path"):
        (x,y) = transfers(i.get("StationCode"))
        for j in y:
            if j == end_line_code:
                transfer_station = i.get("StationName")
                return (ret + one_path(x,end_code))
        ret.append(i.get("StationName"))            
    req.close()
    return ret

#Gets the stations that are on a specific path
def one_path(start_code, end_code):
    
    #Holds all stations being passed through
    ret = []
    
    #Gets all the stations between the start and end code
    r = http.client.HTTPSConnection('api.wmata.com')
    params2 = urllib.parse.urlencode({
        'FromStationCode': start_code,
        'ToStationCode': end_code,
    })
    r.request("GET", "/Rail.svc/json/jPath?%s" % params2, "{body}", headers)
    response2 = r.getresponse()
    
    #Converts the binary code to UTF-8 and then into JSON format
    path2 = response2.read().decode('UTF-8')
    data_path2 = json.loads(path2)
    
    #Goes through all the stations on the path and adds them to the station list to be returned
    for i in data_path2.get("Path"):
        ret.append(i.get("StationName"))
    r.close()
    return ret


#This function will display all relevent and useful information
def path_info(start_id, end_id, start_station, end_station, start_line, end_line):
    
    #Gets the station to station information
    r = http.client.HTTPSConnection('api.wmata.com')
    params = urllib.parse.urlencode({
        'FromStationCode': start_id,
        'ToStationCode': end_id,
    })
    r.request("GET", "/Rail.svc/json/jSrcStationToDstStationInfo?%s" % params, "{body}", headers)
    response = r.getresponse()
    
    #Converts the binary code to UTF-8 and then into JSON format
    info = response.read().decode('UTF-8')
    data_info = json.loads(info)
    
    #Gets the day of the week as a number (Monday = 0, Tuesday = 1, ...)
    day_of_week = datetime.datetime.today().weekday()
    
    #Gets the current time on the east coast
    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    
    #Creates time objects for 5 am, 9:30 am, 3 pm, and 7 pm
    five_am = now.replace(hour=7, minute=0, second=0, microsecond=0)
    nine_thirty_am = now.replace(hour=9, minute=30, second=0, microsecond=0)
    three_pm = now.replace(hour=15, minute=0, second=0, microsecond=0)
    seven_pm = now.replace(hour=19, minute=0, second=0, microsecond=0)
    fare = 0
    total_time = 0
    
    #Gets prints the start station, start line color, transfer station, end station and end line color
    print("Starting from " + start_station + ", take the", end = "")
    if start_line == 'RD':
        print(" red ", end = "")
    if start_line == 'BL':
        print(" blue ", end = "")
    if start_line == 'GR':
        print(" green ", end = "")
    if start_line == 'SV':
        print(" silver ", end = "")
    if start_line == 'OR':
        print(" orange ", end = "")
    if start_line == 'YL':
        print(" yellow ", end = "")
    print("line to get to the transfer station at " + str(transfer_station) + ". Then take the", end = "")
    if end_line == 'RD':
        print(" red ", end = "")
    if end_line == 'BL':
        print(" blue ", end = "")
    if end_line == 'GR':
        print(" green ", end = "")
    if end_line == 'SV':
        print(" silver ", end = "")
    if end_line == 'OR':
        print(" orange ", end = "")
    if end_line == 'YL':
        print(" yellow ", end = "")
    print("line to " + end_station + ".")
    
    #Goes through the API call's information to get the far and the total time
    for i in data_info.get("StationToStationInfos"):
        
        #Adjusts the price if it's peak time or not
        if day_of_week <= 4:
            if (now >= five_am and now <= nine_thirty_am) or (now >= three_pm and now <= seven_pm):
                fare = i.get("RailFare").get("PeakTime")
            else:
                fare = i.get("RailFare").get("OffPeakTime")
        else:
            fare = i.get("RailFare").get("OffPeakTime")
            
        #Gets total time elapsed between stations
        total_time = i.get("RailTime")
    print("Total Time: " + str(total_time) + " minutes\nCurrent Date and Time in Washington DC: " + str(now.strftime("%m/%d/%Y - %H:%M:%S")) + "\nCost (adjusted for peak/off-peak hours based on current time in DC): $" + str(fare))

main()
