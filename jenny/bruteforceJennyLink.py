import random
import itertools

#  from selenium import webdriver
#  def openurlbrowser(url, driver):
    #  driver.get(url)
    #  return driver.getTitle("404")

#  import requests
#  def testUrlValidity(url):
    #  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    #  response = requests.get(url, headers=headers, timeout=3)
    #  return response

def genBadgesString():
    names = ["Goon", "Creator", "Speaker", "Artist", "Vendor", "Press"]
    answers = []
    answerl = list(itertools.permutations(names))
    for i in range(len(answerl)):
        answers.append("")
        for j in range(len(answerl[i])):
            answers[i] += answerl[i][j]
            if j == 3:
                answers[i] += "Human"
    return answers

import os

def main():
    #  numbers = 8675309
    #  driver = webdriver.Firefox(executable_path="./data/Drivers/geckodriver")
    baseurl = "https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/"
    BadgesStrings = genBadgesString()
    print("Number of Links to Test: ", len(BadgesStrings))
    #  with open("links.txt", 'w') as f:
        #  for i in range(len(BadgesStrings)):
            #  testurl = baseurl + BadgesStrings[i]
            #  f.write(testurl+"\n")
            #  openurlbrowser(testurl)
    for i in range(len(BadgesStrings)):
        testurl = baseurl + BadgesStrings[i]
        print(i)
        os.system("curl -I " + testurl)
        #  f.write(testurl+"\n")
        #  openurlbrowser(testurl)
    #  idx = 1
    #  while openurlbrowser(testurl, driver):
        #  print("Number of Links to Test: ", len(BadgesStrings)-idx)
        #  print("LinkNotValid")
        #  print(testurl)
    #  print("Link Valid")
    #  print(testurl)


if __name__ == '__main__':
    main()

