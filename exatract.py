import re

my_string =  '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'

ipadd = re.findall("123.123.123.123",my_string)
print(ipadd)

date = re.findall("[26/Apr/2000:00:23:48 -0400]",my_string)
print(date)

pics = re.findall("GET /pics/wpaper.gif HTTP/1.0",my_string)
print(pics)

url = re.findall("[http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)]", my_string)
print(url)
