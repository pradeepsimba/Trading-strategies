import tkinter as tk

from tkinter import ttk

import threading

from fyers_api import fyersModel

from fyers_api import accessToken

#create Window

root=tk.Tk()

style=ttk.Style()

style.theme_use('winnative')

def allThread():

	t1=threading.Thread(target=liveData)

	t1.start()

def clearWidgets():

	for widgets in scrollableFrame.winfo_children():

		widgets.destroy()

def connect_fyers():

	global fyers

	session=accessToken.SessionModel(client_id="CLIENT ID",

	secret_key="SECRET KEY",redirect_uri="https://trade.fyers.in/", 

	response_type="code", grant_type="authorization_code",

	state="abcdefg",scope="",nonce="")

	response = session.generate_authcode()

	#https://api.fyers.in/api/v2/generate-authcode?client_id=CLIENT_ID&redirect_uri=https://trade.fyers.in/&response_type=code&state=sample_state&nonce=sample_nonce  

	auth_code="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NDYyNzg4NjgsImV4cCI6MTY0NjMwODg2OCwibmJmIjoxNjQ2Mjc4MjY4LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYTTE1ODgyIiwibm9uY2UiOiJzYW1wbGVfbm9uY2UiLCJhcHBfaWQiOiI1UU41RjNXR1Y2IiwidXVpZCI6Ijc4MmVlNTRkNjU5OTRkMWZiNTY5ZWQyNDIzZWI5ZGZiIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.xQQGXU14_GWgsXDYAkrauBXC6AjIf9Ja1mXbx7W_6Zw"

	session.set_token(auth_code)

	response = session.generate_token()

	access_token = response["access_token"]

	fyers = fyersModel.FyersModel(client_id="CLIENT_ID", token=access_token,log_path="E:/tools")

	profile=fyers.get_profile()

	print(profile["data"]["name"])

connect_fyers()

def liveData():

	clearWidgets()

	f=open("E:/tools/"+indices.get()+".txt")

	stockList=f.read()

	stocks=stockList.split(",")



	i=0

	for value in stocks:

		data = {"symbols":"NSE:"+value+"-EQ"}

		out=fyers.quotes(data)

		if(cond.get()=="ALL"):

			ttk.Label(scrollableFrame,text=value,width=15,font=("Arial bold",10)).grid(row=i,column=0)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["open_price"],width=15,font=("Arial bold",10)).grid(row=i,column=1)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["high_price"],width=15,font=("Arial bold",10)).grid(row=i,column=2)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["low_price"],width=15,font=("Arial bold",10)).grid(row=i,column=3)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["volume"],width=15,font=("Arial bold",10)).grid(row=i,column=4)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["lp"],width=15,font=("Arial bold",10)).grid(row=i,column=5)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["ch"],width=15,font=("Arial bold",10)).grid(row=i,column=6)

			ttk.Label(scrollableFrame,text=out["d"][0]["v"]["chp"],width=15,font=("Arial bold",10)).grid(row=i,column=7)

			i+=1

		elif(cond.get()=="LOWER THAN"):	

			chp=out["d"][0]["v"]["chp"]

			if(chp<=float(changeValue.get())):

				ttk.Label(scrollableFrame,text=value,width=15,font=("Arial bold",10)).grid(row=i,column=0)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["open_price"],width=15,font=("Arial bold",10)).grid(row=i,column=1)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["high_price"],width=15,font=("Arial bold",10)).grid(row=i,column=2)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["low_price"],width=15,font=("Arial bold",10)).grid(row=i,column=3)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["volume"],width=15,font=("Arial bold",10)).grid(row=i,column=4)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["lp"],width=15,font=("Arial bold",10)).grid(row=i,column=5)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["ch"],width=15,font=("Arial bold",10)).grid(row=i,column=6)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["chp"],width=15,font=("Arial bold",10)).grid(row=i,column=7)

				i+=1

		elif(cond.get()=="HIGHER THAN"):	

			chp=out["d"][0]["v"]["chp"]

			if(chp>=float(changeValue.get())):

				ttk.Label(scrollableFrame,text=value,width=15,font=("Arial bold",10)).grid(row=i,column=0)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["open_price"],width=15,font=("Arial bold",10)).grid(row=i,column=1)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["high_price"],width=15,font=("Arial bold",10)).grid(row=i,column=2)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["low_price"],width=15,font=("Arial bold",10)).grid(row=i,column=3)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["volume"],width=15,font=("Arial bold",10)).grid(row=i,column=4)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["lp"],width=15,font=("Arial bold",10)).grid(row=i,column=5)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["ch"],width=15,font=("Arial bold",10)).grid(row=i,column=6)

				ttk.Label(scrollableFrame,text=out["d"][0]["v"]["chp"],width=15,font=("Arial bold",10)).grid(row=i,column=7)

				i+=1				

#creating frame

topFrame=ttk.Frame(root)

ttk.Label(topFrame,text="SELECT INDEX",width=15, font=("Arial bold",10)).grid(row=0,column=0)

indices=ttk.Combobox(topFrame,values=["NIFTY50","SMALLCAP","MIDCAP","NIFTYBANK","NIFTYIT"],width=15, font=("Arial bold",10))

indices.current(0)

indices.grid(row=0,column=1)

ttk.Label(topFrame,text="SELECT INDEX",width=15, font=("Arial bold",10)).grid(row=0,column=2)

cond=ttk.Combobox(topFrame,values=["ALL","HIGHER THAN","LOWER THAN"],width=15, font=("Arial bold",10))

cond.current(0)

cond.grid(row=0,column=3)

changeValue=ttk.Entry(topFrame,width=15)

changeValue.grid(row=0,column=5)

ttk.Button(topFrame,text="SEARCH",command=allThread,width=15).grid(row=0,column=6)

ttk.Label(topFrame,text="NAME",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=0)

ttk.Label(topFrame,text="OPEN",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=1)

ttk.Label(topFrame,text="HIGH",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=2)

ttk.Label(topFrame,text="LOW",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=3)

ttk.Label(topFrame,text="VOLUME",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=4)

ttk.Label(topFrame,text="LTP",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=5)

ttk.Label(topFrame,text="CHANGE",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=6)

ttk.Label(topFrame,text="CHANGE%",foreground="blue",width=15,font=("Arial bold",10)).grid(row=1,column=7)

topFrame.pack()



#creating frame for displaying results



botFrame=ttk.Frame(root)

canvas=tk.Canvas(botFrame)

scrollbar=ttk.Scrollbar(botFrame,orient="vertical",command=canvas.yview)

scrollableFrame=ttk.Frame(canvas)

scrollableFrame.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0,0),window=scrollableFrame,anchor="nw")

canvas.configure(width=900,yscrollcommand=scrollbar.set)

botFrame.pack()

canvas.pack(side="left",fill="both",expand=True)

scrollbar.pack(side="right",fill="y")



root.mainloop()
