file = open("fortnite.txt")

print(file.read())

file.close()
#write operation
file = open("fortnite.txt", 'w')

print(file.write("Fortnite is a game where players can join matches and elimate players using weapons.Fortnite has popular gamemodes such as battle royale, reload, and rocket racing.Players can have skins, pickaxes, back blings, and emote which will be displayed in-game and in the lobby.Every few months a new season or chapter comes where a new update happens from items the map.The battlepass is 950 vbucks or $9.00 in which players collect xp from doing different quests or achievements. To get vbucks $9.00 for 1000 vbucks and other packages for more vbucks"))

file.close()
#append operation
file = open("fortnite.txt", 'a')

print(file.write("To get vbucks $9.00 for 1000 vbucks and other packages for more vbucks which can be used in the shop for skins, emotes, pickaxes, wraps, and packages"))

file.close()
#counting lines
file = open("fortnite.txt")

Counter = 0
Content = file.read()


CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1
        
print("This is the number of lines in the file.")
print(Counter)

file.close