from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=us+election+results&oq=&aqs=chrome.5.35i39i362l6j46i39i362l2...8.1411738829j0j15&sourceid=chrome&ie=UTF-8')

while(True):
    votes = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div[1]/div/div[2]/span')
    votes = int(votes.text)
    print('Biden: electoral votes: ' + str(votes))
    if votes >= 270:
        print("Biden won")
        from playsound import playsound
        playsound('alarm.mp3')
        break
    else :
        voteToWin = 270 - votes
        print(str(voteToWin) + ' more electoral votes to win\n')
    time.sleep(300)
    driver.refresh()




