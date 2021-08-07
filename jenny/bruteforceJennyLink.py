import random
import itertools
import os

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

def main():
    #  numbers = 8675309
    baseurl = "https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/"
    BadgesStrings = genBadgesString()
    print("Number of Links to Test: ", len(BadgesStrings))
    for i in range(len(BadgesStrings)):
        testurl = baseurl + BadgesStrings[i]
        print(i)
        os.system("curl -I " + testurl)

if __name__ == '__main__':
    main()

