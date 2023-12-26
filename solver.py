values = 0

file1 = open('p1_input.txt','r')
file1 = open('p1_input.example','r')
Lines = file1.readlines()

#red, green, blue
num_marbles = [12,13,14]

for index, games in enumerate(Lines):
    max_marbles = {"green":0,"blue":0,"red":0}
    games = games.split(":")
    games = games[1].replace(",","").strip()
    games = games.split(";")
    for game in games:
        tmp = game.split()
        print("game:",index+1,tmp)
        for i in range(len(tmp)-1):
            if i % 2 == 0:
                if max_marbles[tmp[i+1]] < int(tmp[i]):
                    max_marbles[tmp[i+1]] = int(tmp[i])
    print(max_marbles)
    if(max_marbles["red"] <= num_marbles[0] and max_marbles["green"] <= num_marbles[1] and max_marbles["blue"] <= num_marbles[2]):
        values += index+1

print(values)

