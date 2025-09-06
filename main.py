from requests import get
from pprint import PrettyPrinter

baseURL = "https://data.nba.net"
allJSON = "/prod/v1/today.json"
printer = PrettyPrinter()
def getLinks():
    dataSet = get(baseURL + allJSON).json()  # whenever we send a request the program will have access to json
    links = dataSet["links"]
    return links


def getscoreBoard():
    scoreBoard = getLinks()["currentScoreBoard"]
    gameData = get(baseURL + scoreBoard).json()["games"]
    for game in gameData:
        homeTeam = game["hTeam"]
        awayTeam = game["vTeam"]
        time = game["clock"]
        period = game["period"]
        print("----------------------------")
        print(f"{homeTeam["triCode"]} VS {awayTeam["triCode"]}")
        print(f"{homeTeam["score"]} - {awayTeam["score"]}") # score of each team
        print(f"{time} - {period["current"]}")
        
def getStats():
    stats = getLinks()["leagueTeamStatsLeaders"]
    teamStats = get(baseURL + stats).json()["league"]["standard"]["regular season"]["teams"]

    # filtering teams with unrelatable names
    # we use filter function which will filter out against every single element in the list of teams 
    # if function returns true - program will keep the element. If it returns false, the program will remove it
    teams = list(filter(lambda x: x["name"] != "Team", teams)) # here we use list because the filter function returns an object and not a list. Since we wnated a list therefore used list function
    # now we rank teams based on their ranks per game
    teams.sort(key = lambda x: int(x["ppg"]["rank"]))

    for i,  team in enumerate(teamStats):
        name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]["avg"]
        print(f"{i + 1}{name} - {nickname} - {ppg}")

getStats()




