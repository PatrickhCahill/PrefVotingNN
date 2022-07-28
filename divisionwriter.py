from collections import defaultdict
import csv
import pymongo
from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb+srv://Patrick:ZeusAri5@pcluster.8cgdq.mongodb.net/?retryWrites=true&w=majority")
db = client.election_forecast
seats = db.seat_collection

default = lambda: {
    "name":"default_name",
    "state":"default_state",
    "2022winner_name": "default_winner",
    "2022winner_party":"default_party",
    "openrace" : False,
    "results2022": {
        "votesprimary":{
            "alp" :0,
            "lp"  :0,
            "np"  :0,
            "grn" :0,
            "on" :0,
            "uapp":0,
            "ajp" :0,
            "ind" :0,
            "others":0,
            "informal":0
        },
        "votes2cp" : {
        },
        "votes2pp" : {
            "alp":0,
            "lp" :0
        }
    }
}
DOING = False
if DOING:
    d = defaultdict(lambda:default())

    with open("2CPDivision.csv","r") as data2cpfile:
        next(data2cpfile)
        data2cp = csv.DictReader(data2cpfile,delimiter=',',quotechar='"')
        for row in data2cp:
            # Populate all of the seats with correct names
            seatinfo = d[row["DivisionNm"].lower()]
            seatinfo["name"] = row["DivisionNm"].lower()

            # Populate seats with the 2cp data 2022
            seatinfo["results2022"]["votes2cp"][row["PartyAb"].lower()] = int(row["TotalVotes"])
            
            # Populate the state entry of each seat
            seatinfo["state"] = row["StateAb"]

            # Populate seat winner and party
            if row["Elected"] == "Y":
                winner2022 = row["Surname"] +"_"+row["GivenNm"]
                seatinfo["2022winner_name"] = winner2022
                seatinfo["2022winner_party"] = row["PartyAb"].lower()

    with open("PrimaryDivision.csv","r") as primarydatafile:
        next(primarydatafile)
        primarydata = csv.DictReader(primarydatafile,delimiter=',',quotechar='"')
        for row in primarydata:
            seatinfo = d[row["DivisionNm"].lower()]
            seatinfo["name"] = row["DivisionNm"].lower()

            if row["PartyAb"].lower()=="ind":
                # If the row is an independent, we check the winner of the seat:
                candidateName = row["Surname"] +"_"+row["GivenNm"]
                # Catch if it is a second independent running:
                if seatinfo["2022winner_party"]=="ind" and candidateName != seatinfo["2022winner_name"]:
                    seatinfo["results2022"]["votesprimary"][row["PartyAb"].lower()+row["Surname"]] = int(row["TotalVotes"])
                # This is correct candidate and either the winner and/or the only independent:
                else:
                    seatinfo["results2022"]["votesprimary"][row["PartyAb"].lower()] = int(row["TotalVotes"])
            elif row["PartyAb"].lower()=="" or row["PartyAb"]==None or not row["PartyAb"]:
                # Catch the informal votes
                if row["PartyNm"].lower()=="informal":
                    seatinfo["results2022"]["votesprimary"]["informal"] = int(row["TotalVotes"])
            elif row["PartyAb"].lower() not in ["alp","lp","np","grn","on","uapp","ajp"]:
                # Put parties not modelled into others
                seatinfo["results2022"]["votesprimary"]["others"] += int(row["TotalVotes"])
            else:
                # Everything else gets logged
                seatinfo["results2022"]["votesprimary"][row["PartyAb"].lower()] = int(row["TotalVotes"])

    outdata = list(d.values())
    seats.insert_many(outdata)

results = seats.find({},{"name":1})
for result in results:
    pprint(result)

""" Future Plans
-------------
1.

Load 2PP data into the database
Develop some helper functions that calculate a national 2pp, national primary data, a seat pendulum
Add all the 2019, 2016, 2013, 2010, 2007 seat data into database

2.
Train neural net on above polling place data

3.
Create a polling collection
Create a Kalman filter and simple polling averages for polls
Polls should contain: results, sample size, pollster -> with house effects etc...

4.
Create function tools that then calculate predicted swings and then

5.
Kalman filter should use fundamentals which can then be made more sophisticated.
# # # #
As I go along I should create helper functions that make editing the database easier. Flag properties that I'm concerned with etc.  """