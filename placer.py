from bs4 import BeautifulSoup
import requests
import time
import pyautogui as py
import pyperclip


def getMean(wrd):

    prep = []
    klmAnlm = []

    response = requests.get(
        "https://tureng.com/en/turkish-english/{}".format(wrd))
    bs = BeautifulSoup(response.content)
    en = bs.find_all("td", {"class": "en tm"})
    tr = bs.find_all("td", {"class": "tr ts"})
    for i in range(len(en)-1):
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
    return(klmAnlm)

#     pyautogui.write(i)
#     pyautogui.press("tab")
#     pyautogui.press("tab")


def createCard(a):
    py.click(x=446, y=62)
    py.hotkey('ctrl', 'a')
    py.press("delete")
    py.write("https://quizlet.com/create-set")
    py.press("enter")
    time.sleep(3)
    py.click(x=339, y=442)  # enter term
    py.hotkey("ctrl", "a")
    py.press("delete")
    py.write(f"Fast Days {a} - ENG Words")
    time.sleep(1)
    py.click(x=691, y=1057)  # enter term


fileName = input("file name : ")
doc = open(f"{fileName}.txt", "r+")
words = doc.readlines()
newList = words.copy()
# print(words.index("mall\n"))

# createCard(a)
time.sleep(2)
for i in words:
    py.hotkey("ctrl", "a")
    py.press("delete")
    pyperclip.copy(newList[words.index(i)][0:-1])
    py.hotkey("ctrl", "v")
    py.press("tab")
    py.hotkey("ctrl", "a")
    py.press("delete")
    # pyperclip.copy(str(getMean(newList[words.index(i)][0:-1])))
    # py.hotkey("ctrl", "v")
    py.press("tab")

doc.close()
