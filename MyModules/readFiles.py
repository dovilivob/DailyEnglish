import json
import sys
from os.path import dirname, abspath

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import MyModules.TimerLoadBar as TimeBar

class Load:
    with open("Databases\Database.json", mode="r") as file:
        load_json = json.loads(file.read())
        TimeBar.Adding()

    with open("Databases\daily_english.json", mode="r") as file:
        Dictionary = file.read()
        TimeBar.Adding()

    lastCharsRepeated = load_json[2]["Analysing Results"]["Advanced Datas"][
        "Characters Repeated Times"
    ]


    # lastAllan = load_json[3]["Project Statment"]["Allan Poe Index"]

    with open("Databases\TypingPracticeRecords.json", mode="r") as file:
        typingJson = file.read()
        TimeBar.Adding()
        typingDatas =  json.loads(typingJson)
        TimeBar.Adding()