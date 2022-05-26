from rubika.encryption import encryption
from json import dumps,loads
from random import randint
from requests import post
from re import findall
from threading import Thread
from datetime import datetime
from rubika.client import Bot, Socket
import requests
from requests import get
from re import findall
import os
import glob
from rubika.client import Bot
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import time
import random
import urllib
import io
import json
from random import choice
from PIL import Image
from requests import post
from random import randint
from json import loads, dumps
import asyncio,base64,glob,json,math,urllib3,os,pathlib,random,rubika.__pycache__,sys,concurrent.futures,time
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests import get
from re import findall
from requests import post
import time
from PIL import Image
from json import loads
from gtts import gTTS
from mutagen.mp3 import MP3
import io
from requests import get
from re import findall
import base64
import concurrent.futures
import datetime
import glob
import json
import math
import os
import pathlib
import random
import sys
import time
from json import dumps, loads
from random import randint
import re
from re import findall
import requests
import urllib3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from requests import post
from googletrans import Translator
import io
from PIL import Image , ImageFont, ImageDraw 
import arabic_reshaper
from mutagen.mp3 import MP3
from gtts import gTTS
from threading import Thread
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from rubika.client import Bot
from json import load , dump
import time
from mutagen.mp3 import MP3
from os import system
from time import sleep
from requests import get
from re import findall
from requests import post
import time
from PIL import Image
from json import loads
from gtts import gTTS
from mutagen.mp3 import MP3
import io
from random import choice
from requests import post
from PIL import Image
from mutagen.mp3 import MP3
from json import load , dump
import time
from mutagen.mp3 import MP3
from os import system
from time import sleep
from requests import get
from re import findall
from requests import post
import time
from PIL import Image
from json import loads
from gtts import gTTS
from mutagen.mp3 import MP3
import io
from random import choice
from requests import post
from PIL import Image
from mutagen.mp3 import MP3

bot = Bot("AppName", auth="dulqymywasljhepdqxarklmqsbegtgfo")
target = "g0B8eMF0ce5c0a20eeb61840dae46e4f"

channell = "c0BCZ6p0f50023af73937b9c76a9699c"
bot.sendPhoto(target, '/storage/emulated/0/now.png',caption=  f"محمد بات با موفقیت در گروه فعال شد 😍🕺")

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me","www."]
	for i in links:
		if i in msg:
			return True


def searchUserInGroup(guid):
	user = bot.getUserInfo(guid)["data"]["user"]["username"]
	members = bot.getGroupAllMembers(user,target)["in_chat_members"]
	if members != [] and members[0]["username"] == user:
		return True
# static variable
answered, sleeped, retries = [], False, {}

# option lists
blacklist, exemption, auto_lock , no_alerts , no_stars =  [] , [] , False , [] , []
alerts, stars = {} , {}
auto_lock , locked , gif_lock = False , False , False


# alert function
def alert(guid,user,alert_text=""):
	no_alerts.append(guid)
	alert_count = int(no_alerts.count(guid))

	alerts[user] = alert_count

	max_alert = 5    # you can change it


	if alert_count == max_alert:
		blacklist.append(guid)
		bot.sendMessage(target, "\n 🚫 کاربر [ @"+user+" ] \n ("+ str(max_alert) +") اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .", msg["message_id"])
		bot.banGroupMember(target, guid)
		return

	for i in range(max_alert):
		no = i+1
		if alert_count == no:
			bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n\n"+ str(alert_text) +" شما ("+ str(no) +"/"+ str(max_alert) +") اخطار دریافت کرده اید .\n\nپس از دریافت "+ str(max_alert) +" اخطار ، از گروه اخراج خواهید شد .", msg["message_id"])
			return

# star function
def star(guid,user):
	no_stars.append(guid)
	star_count = int(no_stars.count(guid))
	stars[user] = star_count

	bot.sendMessage(target, "⭐ کاربر @"+ user +" امتیاز دریافت کرد .\n\nتعداد امتیاز های کاربر تا این لحظه = "+ str(star_count), msg["message_id"])
retries = {}
sleeped = False
# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]
plus= True

