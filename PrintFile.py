def main():
  myFile = open("qbdata.txt", 'r')

  """for line in myFile:
    print (line)                    """

  for line in myFile:
    info = line.split(" ")
    td = info[9]
    name = info[0]
    rating = info[11]
    print(name,  "had a rating of", rating , "and threw", td, "touchdowns.")

  
  myFile.close()


if __name__ == '__main__':
  main()
