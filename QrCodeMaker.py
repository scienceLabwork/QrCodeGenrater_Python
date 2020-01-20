import pyqrcode

userUrl = input("Please Input url to generate QR-CODE: ")

url = pyqrcode.create(userUrl)
url.svg('uca-url.svg',scale="8")
print(url.terminal(quiet_zone=1))