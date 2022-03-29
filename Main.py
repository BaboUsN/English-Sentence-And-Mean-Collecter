import time
import Multi
import Single


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
            Single.sentenceFinder(cWord)
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
        Multi.wordListSearch()
        print("------------------------------------------------------------")
        print("Success")
        time.sleep(1)
        quit()
