import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

x = re.findall("[a-m]", txt)
print(x)

x = re.findall("r..n", txt)
print(x)

x = re.search("^The", txt)
print("Yes" if x else "No")
x = re.findall("ain$", txt)
print("Yes" if x else "No")