while True:
	if auto_lock:
		if not locked and time.localtime().tm_hour == 00:
			bot.setMembersAccess(target, ["AddMember"])
			bot.sendMessage(target, "⏰ زمان قفل خودکار گروه فرا رسیده است .\n - گروه تا ساعت [ 08:00 ] تعطیل می باشد .")
			locked , sleeped = True , True

		if locked and time.localtime().tm_hour == 8:
			bot.setMembersAccess(target, ["SendMessages","AddMember"])
			bot.sendMessage(target, "⏰ زمان قفل خودکار گروه به پایان رسیده است .\n - اکنون اعضا می توانند در گروه چت کنند .")
			locked , sleeped = False , False		


	# time.sleep(15)
	try:

		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		with open("learn.json","r",encoding="utf-8") as learn:
			data = load(learn)

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				# Check Bot is Sleeped or Not
				if not sleeped:

					# Get Text Messages
					if msg["type"]=="Text" and not msg["message_id"] in answered:

							
						   
						if msg["author_object_guid"] in admins:

							if msg["text"] == "ربات خاموش" or msg["text"] == "/sleep" :
								sleeped = True
								bot.sendMessage(target, "💤 ربات اکنون خاموش است .", msg["message_id"])
							elif msg["text"] == "!start" or msg["text"] == "/start" :
								bot.sendMessage(target, "✨ربات محمد فعال شد، کلمه (دستورات) را ارسال کنید .", msg["message_id"])	     
							elif msg.get("text").startswith("دانش") or msg.get("text").startswith("danestani") or msg.get("text").startswith("!danestani"):
						
						           try:
							           response = get("https://api.codebazan.ir/danestani/").text
							           bot.sendMessage(target, response,message_id=msg.get("message_id"))
						           except:
							           bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])	     	
							elif msg.get("text").startswith("بفرست"):
							    try:
								    if msg.get('reply_to_message_id') != None:
									    bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									    if bego2['text'] != None:
										    textss= bego2['text']
										    kanal = textss
										    bot.sendMessage(channell, kanal)
										    print('error Channel')
								    else:
									    bot.sendMessage(target, 'رو پیامی که میخواهید به کانالتان ارسال شود ریپ زنید❌',message_id=msg["message_id"])
							    except:
								    print('error Channel')
							elif msg.get("text") == "بات"and msg.get("author_object_guid") :
							    try:
							    	bot.sendPhoto(target, 'https://s6.uupload.ir/files/robo_y9pr.jpg', caption=f"جون ربات عشقم", message_id=msg.get("message_id"))
							    	print(SEND)
							    except:
							        print(error)
							
							elif msg.get("text") == "ربات":
								try:
									ans = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n جان کاری داشتید","🎓\n🙂\n🧥\n👖 \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩"]
									
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
								except:
									bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text").startswith("عکس جستجو") or msg.get("text").startswith("webshot") or msg.get("text").startswith("!webshot"):						
						           try:
							            args = msg['text'].split()[1]
							            if '.ir' in args:
								            response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							            else:
								            response = get("https://http.cat/403").content
							            with open("shot.jpg","wb") as shot: shot.write(response)
							            bot.sendPhoto(target, "./shot.jpg", [720,720], caption="نمایی از صفحه موردنظر شما", message_id=msg["message_id"])
						           except: 
						                bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])
							elif msg.get("text").startswith("!p_danesh"):
						         try:
							         args = msg['text'].split()[1]
							         if '.ir' in args:
								         response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							         else:
								         response = post("http://api.codebazan.ir/danestani/pic").content
							         with open("shot.jpg","wb") as shot: shot.write(response)
							         bot.sendPhoto(target, "./shot.jpg", [720,40], caption="محمدبات", message_id=msg["message_id"])
						         except:
							         bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							    try:
								    bot.pin(target, msg["reply_to_message_id"])
								    bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							    except:
								    print("err pin")
							
							
							elif msg.get("text") == "ویسکال" and msg.get("author_object_guid") in admins :
							     try:
								     bot.startVoiceChat(target,)
								     bot.sendMessage(target, "ویسکال با موفقیت ایجاد شد✔️", message_id=msg.get("message_id"))
							     except:
								     print("err Voice Chat")
							elif msg.get("text") == "محمدبات":
					     			user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
					     			text = f"جـــونــم {user} عــزیـزم🙂🌹"
					     			bot.sendMessage(target, text, message_id=msg.get("message_id"))
							
							elif msg["text"].startswith("یادبگیر") or msg["text"].startswith("/learn"):
								try:
									text = msg["text"].replace("یادبگیر ","").replace("/learn ","").split(":")
									word = text[0]
									answer = text[1]

									data[word] = answer
									with open("learn.json","w",encoding="utf-8") as learn:
										dump(data, learn)

									bot.sendMessage(target, "✅ ذخیره شد", msg["message_id"])
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])						    			    
							
							elif msg.get("text") == "بابات کیه"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "محمد عشقم", message_id=msg.get("message_id"))
							elif msg.get("text") == "خوبی":
						         try:							
							         ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")			    			    							    			        
							elif msg.get("text") == "پسرم"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "چیه پدر عزیزم", message_id=msg.get("message_id"))							    			    						
							elif msg.get("text") == "بای"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "خدافز عچقم😍🗿", message_id=msg.get("message_id"))
								
							elif msg.get("text") == "ایموجی":
								try:
									ans = ["😀","😃","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","🤬","☹️","🙁","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","🤤","🥱","😴","😪","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","😇","🤠","🤑","😎","🤓","🤥"]
									renn= choice(ans)
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
									bot.sendDocument(target,"/storage/emulated/0/mamadbot.mp4", caption= f"{renn}")
								except:
									 bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام"):
							    try:
								    guidr= msg.get("author_object_guid")
								    textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
								    taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
								    ren= choice(taf)
								    f = open('/storage/emulated/0/Download/arianbot/arianbot/hello.jpg')
								    p = Image.open('hello.jpg')
								    bot.sendPhoto(target, 'hello.jpg', p.size,caption=  f"علیک {textw} {ren}")
							    except:
								    print("err hello")
							elif msg.get("text") == "قلب":
								try:
									ans = ["❤️","🧡","💛","💚","💙","💜","🤎","🖤","🤍","♥️","💘","💝","💖","💗","💓","💞","💕","💟","❣️","💔"]
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
								except:
									 bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text") == "صلم":
						         try:							
							         ans = ["سلام عزیزم😋💛", "سلام گوگولی من😄❤️","سلام عجقم🤤🌹","سپاس صلم عشقم🌺","سلام خوبی چیکار میکنی 😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg.get("text") == "خبی":
						         try:							
							         ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg["text"].startswith("افزودن ادمین") or msg["text"].startswith("/add_admin") :

								try:
									user = msg["text"].replace("افزودن ادمین ","").replace("/add_admin ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									
									if not guid in admins :
										bot.setGroupAdmin(target, guid)
										bot.sendMessage(target, "✅ کاربر @"+ str(user) +" با موفقیت ادمین شد .", msg["message_id"])
									else:
										bot.sendMessage(target, "❌ کاربر هم اکنون ادمین میباشد", msg["message_id"])

								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]
										
										if not guid in admins :
											bot.setGroupAdmin(target, guid)
											bot.sendMessage(target, "✅ کاربر @"+ str(user) +" با موفقیت ادمین شد .", msg["message_id"])
										else:
											bot.sendMessage(target, "❌ کاربر هم اکنون ادمین میباشد", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
                            
							elif msg["text"].startswith("حذف ادمین") or msg["text"].startswith("/del_admin") :
								try:
									user = msg["text"].replace("حذف ادمین ","").replace("/del_admin ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]

									if guid in admins :
										bot.deleteGroupAdmin(target, guid)
										bot.sendMessage(target, "✅ کاربر @"+ str(user) +" با موفقیت از ادمینی برکنار شد .", msg["message_id"])
									else:
										bot.sendMessage(target, "❌ کاربر ادمین گروه نمیباشد", msg["message_id"])

								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]

										if not guid in admins :
											bot.setGroupAdmin(target, guid)
											bot.sendMessage(target, "✅ کاربر @"+ str(user) +" با موفقیت از ادمینی برکنار شد .", msg["message_id"])
										else:
											bot.sendMessage(target, "❌ کاربر ادمین گروه نمیباشد", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
						      			
							elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						         try:
							         response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							         bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							         bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
						         except:
							          bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
							elif msg.get("text").startswith("بورس"):
							    try:
								    response = get("https://api.codebazan.ir/bours/").text
								    bot.sendMessage(target, response,message_id=msg.get("message_id"))
							    except:
								    bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])			
							elif msg.get("text").startswith("ترجمه"):
						         try:
							         responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							         al = [responser["result"]]
							         bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							         bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						         except:
							          bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							elif msg["text"].startswith("معاف") :
								try:
									guid = bot.getInfoByUsername(msg["text"].replace("معاف ","")[1:])["data"]["chat"]["abs_object"]["object_guid"]
									if not guid in admins :
										if not guid in exemption:
											exemption.append(guid)
											bot.sendMessage(target, "✅ کاربر با موفقیت معاف شد .", msg["message_id"])
										else:
											bot.sendMessage(target, "❌ کاربر هم اکنون معاف میباشد .", msg["message_id"])
								
									else :
										bot.sendMessage(target, "❌ کاربر ادمین میباشد .", msg["message_id"])
										
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										if not guid in admins:
											if not guid in exemption:
												exemption.append(guid)
												bot.sendMessage(target, "✅ کاربر با موفقیت معاف شد .", msg["message_id"])
											else:
												bot.sendMessage(target, "❌ کاربر هم اکنون معاف میباشد .", msg["message_id"])

										else :
											bot.sendMessage(target, "❌ کاربر ادمین میباشد .", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text").startswith("شماره") :
						         bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["phone"]["chat"]["object_guid"], "{phone}"+" ".join(msg.get("text").split(" ")[2:]))
						         bot.sendMessage(target, "شمارت ارسال شد.", message_id=msg.get("target=phone_id"))
							elif msg["text"].startswith("جوین") or msg["text"].startswith("شو"):
								try:
									text = str(msg["text"].replace("جوین","").replace("شو",""))

									bot.joinGroup(str(text))
									bot.sendMessage(target,"در گروه "+str(text)+ " شدم", message_id=msg.get("message_id"))

								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "بگو":
								try:
									if msg.get('reply_to_message_id') != None:
										msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
									else:
										bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
								except:
									print('server gtts bug')
							elif msg["text"].startswith("حذف معاف") :
								try:
									guid = bot.getInfoByUsername(msg["text"].replace("حذف معاف ","")[1:])["data"]["chat"]["abs_object"]["object_guid"]
									if not guid in admins :
										if guid in exemption:
											exemption.remove(guid)
											bot.sendMessage(target, "✅ کاربر از معافیت حذف شد", msg["message_id"])
										else:
											bot.sendMessage(target, "❌ کاربر معاف نمیباشد .", msg["message_id"])
									else :
										bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
										
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										if not guid in admins and guid in exemption:
											if guid in exemption:
												exemption.remove(guid)
												bot.sendMessage(target, "✅ کاربر با از معافیت حذف شد", msg["message_id"])
											else:
												bot.sendMessage(target, "❌ کاربر معاف نمیباشد .", msg["message_id"])

										else :
											bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
									
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])			
							
							elif msg.get("text") == "عجب"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "آره داپش عجب", message_id=msg.get("message_id"))
        
							elif msg.get("text") == "هعی"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "آری داپش هعی🗿🚬", message_id=msg.get("message_id"))
							elif msg["text"] == "لیست امتیاز" or msg["text"] == "/star_list":
								try:
									text = "💎 لیست امتیازات کاربران گروه :\n\n"
									stars_list = ""
									for i in stars:
										stars_list += (" - @"+i+" \t= "+str(stars[i])+"\n")
									bot.sendMessage(target, text + str(stars_list), msg["message_id"])
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
								
							elif msg.get("text").startswith("هلیکوپتر") :
						                   bot.sendMessage(target, "▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄◢◤╬\n█▄ ██▄ ███▀▀▀▀▀▀\n◥█████◤\n══╩══╩═\nاینم از هلیکوپتر😅", message_id=msg.get("message_id"))		
							elif msg.get("text") == "کص" or msg.get("text") == "کیر" or msg.get("text") == "کوص" or msg.get("text") == "کیری" or msg.get("text") == "گاییدم" or msg.get("text") == "خارکسده" or msg.get("text") == "خایه" or msg.get("text") == "جق" or msg.get("text") == "کصکش":
							    try:
								    bot.deleteMessages(target, message_id=msg.get("message_id"))
								    bot.sendMessage(target, "بی تر ادب", message_id=msg.get("message_id"))
							    except:
								    print("err delete fesh")

							elif msg.get("text").startswith("اخبار"):
								try:
									response = get("https://api.codebazan.ir/khabar/?kind=iran").json
									bot.sendMessage(target, response,message_id=msg.get("message_id"))
								except:
									bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
							elif msg.get("text").startswith("بازی") or msg.get("text").startswith("جرعت حقیقت") or msg.get("text").startswith("ج ح"):
								rules = open("jorat.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							elif msg.get("text").startswith("اپدیت بازی") and msg.get("author_object_guid") in admins:
								try:
									rules = open("jorat.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت بازی")))
									bot.sendMessage(target, "بازی با موفقیت بروزرسانی شد.", message_id=msg.get("message_id"))
								
								except:
									bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))
							elif msg.get("text").startswith("جستجو") or msg.get("text").startswith("!search") or msg.get("text").startswith("search"):
						          try:
							          search = msg.get('text').split()[1]                             
							          jd = loads(get('https://zarebin.ir/api/?q=' + search + '&page=1&limit=10').text)
							          results = jd['results']['webs']
							          text = ''
							          for result in results:
								          text += result['title'] + ':\n\n  ' + str(result['description']).replace('</em>', '').replace('<em>', '').replace('(Meta Search Engine)', '').replace('&quot;', '').replace(' — ', '').replace(' AP', '') + '\n\n'  
							          bot.sendMessage(target, 'نتایج کامل به پیوی شما ارسال شد', message_id=msg["message_id"])
							          bot.sendMessage(msg['author_object_guid'], 'نتایج یافت شده برای (' + search + ') : \n\n'+text)
						          except:
							          print('zarebin search err')	
							elif msg.get("text") == "برسی":
							    try:
								    GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								    guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								    useru = bot.getUserInfo(guidu)["data"]["user"]["username"]
								    if not guidu in admins:
									    bot.sendMessage(target, f"کاربر {useru} یک شخص عادی در گروه {GAPE} می باشد", message_id=msg.get("message_id"))
								    else:
									    bot.sendMessage(target, f"کاربر {useru} در گروه {GAPE} آدمین می باشد", message_id=msg.get("message_id"))
							    except:
								    print('analiz user')
							elif msg.get("text") == "تبلیغات روشن":
							    try:
								    bot.sendMessage(target, "🤖در پیام بعدی لینک گروه مورد نظر را ثبت نمائید🤖\nمثال:\n\nجوین گروه\nhttps://rubika.ir/joinc/BEDJEHGJ0LXSIPACCXGCQCBIJBZESKWA")
							    except:
								    print("error ersal start1")
							elif msg.get("text").startswith("جوین گروه"):
							    try:
								    yourlink = open("target.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								    bot.sendMessage(target,  "✅ با موفقیت لینک گروه مورد نظر ثبت شد")
								    bot.sendMessage(target,  "\n🤖بنر خود را برای تبلیغات در پیام بعدی ثبت نمائید🤖\n\nمثال رو پیامی که می خواهید پخش شود ریپ بزنید و بگویید [ ثبت تبلیغ ]\n")
							    except:
								    print("error sabt_link-tabligh")
							elif msg.get("text").startswith("ثبت تبلیغ"):
							    try:
								    if msg.get('reply_to_message_id') != None:
									    banner = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									    if banner['text'] != None:
										    matnbanner= banner['text']
										    matntabligh = open("matnTABLIGH.txt","w",encoding='utf-8').write(str(matnbanner))
							    except:
								    bot.sendMessage(target, "✅  \n\nمتن مورد نظر برای تبلیغات ثبت شد\nبرای شروع تبلیغات [ تبلیغ کن ] را وارد کنید", message_id=msg.get("message_id"))
							    
							elif msg.get("text").startswith("تبلیغ کن"):
							    while True:
								    sleep(5)
								    tabyligh = open("matnTABLIGH.txt","r",encoding='utf-8').read()
								    tabgligh = open("target.txt","r",encoding='utf-8').read()
								    tabeligh = bot.joinGroup(tabgligh)
								    tabrligh = tabeligh['data']['group']['group_guid']
								    bot.sendMessage(tabrligh,tabyligh)
								    bot.leaveGroup(tabrligh)
							elif msg.get("text").startswith("شات") or msg.get("text").startswith("!shot") or msg.get("text").startswith("shot"):
						            if msg.get('reply_to_message_id') != None:
							            msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							            if msg_reply_info['text'] != None:
								            text = msg_reply_info['text']
								            res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								            if res.status_code == 200 and res.content != b'':
									            b2 = res.content
									            print('get the image')
									            f = open('image.jpg','wb')
									            f.write(b2)
									            f.close()
									            p = Image.open('image.jpg')
									            bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg["message_id"])
								            else:
									            bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg["message_id"])
							            else:
								            bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
						            else:
							            bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg["message_id"])
							elif msg["text"].startswith("arz"):
							    try:
								    response = get(f"http://api.codebazan.ir/arz/?type={msg['text'].split()[1]}").json()
								    bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:50])).text
								    bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							    except:
								    bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
							elif msg.get("text").startswith("!trans"):
							    try:
								    responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								    al = [responser["result"]]
								    bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								    bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							    except:
								    bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
							elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							    try:
								    rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								    renn= choice(rew)
								    bot.sendDocument(target,"/storage/emulated/0/ARIANBOT.mp4", caption= f"{renn}")
							    except:
								    print("err bot answer")
							elif msg.get("text").startswith("پسورد"):
							    try:
								    response = get(f"http://api.codebazan.ir/password/?length={msg['text'].split()[1]}").text
								    bot.sendMessage(target, response,message_id=msg.get("message_id"))
							    except:
								    bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])
							elif msg.get("text").startswith("send"):

							    try:

								    if msg.get('reply_to_message_id') != None:

									    befrest = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]

									    if befrest['text'] != None:

										    texts= befrest['text']

										    usersendmatn = msg.get("text").split(" ")[1][1:]

									    bot.sendMessage(bot.getInfoByUsername(usersendmatn)["data"]["chat"]["abs_object"]["object_guid"],texts)

							    except:

								    print("err send_massage_be_id")
								
							
							elif msg.get("text") == "برسی":
							    try:
								    GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								    guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								    useru = bot.getUserInfo(guidu)["data"]["user"]["username"]
								    if not guidu in admins:
									    bot.sendMessage(target, f"کاربر {useru} یک شخص عادی در گروه {GAPE} می باشد", message_id=msg.get("message_id"))
								    else:
									    bot.sendMessage(target, f"کاربر {useru} در گروه {GAPE} آدمین می باشد", message_id=msg.get("message_id"))
							    except:
								    print('analiz user')
							elif msg.get("text").startswith("بگو"):
							    try:
								    if msg.get('reply_to_message_id') != None:
									    bego1 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									    if bego1['text'] != None:
										    texts= bego1['text']
										    bot.sendMessage(target,texts, message_id=msg.get("message_id"))
										    print('error begho')
								    else:
									    bot.sendMessage(target, 'رو متن مورد نظر ریپ نزدید❌',message_id=msg["message_id"])
							    except:
								    print('error begho')
							elif msg.get("text").startswith("پینگ"):
						
						         try:
							         responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							         bot.sendMessage(target, responser,message_id=msg["message_id"])
						         except:
							         bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							if  msg.get("text").startswith('!user @'):
								try:
									user_info = bot.getInfoByUsername( msg.get("text")[7:])
									if user_info['data']['exist'] == True:
										if user_info['data']['type'] == 'User':
											bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
											print('sended response')
										else:
											bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
											print('sended response')
									else:
										bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
										print('sended response')
								except:
									print('server bug6')
									bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							elif msg.get("text") == "حق"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "آره داپش حق 🗿👌", message_id=msg.get("message_id"))
							elif msg["text"] == "لیست اخطار" or msg["text"] == "/alert_list":
								try:
									text = "⚠ لیست اخطارهای کاربران گروه :\n\n"
									alert_list = ""
									for i in alerts:
										alert_list += (" - @"+i+" \t= "+str(alerts[i])+"\n")
									bot.sendMessage(target, text + str(alert_list), msg["message_id"])
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])

							elif msg.get("text") == "😂"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "چرا میخندی سید چه خنده دار بود 🗿", message_id=msg.get("message_id"))
							elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							      try:
								      response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								      bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20000000000000000000000])).text
								      bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							      except:
								         bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
							elif msg["text"].startswith("حذف اخطار") or msg["text"].startswith("/del_alert"):
								try:
									user = msg["text"].replace("حذف اخطار ","").replace("/del_alert ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									
									if guid in no_alerts:
										for i in range(no_alerts.count(guid)):
											no_alerts.remove(guid)
										alerts[user] = 0
										bot.sendMessage(target, "✅ اخطارهای کاربر حذف شد .", msg["message_id"])
									else:
										bot.sendMessage(target, "❌ کاربر اخطاری ندارد .", msg["message_id"])
										
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]

										if guid in no_alerts:
											for i in range(no_alerts.count(guid)):
												no_alerts.remove(guid)
											alerts[user] = 0
											bot.sendMessage(target, "✅ اخطارهای کاربر حذف شد .", msg["message_id"])
										else:
											bot.sendMessage(target, "❌ کاربر اخطاری ندارد .", msg["message_id"])

									except:
										bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", msg["message_id"])	         
							
							elif msg.get("text").startswith("ترجمه"):					
								try:
									responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
									al = [responser["result"]]
									bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
									bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
								except:
									bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							      try:
								      response = get("http://api.codebazan.ir/hadis/").text
								      bot.sendMessage(target, response,message_id=msg.get("message_id"))
							      except:
								        bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])          	
							elif msg.get("text").startswith("دعوت ") :
						                        bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "https://rubika.ir/joing/CBEICAHA0XPEKOMJOTNWMBCFPQULKDHO\nسلام کاربر گرامی شما به گروه ما دعوت شدید❤️☘\nراستی قوانین گپ را رعایت کن✅\nفحش=ریمو❌\nناسزاگویی=ریمو❌\nشاخ=ریمو❌\nاسپم=ریمو❌\nکد هنگی=ریمو❌\nممنون میشیم وارد گروهمون شوید❤️\nعشــــــــــــــــــــــــــــــــــــــقی❤️💐"+" ".join(msg.get("text").split(" ")[2:]))
						                        
						                        bot.sendMessage(target, "‌‌د‌عوت نامه شما با موفقیت ارسال گشت.", message_id=msg.get("message_id"))	
							elif msg["text"].startswith("اخطار")  or msg["text"].startswith("/alert"):
								try:
									user = msg["text"].replace("اخطار ","").replace("/alert ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									
									if not guid in admins :
										alert(guid,user)
									else :
										bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
										
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]
										if not guid in admins:
											alert(guid,user)
										else:
											bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							    try:
								    response = get("http://api.codebazan.ir/dastan/").text
								    bot.sendMessage(target, response,message_id=msg.get("message_id"))
							    except:
								     bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])	 			
							
							elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							     try:
								     response = get("https://api.codebazan.ir/bio/").text
								     bot.sendMessage(target, response,message_id=msg.get("message_id"))
							     except:
								      bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])
							
							elif msg.get("text").startswith("جوک"):
						         try:
							         response = get("https://api.codebazan.ir/jok/").text
							         bot.sendMessage(target, response,message_id=msg.get("message_id"))
						         except:
							          bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							elif msg.get("text").startswith("آیه_الکرسی") :
						         bot.sendMessage(target, "ب‍‌ِس‍‌م‍ِ اللهِ ال‍‌رَّح‍‌م‍‌ن ال‍‌رَّح‍‌ی‍‌م‍ِ\n\nاللّهُ لاَ إِلَهَ إِلاَّ هُوَ الْحَیُّ الْقَیُّومُ لاَ تَأْخُذُهُ سِنَهٌ وَ لاَ نَوْمٌ لَّهُ مَا فِی السَّمَاوَاتِ وَمَا فِی الأَرْضِ مَن ذَا الَّذِی یَشْفَعُ عِنْدَهُ إِلاَّ بِإِذْنِهِ یَعْلَمُ مَا بَیْنَ أَیْدِیهِمْ وَمَا خَلْفَهُمْ وَ لاَ یُحِیطُونَ بِشَیْءٍ مِّنْ عِلْمِهِ إِلاَّ بِمَا شَاء وَسِعَ کُرْسِیُّهُ السَّمَاوَاتِ وَ الأَرْضَ وَ لاَ یَۆُودُهُ حِفْظُهُمَا وَ هُوَ الْعَلِیُّ الْعَظِیمُ لاَ إِکْرَاهَ فِی الدِّینِ قَد تَّبَیَّنَ الرُّشْدُ مِنَ الْغَیِّ فَمَنْ یَکْفُرْ بِالطَّاغُوتِ وَ یُۆْمِن بِاللّهِ فَقَدِ اسْتَمْسَکَ بِالْعُرْوَهِ الْوُثْقَیَ لاَ انفِصَامَ لَهَا وَاللّهُ سَمِیعٌ عَلِیمٌ اللّهُ وَلِیُّ الَّذِینَ آمَنُواْ یُخْرِجُهُم مِّنَ الظُّلُمَاتِ إِلَی النُّوُرِ وَالَّذِینَ کَفَرُواْ أَوْلِیَآۆُهُمُ الطَّاغُوتُ یُخْرِجُونَهُم مِّنَ النُّورِ إِلَی الظُّلُمَاتِ أُوْلَئِکَ أَصْحَابُ النَّارِ هُمْ فِیهَا خَالِدُونَ.\n\n#آیة_الکرسی | #قرآن", message_id=msg.get("message_id"))
							elif msg.get("text") == "سلام"and msg.get("author_object_guid") :
							    			   bot.sendMessage(target, "سلــــــــــــام عجقم❤️😍", message_id=msg.get("message_id"))
							elif msg["text"].startswith("حالت آرام") or msg["text"].startswith("/slow"):
								try:
									number = int(msg["text"].replace("حالت آرام ","").replace("/slow ",""))

									bot.setGroupTimer(target,number)

									bot.sendMessage(target, "⏰ حالت آرام برای "+str(number)+"ثانیه فعال شد", msg["message_id"])

								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("!pa-na-pa") or msg.get("text").startswith("په نه په"):
							     try:
								     response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								     bot.sendMessage(target, response,message_id=msg.get("message_id"))
							     except:
								      bot.sendMessage(target, "شرمنده نتونستم بفرستم!", message_id=msg["message_id"])		
							elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							    try:
								    response = get("https://api.codebazan.ir/jok/").text
								    bot.sendMessage(target, response,message_id=msg.get("message_id"))
							    except:
								    bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])
							elif msg.get("text") == "تایم":
						                   bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))
							elif msg.get("text") == "تاریخ":
					                        bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))	
							elif msg["text"] == "قفل گیف" or msg["text"] == "/gif_lock":
							    	gif_lock = True
							    	bot.sendMessage(target, "✅ قفل گیف و استیکر فعال شد .", msg["message_id"])
							elif msg["text"] == "حذف قفل گیف" or msg["text"] == "/del_gif_lock":
							 	  gif_lock = False
							 	  bot.sendMessage(target, "✅ قفل گیف و استیکر غیرفعال شد .", msg["message_id"])
							elif msg["text"] == "حذف حالت آرام" or msg["text"] == "/off_slow":
								try:
									number = 0
									bot.setGroupTimer(target,number)

									bot.sendMessage(target, "⏰ حالت آرام غیرفعال شد", msg["message_id"])
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
									
					    
					         
							# elif msg["text"] == "قفل گیف" or msg["text"] == "/gif_lock":
							# 	gif_lock = True
							# 	bot.sendMessage(target, "✅ قفل گیف و استیکر فعال شد .", msg["message_id"])

							
							# elif msg["text"] == "حذف قفل گیف" or msg["text"] == "/del_gif_lock":
							# 	gif_lock = False
							# 	bot.sendMessage(target, "✅ قفل گیف و استیکر غیرفعال شد ."           "             
							elif msg["text"] == "قفل خودکار" or msg["text"] == "/auto_lock":
								try:
									auto_lock = True
									# time = msg["text"].split(" ")[2].split(":") start=time[0] , end=time[1]
									start = "21:00"
									end = "08:00"
									# open("time.txt","w").write(start +"-"+ end)
									bot.sendMessage(target, "🔒 قفل خودکار برای گروه فعال شد . \n\n گروه ساعت [ "+ start +" ] قفل خواهد شد \n و در ساعت [ "+ end +" ] باز خواهد شد .", msg["message_id"])	
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text") == "گل":
						         try:
							         ans = ["💐","🌹","🌷","🌺","🌸","🏵️","🌻","🌼","💮"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err random")
							elif msg.get("text") == "خوبی":
						         try:							
							         ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg["text"] == "حذف قفل خودکار" or msg["text"] == "/del_auto_lock":
								auto_lock = False
								bot.sendMessage(target, "🔓 قفل خودکار برداشته شد .", msg["message_id"])


							elif msg["text"].startswith("اخراج") or msg["text"].startswith("/ban") :
								try:
									guid = bot.getInfoByUsername(msg["text"].replace("اخراج ","").replace("/ban ","")[1:])["data"]["chat"]["abs_object"]["object_guid"]
									if not guid in admins :
										bot.banGroupMember(target, guid)
										# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", msg["message_id"])
									else :
										bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
										
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										if not guid in admins :
											bot.banGroupMember(target, guid)
											# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", msg["message_id"])
										else :
											bot.sendMessage(target, "❌ کاربر ادمین میباشد", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg.get("text").startswith("نام شاخ"):
						
						         try:
							         response = get("https://api.codebazan.ir/name/").text
							         bot.sendMessage(target, response,message_id=msg.get("message_id"))
						         except:
							          bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید❌", message_id=msg["message_id"])	
							elif msg.get("text").startswith("بفرست"):
							    try:
								    if msg.get('reply_to_message_id') != None:
									    bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									    if bego2['text'] != None:
										    textss= bego2['text']
										    kanal = textss
										    bot.sendMessage(channell, kanal)
										    print('error Channel')
								    else:
									    bot.sendMessage(target, 'رو پیامی که میخواهید به کانالتان ارسال شود ریپ زنید❌',message_id=msg["message_id"])
							    except:
								    print('error Channel')
							elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام"):
							    try:
								    guidr= msg.get("author_object_guid")
								    textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
								    taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
								    ren= choice(taf)
								    f = open('/storage/emulated/0/hello.jpg')
								    p = Image.open('hello.jpg')
								    bot.sendPhoto(target, 'hello.jpg', p.size,caption=  f"علیک {textw} {ren}")
							    except:
								    print("err hello")
							elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							    try:
								    rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								    renn= choice(rew)
								    bot.sendDocument(target,"/storage/emulated/0/Mamadbot.mp4", caption= f"{renn}")
							    except:
								    print("err bot answer")
							elif msg["text"].startswith("حذف") or msg["text"].startswith("/del"):
								try:
									number = int(msg["text"].replace("حذف ","").replace("/del ",""))
									if number > 500:
										bot.sendMessage(target, "❌ ربات فقط تا 500پیام اخیر را پاک میکند .", msg["message_id"])
									else:
										answered.reverse()
										bot.deleteMessages(target, answered[0:number])

										bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", msg["message_id"])
										answered.reverse()

								except:
									try:
										bot.deleteMessages(target, [msg["reply_to_message_id"]])
										bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", msg["message_id"])
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])

							elif msg.get("text") == "چه خبر"and msg.get("author_object_guid") :
							    			    bot.sendMessage(target, "سلامتی تو چه خبر", message_id=msg.get("message_id"))
										    
							elif msg["text"].startswith("آپدیت قوانین") or msg["text"].startswith("/update_rules"):
								rules = open("rules.txt","w",encoding='utf-8').write(str(msg["text"].replace("آپدیت قوانین","").replace("/update_rules","")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", msg["message_id"])
								# rules.close()
							elif msg["text"].startswith("امتیاز") or msg["text"].startswith("/star"):
								try:
									user = msg["text"].replace("امتیاز ","").replace("/star ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									star(guid,user)
									star = open("star.txt","w",encoding='utf-8').write(str(msg["text"].replace("امتیاز","").replace("/star","")))
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]
										star(guid,user)
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
							elif msg["text"] == "قفل گروه" or msg["text"] == "/lock":
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه قفل شد", msg["message_id"])


							elif msg["text"] == "بازکردن گروه" or msg["text"] == "/unlock" :
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه اکنون باز است", msg["message_id"])
							

							elif msg["text"].startswith("افزودن") or msg["text"].startswith("/add"):
								try:
									guid = bot.getInfoByUsername(msg["text"].replace("افزودن ","").replace("/add ","")[1:])["data"]["chat"]["object_guid"]
									if guid in blacklist:
										for i in range(no_alerts.count(guid)):
											no_alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:
										bot.invite(target, [guid])
									
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
					        
							elif msg["text"] == "قوانین":
								rules = open("rules.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), msg["message_id"])
								# rules.close()
						
							elif msg["text"] == "دستورات":
								commands = open("commands.txt","r",encoding='utf-8').read()
								bot.sendMessage(target,str(commands),msg["message_id"])
					
						# User Commands
						else:

							if hasAds(msg["text"]) and not msg["author_object_guid"] in exemption:
								guid = msg["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								bot.deleteMessages(target, [msg["message_id"]])
								alert(guid,user,"گذاشتن لینک در گروه ممنوع میباشد .\n\n")
							if  msg.get("text").startswith('!user @'):
								try:
									user_info = bot.getInfoByUsername( msg.get("text")[7:])
									if user_info['data']['exist'] == True:
										if user_info['data']['type'] == 'User':
											bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
											print('sended response')
										else:
											bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
											print('sended response')
									else:
										bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
										print('sended response')
								except:
									print('server bug6')
									bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							elif msg.get("text") == "تبلیغات روشن":
							    try:
								    bot.sendMessage(target, "🤖در پیام بعدی لینک گروه مورد نظر را ثبت نمائید🤖\nمثال:\n\nجوین گروه\nhttps://rubika.ir/joinc/BEDJEHGJ0LXSIPACCXGCQCBIJBZESKWA")
							    except:
								    print("error ersal start1")
							elif msg.get("text").startswith("جوین گروه"):
							    try:
								    yourlink = open("target.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								    bot.sendMessage(target,  "✅ با موفقیت لینک گروه مورد نظر ثبت شد")
								    bot.sendMessage(target,  "\n🤖بنر خود را برای تبلیغات در پیام بعدی ثبت نمائید🤖\n\nمثال رو پیامی که می خواهید پخش شود ریپ بزنید و بگویید [ ثبت تبلیغ ]\n")
							    except:
								    print("error sabt_link-tabligh")
							elif msg.get("text").startswith("ثبت تبلیغ"):
							    try:
								    if msg.get('reply_to_message_id') != None:
									    banner = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									    if banner['text'] != None:
										    matnbanner= banner['text']
										    matntabligh = open("matnTABLIGH.txt","w",encoding='utf-8').write(str(matnbanner))
							    except:
								    bot.sendMessage(target, "✅  \n\nمتن مورد نظر برای تبلیغات ثبت شد\nبرای شروع تبلیغات [ تبلیغ کن ] را وارد کنید", message_id=msg.get("message_id"))
							    
							elif msg.get("text").startswith("تبلیغ کن"):
							    while True:
								    sleep(5)
								    tabyligh = open("matnTABLIGH.txt","r",encoding='utf-8').read()
								    tabgligh = open("target.txt","r",encoding='utf-8').read()
								    tabeligh = bot.joinGroup(tabgligh)
								    tabrligh = tabeligh['data']['group']['group_guid']
								    bot.sendMessage(tabrligh,tabyligh)
								    bot.leaveGroup(tabrligh)
							elif msg.get("text") == "کص" or msg.get("text") == "کیر" or msg.get("text") == "کوص" or msg.get("text") == "کیری" or msg.get("text") == "گاییدم" or msg.get("text") == "خارکسده" or msg.get("text") == "خایه" or msg.get("text") == "جق" or msg.get("text") == "کصکش":
							    try:
								    bot.deleteMessages(target, message_id=msg.get("message_id"))
								    bot.sendMessage(target, "بی تر ادب", message_id=msg.get("message_id"))
							    except:
								    print("err delete fesh")
							elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						         try:
							         response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							         bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							         bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
						         except:
							          bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
							elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							    try:
								    rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								    renn= choice(rew)
								    bot.sendDocument(target,"/storage/emulated/0/ARIANBOT.mp4", caption= f"{renn}")
							    except:
								    print("err bot answer")
							elif msg.get("text").startswith("send"):

							    try:

								    if msg.get('reply_to_message_id') != None:

									    befrest = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]

									    if befrest['text'] != None:

										    texts= befrest['text']

										    usersendmatn = msg.get("text").split(" ")[1][1:]

									    bot.sendMessage(bot.getInfoByUsername(usersendmatn)["data"]["chat"]["abs_object"]["object_guid"],texts)

							    except:

								    print("err send_massage_be_id")
							elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام"):
							    try:
								    guidr= msg.get("author_object_guid")
								    textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
								    taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
								    ren= choice(taf)
								    f = open('/storage/emulated/0/Download/arianbot/arianbot/hello.jpg')
								    p = Image.open('hello.jpg')
								    bot.sendPhoto(target, 'hello.jpg', p.size,caption=  f"علیک {textw} {ren}")
							    except:
								    print("err hello")
							elif msg.get("text").startswith("بازی") or msg.get("text").startswith("جرعت حقیقت") or msg.get("text").startswith("ج ح"):
								rules = open("jorat.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							    try:
								    response = get("https://api.codebazan.ir/jok/").text
								    bot.sendMessage(target, response,message_id=msg.get("message_id"))
							    except:
								    bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])
							elif msg.get("text") == "سلام":
						         try:							
							         ans = ["سلام عزیزم😋💛", "سلام گوگولی من😄❤️","سلام عجقم🤤🌹","سپاس صلم عشقم🌺","سلام خوبی چیکار میکنی 😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg.get("text") == "خوبی":
						         try:							
							         ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg.get("text") == "ربات":
								try:
									ans = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n جان کاری داشتید","🎓\n🙂\n🧥\n👖 \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩"]
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
								except:
									bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text") == "محمدبات":
					      			user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
					      			text = f"جـــونــم {user} عــزیـزم🙂🌹"
					      			bot.sendMessage(target, text, message_id=msg.get("message_id"))
							elif msg.get("text") == "گل":
						         try:
							         ans = ["💐","🌹","🌷","🌺","🌸","🏵️","🌻","🌼","💮"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err random")
							elif msg.get("text").startswith("جستجو") or msg.get("text").startswith("!search") or msg.get("text").startswith("search"):
						          try:
							          search = msg.get('text').split()[1]                             
							          jd = loads(get('https://zarebin.ir/api/?q=' + search + '&page=1&limit=10').text)
							          results = jd['results']['webs']
							          text = ''
							          for result in results:
								          text += result['title'] + ':\n\n  ' + str(result['description']).replace('</em>', '').replace('<em>', '').replace('(Meta Search Engine)', '').replace('&quot;', '').replace(' — ', '').replace(' AP', '') + '\n\n'  
							          bot.sendMessage(target, 'نتایج کامل به پیوی شما ارسال شد', message_id=msg["message_id"])
							          bot.sendMessage(msg['author_object_guid'], 'نتایج یافت شده برای (' + search + ') : \n\n'+text)
						          except:
							          print('zarebin search err')
							elif msg.get("text").startswith("پینگ"):
						
						         try:
							         responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							         bot.sendMessage(target, responser,message_id=msg["message_id"])
						         except:
							         bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							elif msg.get("text") == "😐"and msg.get("author_object_guid") :
							    			   bot.sendMessage(target, "پوکر میدی پوکر بدم😏😐", message_id=msg.get("message_id"))
							elif msg.get("text") == "ایموجی":
								try:
									ans = ["😀","😃","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","🤬","☹️","🙁","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","🤤","🥱","😴","😪","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","😇","🤠","🤑","😎","🤓","🤥"]
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
								except:
									 bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
							elif msg.get("text") == "قلب":
								try:
									ans = ["❤️","🧡","💛","💚","💙","💜","🤎","🖤","🤍","♥️","💘","💝","💖","💗","💓","💞","💕","💟","❣️","💔"]
									bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
								except:
									 bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))	    
							
							elif msg.get("text") == "سلام":
						         try:							
							         ans = ["سلام عزیزم😋💛", "سلام گوگولی من😄❤️","سلام عجقم🤤🌹","سپاس صلم عشقم🌺","سلام خوبی چیکار میکنی 😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg.get("text") == "خوبی":
						         try:							
							         ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
							         bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
						         except:
							         print("err ranodm")
							elif msg["text"] == "دستورات":
								commands = open("commands.txt","r",encoding='utf-8').read()
								bot.sendMessage(target,str(commands),msg["message_id"])
							elif msg["text"] == "قوانین":
								rules = open("rules.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), msg["message_id"])
								# rules.close()
							elif msg["text"].startswith("افزودن") or msg["text"].startswith("/add"):
								try:
									guid = bot.getInfoByUsername(msg["text"].replace("افزودن ","").replace("/add ","")[1:])["data"]["chat"]["object_guid"]
									if guid in blacklist:
										bot.sendMessage(target, "❌ کاربر در لیست سیاه میباشد و فقط ادمین میتواند فرد را به گروه اضافه کند .", msg["message_id"])
									else:
										bot.invite(target, [guid])
										# bot.sendMessage(target, "✅ کاربر اکنون عضو گروه است", msg["message_id"])
									
								except:
									bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
                                
							elif msg["text"] == "لینک":
								group = bot.getGroupLink(target)["data"]["join_link"]
								bot.sendMessage(target, "🔗 لینک گروه :\n"+str(group), msg["message_id"])

							for i in data.keys():
								if i == msg["text"]:
									bot.sendMessage(target, str(data[i]), msg["message_id"])
					elif msg["type"]=="Event" and not msg["message_id"] in answered:
						answered.append(msg["message_id"])

						name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
						data = msg['event_data']
						if data["type"]=="RemoveGroupMembers":
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"🚨 کاربر {user} با موفقیت از گروه حذف شد .", msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						
						elif data["type"]=="AddedGroupMembers":
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"سلام {user} عزیز 🌹 \n • به گروه {name} خوش اومدی 😍 \n 📿 لطفا قوانین رو رعایت کن .\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی .", msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						
						elif data["type"]=="LeaveGroup":
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"خدانگهدار {user} 👋 ", msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						
						elif data["type"]=="JoinedGroupByLink":
							guid = data['performer_object']['object_guid']
							user = bot.getUserInfo(guid)["data"]["user"]["first_name"]
							bot.sendMessage(target, f"سلام {user} عزیز 🌹 \n• به گروه {name} خوش اومدی 😍 \n 📿 لطفا قوانین رو رعایت کن .\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی .", msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
							if guid in blacklist:
								for i in range(no_alerts.count(guid)):
									no_alerts.remove(guid)
								blacklist.remove(guid)
					
					# elif msg["type"]=="Gif" or msg["type"]=="Sticker" and not msg["message_id"] in answered:
					# 	if gif_lock and not msg["author_object_guid"] in admins:
					# 		guid = msg["author_object_guid"]
					# 		user = bot.getUserInfo(guid)["data"]["user"]["username"]
					# 		bot.deleteMessages(target, [msg["message_id"]])
					# 		alert(guid,user,"ارسال گیف و استیکر در گروه ممنوع میباشد .")

					else:
						if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg["message_id"]])[0]["forwarded_from"]["type_from"] == "Channel" and not msg["author_object_guid"] in exemption:
							bot.deleteMessages(target, [msg["message_id"]])
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							bot.deleteMessages(target, [msg["message_id"]])
							alert(guid,user,"فوروارد پیام در گروه ممنوع میباشد .\n\n")
						
						answered.append(msg["message_id"])
						continue
				
				else:
					if msg["text"] == "ربات روشن" or msg["text"] == "/wakeup":
						sleeped = False
						bot.sendMessage(target, "✅ ربات اکنون روشن است .", msg["message_id"])
					
			except:
				continue

			answered.append(msg["message_id"])
			print("[" + msg["message_id"]+ "] >>> " + msg["text"] + "\n")
						
	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue