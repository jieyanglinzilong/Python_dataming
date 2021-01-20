import requests
from io import BytesIO, StringIO
from PIL import Image
imageurl = "https://file.ertuba.com/2020/1225/8854489f04823b276617ee7108dbd865.jpg"
response = requests.get(imageurl)
f = BytesIO(response.content)
img = Image.open(f)
print(img.size)
#保存到本地路径
img.save("lg.jpg")
