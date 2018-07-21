# General imports
import io
import os
from os import listdir
from os.path import isfile, join

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate

# Instantiates a client
client = vision.ImageAnnotatorClient()
translate_client = translate.Client()

# Choosing and creating folders
mypath = "/Users/lmpierin/Documents/TioAcyr/Livro_Alemao/" #Path to images folder

originaltext = mypath + "Texto_Original/" #Path to original text forlder
if not os.path.exists(originaltext):
    os.makedirs(originaltext)
transtext = mypath + "Texto_Traduzido/" #Path to translated text folder
if not os.path.exists(transtext):
    os.makedirs(transtext)

# Reading images from folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
list.sort(onlyfiles) #Sort them 
cont = 0

# Processing all images read
for pag in onlyfiles:
    if(pag == '.DS_Store'): continue #Skip MacOS file
    spacer = " "
    while((len(pag) + len(spacer)) < 20):
        spacer += "-"
    print("Processando: " + pag + spacer + " %.2f%c" % ((cont/len(onlyfiles))*100,"%"), end='\r')

    # The name of the image file to annotate
    file_name = mypath + pag

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    # Writting original text to file/screen
    #print(u'Text: {}'.format(labels[0].description))
    orig = open(originaltext + pag.split('.')[0] + ".txt",'w')
    orig.write(labels[0].description)
    orig.close()

    # The target language
    target = 'pt-br'

    # The text to translate
    text = labels[0].description
    translation = translate_client.translate(text, target_language=target)

    # Writing translated text to file/screen
    #print(u'Translation: {}'.format(translation['translatedText']))
    trad = open(transtext  + pag.split('.')[0] + ".txt", 'w')
    trad.write(translation['translatedText'])
    trad.close()

    cont += 1
print("Completado! ------------------- %.2f%c" % ((cont/len(onlyfiles))*100,"%"))