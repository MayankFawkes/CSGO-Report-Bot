import requests
import tkinter
from tkinter import messagebox
import re,os
global passcheck
root = tkinter.Tk()
root.withdraw()
passcheck=""
logo=r'''

		 ██▀███  ▓█████  ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ▄▄▄▄    ▒█████  ▄▄▄█████▓
		▓██ ▒ ██▒▓█   ▀ ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
		▓██ ░▄█ ▒▒███   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
		▒██▀▀█▄  ▒▓█  ▄ ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
		░██▓ ▒██▒░▒████▒▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
		░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
		  ░▒ ░ ▒░ ░ ░  ░░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ▒░▒   ░   ░ ▒ ▒░     ░    
		  ░░   ░    ░   ░░       ░ ░ ░ ▒    ░░   ░   ░       ░    ░ ░ ░ ░ ▒    ░      
		   ░        ░  ░             ░ ░     ░               ░          ░ ░           
		                                                          ░                   
		                            BurnOut / MayankFawkes

'''
def report(profileurl):
	web="https://reportbot.cloud/steamidconverter.php"
	headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	}
	data={
		"SteamID": profileurl,
		"SteamIDFinder": "Get SteamID64"
	}
	r=requests.post(web,headers=headers,data=data)
	data=r.text
	data=re.findall("<br />Steam ID 64: (.*?)<br />",data)	

	web1="https://reportbot.cloud/"
	data1={}
	data1["steamid"]=data[0]
	if data1["steamid"] is not "":
		r=requests.post(web1,headers=headers,data=data1,allow_redirects=True)
		if r.status_code==200:
			print("[+] 20 Report Submited Against {}".format(data[0]))
	else:
		print("[+] Wrong Profile URl")
def check(usr,pas):
	try:
		global passcheck
		if not passcheck:
			passcheck=requests.get("https://raw.githubusercontent.com/MayankFawkes/Vyapam/master/file.json").json()
		if passcheck[usr]== pas:
			return True
		else:
			return False
	except:
		return False

if __name__ == '__main__':
	while True:
		print(logo)
		usr=input("Enter Username -->").lower()
		pas=input("Enter Password -->").lower()
		if check(usr,pas):
			os.system("cls")
			print(logo)
			print("Type Profile Url")
			while True:
				report(input("-->"))
		else:
			messagebox.showerror("Error", "Username Or Password Wrong")
			os.system("cls")