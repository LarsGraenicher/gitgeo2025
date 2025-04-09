import os #als betriebssystem übersetzen

name = os.name
print(name)

if name == "nt":
    print("Sie benutzen Windows")
else:
    print("Gratulation")


username= os.getlogin()
print(username)

print(os.environ["USERPROFILE"])  #systemvariablen mit Userprofil die für den benutzer

file = open(os.environ["USERPROFILE"] + "/text.txt","w",encoding = "utf-8")
file.write("hallo")
file.close()