def main():
  myFile = open("MLB_Pitching.csv", 'r')

  teamData = []
  
  for line in myFile:
    info = line.split(",")
    name = info[0]
    runsAllowed = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]
    
    teamData.append([name,"",  runsAllowed, wins, losses, era])
    print(teamData)

  
  myFile.close()
  
  hitting = open("MLB_Hitting.csv", 'r')
  
  teamCount = 0
  for line in hitting:
    info = line.split(",")
    runsScored = info[3]
    #print(runsScored)
    teamData[teamCount][1] = runsScored
    print(teamData[teamCount])
    
    teamCount = teamCount + 1
    
  hitting.close()
  

  outFile = open("MLB_Output.csv", 'w')
  
  for line in teamData:
    output = line[0] + "," + line[1] + "," + line [3] + "," + line[4] + "," + line[5] + "\n"
    outFile.write(output)
  
  outFile.close()

if __name__ == '__main__':
  main()
