#Load in Statsbomb competition and match data
#This is a library for loading json files.
import json

#Load the competition file
with open('Statsbomb/data/competitions.json') as f:
    competitions = json.load(f)
    
#Champions League has competition ID 16
competition_id=16

#Load the list of matches for this competition 
#The season ID is the matches file name, I will be using the 2018/19 final (4)
with open('Statsbomb/data/matches/'+str(competition_id)+'/4.json') as f:
    matches = json.load(f)

#Look inside matches
matches[0]
matches[0]['home_team']
matches[0]['home_team']['home_team_name']
matches[0]['away_team']['away_team_name']

#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    #Returns all matches for Liverpool
    if (home_team_name=='Liverpool' or away_team_name=='Liverpool'):
        home_score=match['home_score']
        away_score=match['away_score']
        describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
        result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
        print(describe_text + result_text)

#Now lets find a match we are interested in
home_team_required ="Tottenham Hotspur"
away_team_required ="Liverpool"

#Find ID for the match
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']
print(home_team_required + ' vs ' + away_team_required + ' ID:' + str(match_id_required))