def getTeamsData():
    inp = input("Enter Input : ").split("/")
    mapping = ["name","wins","loss","draws","scored","conceded"]
    teams = list()
    for t in inp:
        team = dict()
        for i, data in enumerate(t.split(',')):
            if i > 0: data = int(data)
            team[mapping[i]] = data
        teams.append(team)

    return teams

def calcPoints(teams_data):
    teams_points = list()
    for team in teams_data:
        current_team = dict()
        current_team["name"] = team["name"]
        current_team["points"] = 3*team["wins"] + 1*team["draws"]
        current_team["gd"] = team["scored"] - team["conceded"]
        teams_points.append(current_team)

    return teams_points

def sortPoint(teams_points):
    for i in range(1, len(teams_points)):
        key = teams_points[i]
        j = i-1

        while j >= 0 and (teams_points[j]["points"] < key["points"] or 
                         (teams_points[j]["points"] == key["points"] and teams_points[j]["gd"] < key["gd"])):
            teams_points[j+1] = teams_points[j]
            j -= 1
                
        teams_points[j+1] = key
    
    return teams_points

teams = getTeamsData()
teams_points = calcPoints(teams)
sortPoint(teams_points)

print("== results ==")
for t in teams_points:
    print([t["name"], {"points":t["points"]}, {"gd":t["gd"]}])


