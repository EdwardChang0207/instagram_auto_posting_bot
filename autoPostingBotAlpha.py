import os
from time import sleep
import PIL.Image as Image
from tkinter import *
from tkinter import ttk
from instabot import Bot

#Delete Config
try:
    os.remove('./config/edwardchang.here_uuid_and_cookie.json')
except:
    pass

#def instabot
global bot
bot = Bot()

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
    bot.login(username = userInfo[0], password = userInfo[1])
    if(login):
        print('success to login' + userInfo[0])
    else:
        print('fail to login' + userInfo[0])

#get img function
def getimgs():
    
    #var def
    global img1, img2, Images
    
    #檢查檔案是否存在
    if(len(image1Entry.get()) > 4): 
        img1 = './img/' + image1Entry.get()
    else:
        img1 = False
    if(len(image2Entry.get()) > 4):
        img2 = './img/' + image2Entry.get()
    else:
        img2 = False    
    Images = [img1, img2]

    #檢查檔案數量
    if( img1 and img2):
        print('recive 2 imgs, ' + Images[0] + ',' + Images[1])
    elif(img1):
        print('recive 1 img, ' + Images[0])
    elif(img2):
        print('recive 1 img, ' + Images[1])
    else:
        print('ERROR!')
    open(img1)

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
    doc = discription+ '/n'+ tags
    print(doc)
    #for doc in doc.split('/n'):
        #print(doc)
    bot.upload_photo(Images, caption='test')

#GUI
window = Tk()
window.title('IG auto posting bot alpha')
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

#imageEntry-2
image2Label = ttk.Label(inputFrame, text='圖片二')
image2Label.grid(row=3, column=0)
image2Entry = ttk.Entry(inputFrame)
image2Entry.grid(row=3, column=1)

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
postBtn = ttk.Button(inputFrame, text='發文', command=post)
postBtn.grid(row=7, column=0)



window.mainloop()

