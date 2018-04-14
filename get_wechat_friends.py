import itchat
import math 
import PIL.Image as Image 
import os 
 
ISDIR1 = os.path.exists('./wechat_avatars')
print (ISDIR1)
if ISDIR1 != True:
    os.makedirs('./wechat_avatars')
else:
    print ("wechat_avatars is existed.")

ISDIR2 = os.path.exists('./one_avatar')
if ISDIR2 != True:
    os.makedirs('./one_avatar')
else:
    print ("one_avatar is existed.")

itchat.auto_login() 
friends = itchat.get_friends(update=True)[0:] 
user = friends[0]["UserName"] 

num = 0 
for i in friends: 
    istr = str(i)
    V_PROFILE = istr.split(',')
    NICKNAME = str(V_PROFILE[3])
    REMARKNAME = str(V_PROFILE[7])
    SIGNATURE = str(V_PROFILE[10])
    PROVINCE = str(V_PROFILE[21])
    CITY = str(V_PROFILE[22])
    print (NICKNAME[14:-1] + "--------" + REMARKNAME[16:-1] + "--------" + SIGNATURE[15:-1] + "--------" + PROVINCE[14:-1] + "--------" + CITY[10:-1])  #打印这行纯粹是为了让屏幕回显看当前进度，省得心里发闷不知道进行到了哪个用户，有这一行心情会大不一样！

#### 抓取用户信息记录到文本中 ################################################################################################
    USER_INFO = open('./User_Info.txt', 'a')
    USER_INFO.write(NICKNAME[14:-1] + "--------" + REMARKNAME[16:-1] + "--------" + SIGNATURE[15:-1] + "--------" + PROVINCE[14:-1] + "--------" + CITY[10:-1] + '\n')
#### 抓取用户信息并记录完毕 ############################################################################################################

#### 抓取所有用户头像为 jpg 格式图片，无 Alpha 通道，所以个别有个性的用户使用的透明图片无法抓取 ##############################
    img = itchat.get_head_img(userName=i["UserName"]) 
    fileImage_pinjie = open('./one_avatar' + "/" + str(num) + ".jpg",'wb') 
    fileImage_pinjie.write(img) 
    fileImage_pinjie.close() 
    fileImage = open('./wechat_avatars' + "/" + NICKNAME[14:-1] + "--------" + REMARKNAME[16:-1] + ".jpg",'wb') 
    fileImage.write(img) 
    fileImage.close() 
    num += 1 
#### 抓取头像完毕 ############################################################################################################

#### 以上可运行,加上以下一段可拼接所有头像为一张 2560*2560 大图 ##############################################################
ls = os.listdir('./one_avatar')
each_size = int(math.sqrt(float(2560*2560)/len(ls)))
lines = int(2560/each_size)
#image = Image.new('RGBA', (640, 640))
image = Image.new('RGB', (2560, 2560))
x = 0
y = 0
for i in range(0,len(ls)+1):
    try:
        img = Image.open('./one_avatar' + "/" + str(i) + ".jpg")
    except IOError:
        print("Cannot Read avatar" + " " + str(i) + ".jpg")
    else:
        img = img.resize((each_size, each_size), Image.ANTIALIAS)
        image.paste(img, (x * each_size, y * each_size))
        x += 1
        if x == lines:
            x = 0
            y += 1
image.save('./one_avatar' + "/" + "all.jpg")
itchat.send_image('./one_avatar' + "/" + "all.jpg", 'filehelper')
#### 拼接头像完毕 ############################################################################################################
