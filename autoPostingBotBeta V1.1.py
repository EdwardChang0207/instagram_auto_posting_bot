import os
import time
from time import sleep
from tkinter import *
from tkinter import ttk
from instagrapi import Client
from threading import Timer

#############################################################################################################################################
########################################################### INITIALIZE ######################################################################
#############################################################################################################################################


#Delete Config
try:
    os.remove('./config/edwardchang.here_uuid_and_cookie.json')
except:
    pass

##############################################################################################################################################
########################################################### INSTAGRAM BOT ####################################################################
##############################################################################################################################################

#def instabot
bot = Client()

#獲取帳號密碼
def getUserInfo():
    global userInfo
    userInfo=[accountEntry.get(), passwordEntry.get()]
    userinfoLabel = ttk.Label(topFrame, text='目前使用帳號為' + userInfo[0])
    userinfoLabel.pack()
    loginBtn = ttk.Button(topFrame, text='登入', command= login)
    loginBtn.pack()

#login function
def login():
    bot.login(username= userInfo[0], password= userInfo[1])
    if(login):
        print('success to login' + userInfo[0])
    else:
        print('fail to login' + userInfo[0])

#get img function
def getimgs():
    
    #var def
    global img1, Images
    
    #檢查檔案是否存在
    img1 = image1Entry.get().split( )
    Images = img1
    print(img1)

    #標記路徑
    for x in range(len(Images)):
        Images[x] = './img/' + Images[x]
    print(Images)

    #檢查是否為圖檔--未完成
    
    #檢查檔案數量
    log = 'reviced ' + str(len(Images)) + ' Images'
    print('reviced ' + str(len(Images)) + ' Images')
    #log
    logLabel = ttk.Label(inputFrame, text= log )
    logLabel.grid(row=8, column=0)

#get discription
def getdiscrpition():
#var def
    global discription
    discription = discrpitionEntry.get()
    if(len(discription) == 0):
        discription = ''
    print(discription)

#get tags
def getTag():
#var def
    global tags
    tags = tagEntry.get()
    if(len(tags) == 0):
        tags = ''
    print(tags)


#post function
def post():
    global doc
    print(discription + '\n' + tags )
    bot.album_upload(Images, caption= discription + '\n' + tags)

######################排程功能#####################

#getTime
def getScheduleTime():
    global scheduleTime
    scheduleTime = timeEntry.get()
    print('schedule time = ' + scheduleTime)

def getTimeNow():
    global timeNow
    timeNow = time.strftime('%m-%d %H:%M', time.localtime())
    print('the time is ' + timeNow)

def schedule():
    getScheduleTime()
    sleep(5)
    getTimeNow()
    sleep(5)
    getdiscrpition()
    sleep(5)
    getimgs()
    sleep(5)
    getTag()
    if timeNow != scheduleTime:
        getTimeNow
    if timeNow == scheduleTime:
        post()


##############################################################################################################################################
################################################################# GUI ########################################################################
##############################################################################################################################################

#GUI
window = Tk()
window.title('IG auto posting bot beta')
window.geometry('800x600')

#top
topFrame = ttk.Frame(window, width=800, height=300)
topFrame.grid(row=0, column=0)

#已排程事件-label
eventsLabel = ttk.Label(topFrame, text='已安排事件')
eventsLabel.pack(anchor= CENTER)

#已排程事件-Frame
eventFrame = ttk.Frame(topFrame,width=800,height=250)
eventFrame.pack(anchor= CENTER)


#bottom
bottomFrame = ttk.Frame(window, width=800, height=300)
bottomFrame.grid(row=1, column=0)

#inputFrame
inputLabel = ttk.Label(bottomFrame, text='輸入區')
inputLabel.pack(anchor= CENTER)
inputFrame = ttk.Frame(bottomFrame, width=800, height=300)
inputFrame.pack(anchor= CENTER)

#accountEntry
accountLabel = ttk.Label(inputFrame, text='帳號')
accountLabel.grid(row=0, column=0)
accountEntry = ttk.Entry(inputFrame)
accountEntry.grid(row=0, column=1)

#passwordEntry
passwordLabel = ttk.Label(inputFrame, text='密碼')
passwordLabel.grid(row=1, column=0)
passwordEntry = ttk.Entry(inputFrame)
passwordEntry.grid(row=1, column=1)

#imageEntry-1
image1Label = ttk.Label(inputFrame, text='圖片一')
image1Label.grid(row=2, column=0)
image1Entry = ttk.Entry(inputFrame)
image1Entry.grid(row=2, column=1)

#timeEntry
timeLabel = ttk.Label(inputFrame, text='時間')
timeLabel.grid(row=3, column=0)
timeEntry = ttk.Entry(inputFrame)
timeEntry.insert(END, 'mm-dd hh:mm')
timeEntry.grid(row=3, column=1)

#discriptionEntry
discrpitionLabel = ttk.Label(inputFrame, text='文案')
discrpitionLabel.grid(row=4, column=0)
discrpitionEntry = ttk.Entry(inputFrame)
discrpitionEntry.grid(row=4, column=1)

#tagEntry
tagLabel = ttk.Label(inputFrame, text='標籤')
tagLabel.grid(row=5, column=0)
tagEntry = ttk.Entry(inputFrame)
tagEntry.grid(row=5, column=1)

#submitBtn
submitBtn = ttk.Button(inputFrame, text='確認帳號', command= getUserInfo)
submitBtn.grid(row=6, column=0)

#img importBtn
imgImpotBtn = ttk.Button(inputFrame, text='載入圖片', command= getimgs)
imgImpotBtn.grid(row=6, column=1)

#discription importBtn
discriptionImpotBtn = ttk.Button(inputFrame, text='載入文案', command= getdiscrpition)
discriptionImpotBtn.grid(row=6, column=2)

#tag importBtn
tagImpotBtn = ttk.Button(inputFrame, text='載入標籤', command= getTag)
tagImpotBtn.grid(row=6, column=3)

#postBtn
postBtn = ttk.Button(inputFrame, text='發文', command= post)
postBtn.grid(row=7, column=0)

#gettimeBtn
getTimeBtn = ttk.Button(inputFrame, text='確認時間', command=getScheduleTime)
getTimeBtn.grid(row=7, column=1)

#scheduleBtn
scheduleBtn = ttk.Button(inputFrame, text='加入排程', command= schedule)
scheduleBtn.grid(row=7, column=2)



window.mainloop()

