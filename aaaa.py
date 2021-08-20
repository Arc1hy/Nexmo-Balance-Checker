import requests
from requests.models import Response
import json

txtName = "api_Info.txt"
try:
    a = open(txtName,"r")
    a.close()
    print(txtName,"Found")
except:
    print(txtName,"Not found, Creating file")
    a = open(txtName,"w")
    a.write("api_key=\napi_secret=")
    a.close()

print("\n")

api_key = ""
api_secret = ""

#Get lines
lines = open(txtName,"r")
for line in lines:
    if line[0:8] == "api_key=":
        api_key = line[8:len(line)-1]
    elif line[0:11] == "api_secret=":
        api_secret = line[11:len(line)]
lines.close()

messageUrl = "https://rest.nexmo.com/account/get-balance?api_key="+api_key+"&api_secret="+api_secret
message = requests.get(messageUrl)

strcontent = str(message.content)

#b'{"value":-0.08840000,"autoReload":false}'

#get rid of useless stuff
temp1 = strcontent.split("{")
temp2 = temp1[1].split("}")
contents = temp2[0]
#now returns "value":-0.08840000,"autoReload":false

content = []
balence = 0
autoReload = None

#Get Balence
temp3 = contents.split("\"value\":")
try:
    temp3.append(temp3[1].split(","))
    content.append(temp3[2])
    balence = content[0][0]
except:
    print("Something went wrong while getting the balence")

#autoReload
try:
    temp4 = temp3[2]
    temp5 = temp4[1].split("\"autoReload\":")
    if temp5[1] == "false":
        autoReload = False
    else:
        autoReload = True
except:
    print("Something went wrong, Most likely due to no balence")
    print("\n")

#get api key
urlEnd = messageUrl[43:len(messageUrl)]
temp6 = urlEnd[8:len(urlEnd)]
temp7 = temp6.split("&")
api_key = temp7[0]

#get api secret
temp8 = temp7[1].split("api_secret=")
api_secret = temp8[1]

print("Your credit is =",balence)
print("Rechargement Automatique =",str(autoReload))
print("\nApi info:\n")
print("Api_key =",api_key)
print("Api_Secret =",api_secret)