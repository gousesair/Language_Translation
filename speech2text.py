#-*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
from flask import *

lang1=""
lang2=""
translator = Translator()

app = Flask(__name__)
langDict = {"mar":"mr","hin":"hi","tam":"ta","tel":"te","guj":"gu","bod":"bn","mal":"ml","kan":"kn","eng":"en","ger":"de","fre":"fr","jap":"ja","kor":"ko","gre":"el","ita":"it","lat":"la","rus":"ru","spa":"es","ara":"ar","por":"pt-PT","urd":"ur"}
langTrans=  {"mar":"marathihts","hin":"hindi","tam":"tamil","tel":"telugu","guj":"htsgujarati_male","bod":"htsbodo","mal":"malayalam","kan":"htskannada_female","eng":"english"}
api = 'AIzaSyCCjlnIZ7zxc3LTltUc60Zjx7Wmg3Mpzpw'


@app.route("/")
def index():
	return render_template("Home.html")

@app.route("/Langselect", methods=['GET', 'POST'])
def lang():
	if request.method == 'POST':
		lang = request.form.get("Language1")
		print(lang+"Lang")
		if lang == "Int":
			return render_template("International.html")
		else:
			return render_template("Indian.html")

@app.route("/Indtrans", methods=['GET', 'POST'])
def Indtrans():
	if request.method == 'POST':
		global lang2
		global lang1
		lang1 = request.form.get("Language1")
		lang2 = request.form.get("Language2")
		print("Lang1 = "+lang1+" Lang2 = "+lang2)
		# langSet1 = langDict[lang1]
		# print(langSet1)
		return render_template("TeluguTyping.html",input=lang1)

		# if lang1=="mar":
		# 	return render_template("MaratiTyping.html")
		# elif lang1=="hin":
		# 	return render_template("HindiTyping.html")
		# elif lang1=="tam":
		# 	return render_template("TamilTyping.html")
		# elif lang1=="tel":
		# 	return render_template("TeluguTyping.html")
		# elif lang1=="guj":
		# 	return render_template("GujarathiTyping.html")
		# elif lang1=="bod":
		# 	return render_template("BodoTyping.html")
		# elif lang1=="mal":
		# 	return render_template("MalayalamTyping.html")
		# elif lang1=="kan":
		# 	return render_template("KannadaTyping.html")
		# elif lang1=="eng":
		# 	return render_template("EnglishTyping.html")

@app.route("/textTrans", methods=['GET', 'POST'])
def textTrans():
	print("Text translate entered")
	if request.method == 'POST':
		SpeechText = request.form.get("speechText")
	dest = langDict[lang2]
	print(dest)
	print(langDict[lang1])
	# SpeechText ="The club isn't the best place to find a lover So the bar is where I go Me and my friends at the table doing shots Drinking fast and then we talk slow Come over and start up a conversation with just me And trust me I'll give it a chance now Take my hand, stop, put Van the Man on the jukebox And then we start to dance, and now I'm singing like Girl, you know I want your love Your love was handmade Come on now, follow my lead I may be crazy, don't mind me Say, boy, let's not talk too much Grab on my waist and put that body on me Come on now, follow my lead Come, come on now, follow my lead I'm in love with the shape of you We push and pull like a magnet do Although my heart is falling too I'm in love with your body And last night you were in my room And now my bedsheets smell like you Every day discovering something brand new I'm in love with your body Oh—I—oh—I—oh—I—oh—I I'm in love with your body Oh—I—oh—I—oh—I—oh—I I'm in love with your body Oh—I—oh—I—oh—I—oh—I 	I'm in love with your body Every day discovering something brand new I'm in love with the shape of you One week in we let the story begin We're going out on our first date You and me are thrifty, so go all you can eat Fill up your bag and I fill up a plate We talk for hours and hours about the sweet and the sour And how your family is doing okay Leave and get in a taxi, then kiss in the backseat Tell the driver make the radio play, and I'm singing like Girl, you know I want your love Your love was handmade for somebody like me Come on now, follow my lead I may be crazy, don't mind me Say, boy, let's not talk too much  Grab on my waist and put that body on me Come on now, follow my lead Come, come on now, follow my lead  I'm in love with the shape of you We push and pull like a magnet do Although my heart is falling too I'm in love with your body And last night you were in my room And now my bedsheets smell like you Every day discovering something brand new I'm in love with your body Oh—I—oh—I—oh—I—oh—I I'm in love with your body Oh—I—oh—I—oh—I—oh—I I'm in love with your body Oh—I—oh—I—oh—I—oh—I I'm in love with your body Every day discovering something brand new I'm in love with the shape of you Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on Come on, be my baby, come on I'm in love with the shape of you We p ush and pull like a magnet do Although my heart is falling too I'm in love with your body Last night you were in my room And now my bedsheets smell like you Every day discovering something brand new I'm in love with your body Come on, be my baby, come on Come on, be my baby, come on I'm in love with your body Come on, be my baby, come on Come on, be my baby, come on I'm in love with your body Come on, be my baby, come on Come on, be my baby, come on I'm in love with your body Every day discovering something brand new I'm in love with the shape of you"
	mytext3 = translator.translate(SpeechText,dest=langDict[lang2],src=langDict[lang1])
	source1=langTrans[lang2]
	return render_template("Native.html",results1=mytext3.text,source=source1)

@app.route("/Inttrans", methods=['GET', 'POST'])
def Inttrans():
	if request.method == 'POST':
		global lang2
		global lang1
		lang1 = request.form.get("Language1")
		lang2 = request.form.get("Language2")
		print("Lang1 = "+lang1+" Lang2 = "+lang2)
		# langSet1 = langDict[lang1]
		# print(langSet1)
		return render_template("EnglishTyping.html",input=lang1)

@app.route("/textintTrans", methods=['GET', 'POST'])
def textintTrans():
	print("Text translate entered")
	if request.method == 'POST':
		SpeechText = request.form.get("speechText")
	dest = langDict[lang2]
	print(dest)
	print(langDict[lang1])
	mytext3 = translator.translate(SpeechText,dest=langDict[lang2],src=langDict[lang1])
	# source1=langTrans[lang2]
	# return render_template("Native.html",results1=mytext3.text,source=source1)

	# mytext2=translator.translate(mytext1,dest='en',src=language1)

	# mytext3 = translator.translate(mytext2.text,dest=language2,src='en') 

	myobj = gTTS(text=mytext3.text, lang=dest, slow=False)
	print("After myobj")

	myobj.save("static/audio.mp3")
	print("After save")
	 
	# os.system("audio.mp3")
	return render_template("audio.html")
if __name__ == '__main__':
	app.run(debug=True)

