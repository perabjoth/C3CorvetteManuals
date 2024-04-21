import base64
from bs4 import BeautifulSoup
from os import listdir, getcwd, makedirs
from os.path import isfile, join, exists

onlyfiles = [f for f in listdir() if isfile(f)]
for x in onlyfiles:
    if x.endswith(".html") and not x.startswith("index"):    
        with open(x, 'rb') as fp:
            soup = BeautifulSoup(fp, features="html.parser")
            images = soup.select("div.pf")
            current_directory = getcwd()
            newDirectory ='img/'+x.replace('.html','')+'/'
            final_directory = join(current_directory, newDirectory)
            if not exists(final_directory):
                makedirs(final_directory)
            for image in images:
                imageName = newDirectory+image['data-page-no']+'.png'
                print(imageName)
                for child in image.descendants:
                    if child.name == "img":
                        imgWrite = open(imageName, "wb")
                        imageString = str(child['src']).replace("data:image/png;base64,", "")
                        imageData = base64.b64decode(imageString)
                        imgWrite.write(imageData)
                        imgWrite.close()                    
                        child['src'] = imageName
            f = open("new"+x, "w")
            f.write(str(soup))
            f.close()