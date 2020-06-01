from twilio.rest import Client
import http.client

#### GETTING WEATHER ####

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "36c5d23ecemsh8242639357a71d1p1fa7a4jsna57adc61a7cd"
    }

conn.request("GET", "/weather?lat=41.783333&lon=44.716667&callback=test&id=2172797&units=metric&mode=xml%252C%20html", headers=headers)

res = conn.getresponse()
data = (res.read()).decode("utf-8")

def tme ():
	WMain = ""
	temp = ""
	flike = ""
	windsp = ""
	for j in range (len (data) - 10):
		str = ""
		for i in range (j, j + 7):
			str += data[i]
		if str == "main\":\"":
			i = j + 7
			while data[i] != "\"":
				WMain += data[i]
				i += 1
		if str == "\"temp\":":
			i = j + 7
			while data[i] != ',':
				temp += data[i]
				i += 1
		if str == "_like\":":
			i = j + 7
			while data[i] != ',':
				flike += data[i]
				i += 1
		if str == "speed\":":
			i = j + 7
			while data[i] != ',':
				windsp += data[i]
				i += 1
	return WMain, temp, flike, windsp
		
WMain, temp, flike, windsp = tme ()

sdata = "weather: " + WMain + "\ntemp: " + temp + "\nfeels like: " + flike + "\nwind speed: " + windsp

#### END GETTING WEATHER ####

##########################

#### MASSEGEEEEEEEEEEE #####
frm = '+12082038413'
ton = '+995579237639'
acc_sid = 'ACe0a64dcef0141841b771c0dbbf47af90'
auth_tok = '99cced919133fe853f586f4e3cd42bc0'
me = Client (acc_sid, auth_tok)

msg = me.messages.create (
							body=sdata,
							from_=frm,
							to=ton
)

print (msg.sid)
