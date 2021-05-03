#for functions only

import discord
def addletters(msg):
    msg=msg.lower()
    countlet=load_database()
    for letter in msg:
        try:
            countlet["lettercount"][str(letter)]+=1
        except:
            # countlet["lettercount"][str(letter)]=0
            pass
    save_database(countlet)
def filterOnlyOnlineMembers(member):
    import discord
    return member.status != discord.Status.offline

def notice(client,title,disc):
	channel = client.get_channel(807532505137545217)
	embed = discord.Embed(
	title=title,
	description=disc,
	color=0x0066ff)
	return channel.send(embed=embed)

def collectdata(client):
    from datetime import date, datetime
    from dateutil.tz import gettz
    import time
    while True:
        now = datetime.now(tz=gettz('Asia/Kolkata'))
        if now.minute % 30 == 0:
            info = load_database()["peopleinfo"]
            for guild in client.guilds:
                membersInServer = guild.members

                membersonline = len(
                    list(filter(filterOnlyOnlineMembers, membersInServer)))
                try:
                    info[str(guild.id)][f"{now.day}/{now.month}/{now.year}"][
                        now.strftime("%H:%M:%S")] = [
                            guild.member_count, membersonline
                        ]
                except:
                    try:
                        info[str(guild.id) ][f"{now.day}/{now.month}/{now.year}"] = {}
                        info[str(guild.id)][f"{now.day}/{now.month}/{now.year}"][
                            now.strftime("%H:%M:%S")] = [
                                guild.member_count, membersonline
                            ]
                    except:

                        info[str(guild.id)] = {}
                        info[str(guild.id)][f"{now.day}/{now.month}/{now.year}"] = {}
                        info[str(guild.id)][f"{now.day}/{now.month}/{now.year}"][
                            now.strftime("%H:%M:%S")] = [
                                guild.member_count, membersonline
                            ]
            pepif=load_database()
            pepif["peopleinfo"]=info
            save_database(pepif)
            print(info)
            time.sleep(600)
        if now.minute % 30 > 15:
            time.sleep((30 - now.minute) % 30)
        else:
            time.sleep(now.minute % 300)


def find_database_path():
    import sys
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "]
    if lix[0][0] not in letter_list:
        return "database.json"
    else:
        for item in letter_list:  #two
            if item == lix[0][0]:
                indexx = letter_list.index(lix[0][0])
                slashindex.append(indexx)
                letter_list[indexx] = "a"
        return relative_path[0:slashindex[-1]] + "\database.json"


def load_database():
    import json
    import os
    global pstr
    path = find_database_path()
    if os.path.exists(path):
        with open(path, "r") as jsonFile:
            info = json.load(jsonFile)

    else:
        initial_data = {
            "peopleinfo":{},
            "serverchannel":{}

        }
        with open(path, "w") as jsonFile:
            json.dump(initial_data, jsonFile, indent=4)
        with open(path, "r") as jsonFile:
            info = json.load(jsonFile)

    return info


def save_database(info):
    import json
    path = find_database_path()
    with open(path, "w") as jsonFile:
        json.dump(info, jsonFile, indent=4)
