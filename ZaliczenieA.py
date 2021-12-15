import json
import requests
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

import self as self


def check(self):
    with open('db.json') as f:
        datafile = f.readlines()
    found = False
    for line in datafile:
        if str(self) in line:
            found = True
            return True
    return False


@dataclass
class Games:
    Game_name: str = ""
    Game_id: float = 0
    Price: float = 0
    GameTag: str = ""

    def set_Games(self):
        self.Game_name = str(input('Enter game name: '))
        self.Game_id = int(input("Enter game id: "))
        self.Price = float(input("Enter price: "))
        self.GameTag = str(input("Enter GameTag: "))

        x = {
            "GameName": self.Game_name,
            "GameId": self.Game_id,
            "Price": self.Price,
            "GameTag": self.GameTag,
            "id": self.Game_id

        }

        if check(self.Game_id) == True:
            print("There is a game with this id!")
            return 0


        with open('db.json') as f:
            data = json.load(f)
            temp = data['Games']
            temp.append(x)

        with open('db.json', "w") as f:
            json.dump(data, f, indent=4)

    def get_Games(self):
        print("Game name: ", self.Game_name)
        print("Game id: ", self.Game_id)
        print("Price: ", self.Price)
        print("GameTag: ", self.GameTag)


@dataclass
class Users:
    User_name: str = ""
    GamerTag: str = ""
    User_id: int = 0
    Hours_spend_total: float = 0
    Game_own: int = 0

    def set_user(self):
        self.User_name = str(input('Enter Name: '))
        self.GamerTag = str(input("Enter GamerTag: "))
        self.User_id = int(input("Enter user id: "))
        self.Hours_spend_total = int(input("Enter hours spend in all games: "))
        self.Game_own = int(input("Enter Games (amount)"))

        x = {
            "UserName": self.User_name,
            "GamerTag": self.GamerTag,
            "UserId": self.User_id,
            "HoursTotal": self.Hours_spend_total,
            "GameOwn": self.Game_own,
            "id": self.User_id

        }

        if check(self.User_id) == True:
            print("There is a user with this id!")
            return 0

        with open('db.json') as f:
            data = json.load(f)
            temp = data['Users']
            temp.append(x)

        with open('db.json', "w") as f:
            json.dump(data, f, indent=4)

    def get_user(self):
        print("User name: ", self.User_name)
        print("GamerTag: ", self.GamerTag)
        print("User id: ", self.User_id)
        print("Hours total spend: ", self.Hours_spend_total)
        print("Game own: ", self.Game_own)


@dataclass
class Library:
    GamerTag: str = ""
    Game_id: int = 0
    Hours_spend_in_game: float = 0
    Achievements: int = 0

    def set_library(self):
        self.GamerTag = str(input("Enter GamerTag: "))
        self.Game_id = int(input("Enter game id: "))
        self.Hours_spend_in_game = int(input("Enter hours spend in game: "))
        self.Achievements = int(input("Enter amount of achievements"))

        x = {
            "GamerTag": self.GamerTag,
            "GameId": self.Game_id,
            "HoursInGame": self.Hours_spend_in_game,
            "Achievements": self.Achievements,
            "id": self.Game_id

        }

        if check(self.Game_id) == True:
            print("This game is in your library!")
            return 0

        with open('db.json') as f:
            data = json.load(f)
            temp = data['Library']
            temp.append(x)

        with open('db.json', "w") as f:
            json.dump(data, f, indent=4)

    def get_library(self):
        print("GamerTag: ", self.GamerTag)
        print("Game id: ", self.Game_id)
        print("Hours spend in game: ", self.Hours_spend_in_game)
        print("Achievements: ", self.Achievements)


def main():
    x = 0
    r = None
    type = str
    while x != 9:

        print("9. EXIT")
        print("1. Add games")
        print("2. Add User")
        print("3. Add Library")
        print("""4. GET
5. DEL 
6. POST
7. PUT
        """)

        x = int(input("What u want to do: "))
        if x > 3 <9:
            print("""1. Users
2. Games
3. Library""")
            type = str(input("Choose and type the name: "))

        if x == 1:
            Games.set_Games(self)
        elif x == 2:
            Users.set_user(self)
        elif x == 3:
            Library.set_library(self)
        elif x == 4:
            r = requests.get('http://localhost:3000/' + type)
            print(r.text)
        elif x == 5:
            i = int(input("Give id to delete: "))
            r = requests.delete('http://localhost:3000/' + str(type) + '/' + str(i))
            print(r.text)
        elif x == 6:
            if type == "Users":
                a = str(input("User Name: "))
                b = str(input("GamerTag: "))
                c = int(input("UserId: "))
                d = int(input("HoursTotal: "))
                e = int(input("GameOwn"))
                r = requests.post('http://localhost:3000/' + str(type), data={"UserName": a,
                                                                               "GamerTag": b,
                                                                               "UserId": c,
                                                                               "HoursTotal": d,
                                                                               "GameOwn": e,
                                                                                })
            elif type == "Games":
                a = str(input('Enter game name: '))
                b = int(input("Enter game id: "))
                c = float(input("Enter price: "))
                d = str(input("Enter GameTag: "))
                r = requests.post('http://localhost:3000/' + str(type), data={"GameName": a,
                                                                                "GameId": b,
                                                                                "Price": c,
                                                                                "GameTag": d,
                                                                                })
            elif type == "Library":
                a = str(input("Enter GamerTag: "))
                b = int(input("Enter game id: "))
                c = int(input("Enter hours spend in game: "))
                d = int(input("Enter amount of achievements"))
                r = requests.post('http://localhost:3000/' + str(type), data={"GameName": a,
                                                                                "GameId": b,
                                                                                "Price": c,
                                                                                "GameTag": d,
                                                                             })


        elif x == 7:
            if type == "Users":
                f = int(input("id: "))
                r2 = requests.get('http://localhost:3000/' + str(type) + '/' + str(f))
                print(r2.text)
                a = str(input("User Name: "))
                b = str(input("GamerTag: "))
                c = int(input("UserId: "))
                d = int(input("HoursTotal: "))
                e = int(input("GameOwn"))
                r = requests.put('http://localhost:3000/' + str(type) + '/' + str(f), data={"UserName": a,
                                                                              "GamerTag": b,
                                                                              "UserId": c,
                                                                              "HoursTotal": d,
                                                                              "GameOwn": e,
                                                                           })

            elif type == "Games":
                f = int(input("id: "))
                r2 = requests.get('http://localhost:3000/' + str(type) + '/' + str(f))
                print(r2.text)
                a = str(input('Enter game name: '))
                b = int(input("Enter game id: "))
                c = float(input("Enter price: "))
                d = str(input("Enter GameTag: "))
                r = requests.put('http://localhost:3000/' + str(type) + '/' + str(f), data={"GameName": a,
                                                                              "GameId": b,
                                                                              "Price": c,
                                                                              "GameTag": d,
                                                                              })


            elif type == "Library":
                f = int(input("id: "))
                r2 = requests.get('http://localhost:3000/' + str(type) + '/' + str(f))
                print(r2.text)
                a = str(input("Enter GamerTag: "))
                b = int(input("Enter game id: "))
                c = int(input("Enter hours spend in game: "))
                d = int(input("Enter amount of achievements"))
                r = requests.put('http://localhost:3000/' + str(type) + '/' + str(f), data={"GameName": a,
                                                                              "GameId": b,
                                                                              "Price": c,
                                                                              "GameTag": d,
                                                                              })

        if r == None:
            print("Done")
        else:
            print(r)

main()
