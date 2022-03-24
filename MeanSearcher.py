import time
from bs4 import BeautifulSoup
import requests


def getSimpleMean(item):
    meanList = []
    link = "https://www.dict.com/ingilizce-turkce/{}".format(item)
    response = requests.get(link)
    bs = BeautifulSoup(response.content, 'html.parser')
    bs = bs.find_all("span", {"class": "lex_ful_tran w l2"})
    try:
        for i in range(5):
            meanList.append(bs[i].text)
    except:
        # print("SimpleMean Error")
        pass
    print(meanList)
    return meanList


def getMean(wrd):
    prep = []
    klmAnlm = []
    response = requests.get(
        "https://tureng.com/en/turkish-english/{}".format(wrd))
    bs = BeautifulSoup(response.content, 'html.parser')
    en = bs.find_all("td", {"class": "en tm"})
    tr = bs.find_all("td", {"class": "tr ts"})
    try:
        for i in range(4):
            isThere = False
            anlm = tr[i].find("a").text
            verb = en[i].find("i").text
            for x in prep:
                if(verb == x):
                    isThere = True
                    break
            if isThere == False:
                klmAnlm.append(anlm)
                prep.append(verb)
    except:
        print("Means Error")
    return(klmAnlm)


def getSynonyms(item):
    synonymsList = []
    link = "https://thesaurus.yourdictionary.com/{}".format(item)
    response = requests.get(link)
    bs = BeautifulSoup(response.content, 'html.parser')
    bs = bs.find_all("a", {"class": "synonym-link"})
    for i in range(5):
        synonymsList.append(bs[i].text)
    return synonymsList


def sentenceFinder(item):
    global wait
    if(len(item.split(" ")) > 1):
        par = item.split(" ")
        demoText = ""
        for j in par:
            if(j == par[-1]):
                break
            demoText = j + "%20"
        item = demoText
        link = "https://sentence.yourdictionary.com/search/result?q={}".format(
            item)
    else:
        item = item.replace(" ", "")
        link = "https://sentence.yourdictionary.com/{}".format(item)
    sentence_List = []
    preText = ""
    print(link)
    response = requests.get(link)
    bs = BeautifulSoup(response.content, 'html.parser')
    bs = bs.find_all("span", {"class": "sentence-item__text"})
    # print(bs)
    for i in range(3):
        sentence_List.append(bs[i].text)
    for i in sentence_List:
        preText += "➡️ " + i + "\n"
    if len(sentence_List) == 0:
        wait = "default"
        return "Kelimeyle ilgili veri bulunamadı"
    # for i in sentence_List:
        # preText = preText + "\n📌" + i["title"] + " ➡️ " + i["sentence"]
    simpleMean = f"🩸 Mean ➡️ {str(getSimpleMean(item))}"
    synm = f"🩸 Synms ➡️ {str(getSynonyms(item))}"
    mean = f"🩸 Tureng Means ➡️ {str(getMean(item))}"
    preText = "\n" + "📌 " + item + "\n" + simpleMean+"\n"+synm + "\n" + mean + "\n" + "\n" + preText + \
        "\n"
    print(preText)
    return preText


def wordListSearch():

    def getSimpleMean(item):
        meanList = []
        link = "https://www.dict.com/ingilizce-turkce/{}".format(item)
        response = requests.get(link)
        bs = BeautifulSoup(response.content, 'html.parser')
        bs = bs.find_all("span", {"class": "lex_ful_tran w l2"})
        try:
            for i in range(5):
                meanList.append(bs[i].text)
        except:
            # print("SimpleMean Error")
            pass
        print(meanList)
        return meanList

    def getMean(wrd):

        prep = []
        klmAnlm = []

        response = requests.get(
            "https://tureng.com/en/turkish-english/{}".format(wrd))
        bs = BeautifulSoup(response.content, 'html.parser')
        en = bs.find_all("td", {"class": "en tm"})
        tr = bs.find_all("td", {"class": "tr ts"})
        try:
            for i in range(4):
                isThere = False
                anlm = tr[i].find("a").text
                verb = en[i].find("i").text
                for x in prep:
                    if(verb == x):
                        isThere = True
                        break
                if isThere == False:
                    klmAnlm.append(anlm)
                    prep.append(verb)
        except:
            print("Means Error")
        return(klmAnlm)

    def getSynonyms(item):
        synonymsList = []
        link = "https://thesaurus.yourdictionary.com/{}".format(item)
        response = requests.get(link)
        bs = BeautifulSoup(response.content, 'html.parser')
        bs = bs.find_all("a", {"class": "synonym-link"})
        for i in range(5):
            synonymsList.append(bs[i].text)
        return synonymsList

    def sentenceFinder(item):
        global wait
        item = item.replace(" ", "")
        sentence_List = []
        preText = ""
        link = "https://sentence.yourdictionary.com/{}".format(item)

        response = requests.get(link)
        bs = BeautifulSoup(response.content, 'html.parser')
        bs = bs.find_all("span", {"class": "sentence-item__text"})
        # print(bs)
        for i in range(3):
            sentence_List.append(bs[i].text)
        for i in sentence_List:
            preText += "➡️ " + i + "\n"
        if len(sentence_List) == 0:
            wait = "default"
            return "Kelimeyle ilgili veri bulunamadı"
        # for i in sentence_List:
            # preText = preText + "\n📌" + i["title"] + " ➡️ " + i["sentence"]
        simpleMean = f"🩸 Mean ➡️ {str(getSimpleMean(item))}"
        synm = f"🩸 Synms ➡️ {str(getSynonyms(item))}"
        mean = f"🩸 Tureng Means ➡️ {str(getMean(item))}"
        preText = "\n" + "📌 " + item + "\n" + simpleMean+"\n"+synm + "\n" + mean + "\n" + "\n" + preText + \
            "\n"
        print(preText)
        file.write(preText)
        return preText
    words = open("word.txt", "r+", encoding="utf-8")
    allWords = words.readlines()
    file = open(
        f"{allWords[0].split('-')[0].split()[0]}.txt", "w+", encoding="utf-8")

    last = len(allWords)
    lastWords = []
    for i in allWords:
        lastWords.append(i.split("-")[0].split("\n")[0].split()[0])
    for i in lastWords:
        print(f"Last {last} - {i}")
        last -= 1
        try:
            sentenceFinder(i)
        except:
            print("Invalid Word, Sorry :(")

    words.close()
    file.close()


def fileChecker():
    try:
        file = open("word.txt", "r+")
        file.close()
    except:
        file = open("word.txt", "w+")
        file.close()
        print("Created Word List File")


while True:
    print("English Mean and Sentence Searcher")
    print("If there is any problem, report to insta: burakeyksl")
    print("""Select Your Operation
    1 - Search with a Word
    2 - Search with word List
    """)
    choice = input("Enter Your Choice: ")
    if(choice == "1"):
        cWord = input("Enter Your Word: ")
        print("-------------------------------------------------------------")
        try:
            sentenceFinder(cWord)
        except:
            print("Invalid Word, Sorry :(")
        print("-------------------------------------------------------------")
        time.sleep(2)
    elif(choice == "2"):
        fileChecker()
        print("Please enter your word list in word.txt file")
        time.sleep(2)
        print("If you ready to Search, press Enter")
        input()
        wordListSearch()
        print("------------------------------------------------------------")
        print("Success")
        time.sleep(1)
        quit()
