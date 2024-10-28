def main():
  myFile = open("ufo_sightings.csv", 'r')

  """for line in myFile:
    print (line)                    """

  for line in myFile:
    info = line.split(" , ")
    
    print(line)

  
  myFile.close()


if __name__ == '__main__':
  main()
