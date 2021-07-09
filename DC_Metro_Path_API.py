import http.client, urllib.request, urllib.parse,json,os,re,time,datetime,pytz

headers = {
    'api_key': '579beb0d63df4e159cb686f8d41f5ad0',
}
transfer_station = None

def clear():
    os.system('cls||clear')

def main():
    req = http.client.HTTPSConnection('api.wmata.com')
    req.request("GET", "/Rail.svc/json/jStations?%s", "{body}", headers)
    response = req.getresponse()
    lines = response.read().decode('UTF-8')
    data = json.loads(lines)
    start_station = input("Start Station: ")
    while re.search("^([A-Z][a-z]+ ?)+", str(start_station)) == None:
        print("Bad Input, Try Again")
        time.sleep(1)
        clear()
        start_station = input("Start station: ")
    end_station = input("End Station: ")
    while re.search("^([A-Z][a-z]+ ?)+", str(end_station)) == None:
        print("Bad Input, Try Again")
        time.sleep(1)
        end_station = input("End Station: ")
    start_id = None
    start_line = None
    end_id = None
    end_line = None
    for i in data.get("Stations"):
        if i.get("Name") == start_station:
            start_id = i.get('Code')
            start_line = i.get('LineCode1')
        if i.get("Name") == end_station:
            end_id = i.get('Code')
            end_line = i.get('LineCode1')
    req.close()
    clear()
    print("Calculating Route From " + start_station + " to " + end_station + "...")
    if start_line == end_line:
        ret = one_path(start_id,end_id)
    else :
        ret = route(start_station, end_station, start_line, end_line, start_id, end_id)
    counter = 1
    if ret != None:
        clear()
        path_info(start_id,end_id, start_station, end_station, start_line, end_line)
        print("Stations List: ")
        for i in ret:
            print("\t" + str(counter) + ". " + i)
            counter += 1
        print("Total Number of Stations: " + str(len(ret)))
    else:
        print("Error in computing path")

def transfers(code):
    ret = []
    r = http.client.HTTPSConnection('api.wmata.com')
    p = urllib.parse.urlencode({
        'StationCode': code,
    })
    r.request("GET", "/Rail.svc/json/jStationInfo?%s" % p, "{body}", headers)
    resp = r.getresponse()
    station = resp.read().decode('utf8')
    data = json.loads(station)
    if data.get("StationTogether1") != "":
        r2 = http.client.HTTPSConnection('api.wmata.com')
        p2 = urllib.parse.urlencode({
            'StationCode': data.get("StationTogether1"),
        })
        r2.request("GET", "/Rail.svc/json/jStationInfo?%s" % p2, "{body}", headers)
        resp2 = r2.getresponse()
        station2 = resp2.read().decode('utf8')
        data2 = json.loads(station2)
        if data2.get("StationTogether1") != "":
            for i in data2:
                if (re.search("LineCode[123]",i)) and (data2.get(i) != None) and (data2.get(i) not in ret):
                    ret.append(data2.get(i))
        r2.close()
    for i in data:
        if (re.search("LineCode[123]",i)) and (data.get(i) != None) and (data.get(i) not in ret):
            ret.append(data.get(i)) 
    r.close()
    if data.get("StationTogether1") != "":
        return (data.get("StationTogether1"),ret)
    return (data.get("Code"),ret)

def route(start_station, end_station, start_line_code, end_line_code, start_code, end_code):
    req = http.client.HTTPSConnection('api.wmata.com')
    req.request("GET", "/Rail.svc/json/jLines?%s", "{body}", headers)
    response = req.getresponse()
    lines = response.read().decode('UTF-8')
    data = json.loads(lines)
    line_start = None
    line_end = None
    for i in data.get("Lines"):
        if i.get("LineCode") == start_line_code:
            line_start = i.get("StartStationCode")
            line_end = i.get("EndStationCode")
    req.close()
    x = paths(line_start,end_line_code, start_code, end_code)
    y = paths(line_end, end_line_code, start_code, end_code)
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

def paths(line_code, end_line_code, start_code, end_code):
    global transfer_station
    ret = []
    req = http.client.HTTPSConnection('api.wmata.com')
    params1 = urllib.parse.urlencode({
        'FromStationCode': start_code,
        'ToStationCode': line_code,
    })
    req.request("GET", "/Rail.svc/json/jPath?%s" % params1, "{body}", headers)
    response1 = req.getresponse()
    path1 = response1.read().decode('UTF-8')
    data_path1 = json.loads(path1)
    for i in data_path1.get("Path"):
        (x,y) = transfers(i.get("StationCode"))
        for j in y:
            if j == end_line_code:
                transfer_station = i.get("StationName")
                return (ret + one_path(x,end_code))
        ret.append(i.get("StationName"))            
    req.close()
    return ret

def one_path(start_code, end_code):
    ret = []
    r = http.client.HTTPSConnection('api.wmata.com')
    params2 = urllib.parse.urlencode({
        'FromStationCode': start_code,
        'ToStationCode': end_code,
    })
    r.request("GET", "/Rail.svc/json/jPath?%s" % params2, "{body}", headers)
    response2 = r.getresponse()
    path2 = response2.read().decode('UTF-8')
    data_path2 = json.loads(path2)
    for i in data_path2.get("Path"):
        ret.append(i.get("StationName"))
    r.close()
    return ret

def path_info(start_id, end_id, start_station, end_station, start_line, end_line):
    r = http.client.HTTPSConnection('api.wmata.com')
    params = urllib.parse.urlencode({
        'FromStationCode': start_id,
        'ToStationCode': end_id,
    })
    r.request("GET", "/Rail.svc/json/jSrcStationToDstStationInfo?%s" % params, "{body}", headers)
    response = r.getresponse()
    info = response.read().decode('UTF-8')
    data_info = json.loads(info)
    day_of_week = datetime.datetime.today().weekday()
    now = datetime.datetime.now(pytz.timezone('America/New_York'))
    five_am = now.replace(hour=7, minute=0, second=0, microsecond=0)
    nine_thirty_am = now.replace(hour=9, minute=30, second=0, microsecond=0)
    three_pm = now.replace(hour=15, minute=0, second=0, microsecond=0)
    seven_pm = now.replace(hour=19, minute=0, second=0, microsecond=0)
    fare = 0
    total_time = 0
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
    for i in data_info.get("StationToStationInfos"):
        if day_of_week <= 4:
            if (now >= five_am and now <= nine_thirty_am) or (now >= three_pm and now <= seven_pm):
                fare = i.get("RailFare").get("PeakTime")
            else:
                fare = i.get("RailFare").get("OffPeakTime")
        else:
            fare = i.get("RailFare").get("OffPeakTime")
        total_time = i.get("RailTime")
    print("Total Time: " + str(total_time) + " minutes\nCurrent Date and Time in Washington DC: " + str(now.strftime("%m/%d/%Y - %H:%M:%S")) + "\nCost (adjusted for peak/off-peak hours based on current time in DC): $" + str(fare))

main()