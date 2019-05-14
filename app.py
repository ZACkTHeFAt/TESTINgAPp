from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def basic_response():
    print("Someone clicked this link!")
    return "This is a website!"

# @app.route("/mAlWaRe")
# def malware():
#     print("Someone clicked this link!")
#     return "YoU hAvE gOtTeN mAlWaRe ByTeS fRoM ClIcKiNg ThE LiNk! :)"

@app.route("/hello")
def hello():
    print("Someone clicked this link!")
    return "HELLO :)"

@app.route("/goodbye")
def goodbye():
    print("Someone clicked this link!")
    return "GOODBYE ;("

@app.route("/WAS-UP")
def wasssup():
    print("Someone clicked this link!")
    return "WASSSSSS UPPPPPP MYYYYYY DOODEEEEEEEEEE??????!??!?!??!?!!!!!!!!!!!!!!??!?!??! :)))))))))))))))))))))))))"

@app.route("/noOn43/<name>")
def noOn43(name):
	print("{} clicked this link!".format(name))
	f = open('NO-ON43.txt','a+')
	f.write(name + '\n')
	f.close()
	return "{} HAS JUST VOTED NO ON PROP 43! WHY TF HAVE U DONE THIS? NOW THE GOVERNMENT WILL GO TO EVERY1S HOUSE AND DOWNLOAD MALWARE BYTES ON THERE COMPUTERS U SMELLY SMELL >:(".format(name)

@app.route("/yeson43/<name>")
def yeson43(name):
	print("{} clicked the link!".format(name))
	f = open('YESON43.txt','a+')
	f.write(name + '\n')
	f.close()
	return "{} IS THE SAVOIOR TO HUMANITY! BECAUSE YOU VOTED NO ON PROP 43, THE RUSSIAN GOVERNMENT WILL NOT GO TO EVER1S HOUSE AND DOWNLOAD MALWARE BYTES ON THERE COMPUTERS! WELL DONE, IM VERY HONORED TO BE IN UR PRESENCE! :)".format(name)

@app.route("/mAlWaRe/<name>")
def say_name(name):
	print("{} clicked this link".format(name))
	f = open('NAMEsVISITEd.txt','a+')
	f.write(name + '\n')
	f.close()
	return "{} clicked this link".format(name)

app.run(debug=False,host='0.0.0.0',port=os.environ.get("PORT",33507))