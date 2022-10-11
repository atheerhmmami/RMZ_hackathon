# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:31:09 2022

@author: aclou
"""

#importing needed libraries
import requests
from PIL import Image
from pytesseract import pytesseract
from googletrans import Translator
import speech_recognition as sr
import pyttsx3
 
 
"""
This class showcases the core functionalities of RMZ 
note: this code isn't complete but meant to describe the functionalities
"""
#step1: get user input/request:  
#functions to convert the user input to a text format
def covertIMGtoText(path_to_image):
    #we will use tesseract to recognize characters
    path_to_tesseract = r'C:\Users\aclou\AppData\Local\Tesseract-OCR\tesseract.exe'
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    #Open image with PIL
    img = Image.open(path_to_image)
    #Extract text from image
    textInput = pytesseract.image_to_string(img)
  
    return textInput

def convertSpeechtoText(voiceInput):
    textInput=""
    # Initialize the recognizer
    r = sr.Recognizer()
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(voiceInput)
    engine.runAndWait()
   
        
       # use the microphone as source for input.
    with sr.Microphone() as source2:
           # handle background noise
           r.adjust_for_ambient_noise(source2, duration=0.2)
           #listens for the user's input
           audio2 = r.listen(source2)  
           # Using google to recognize audio
           MyText = r.recognize_google(audio2)
           textInput = MyText.lower()

    return textInput.
#1.2 convert the input to arabic for the purpose of getting arabic content 
def convertInputtoArabic(word):
    translator = Translator()
    srclng=translator.detect(word) #this will attempt to detect the word's language too
    arabicInput=translator.translate(word, dest='ar', src=srclng)
    
    return arabicInput.text
    
#step2: scrape resources for information using Diffbot (uncomplete)
def scrape_collect(topic):

    url = "https://api.diffbot.com/v3/image?url=https%3A%2F%2Fwww.diffbot.com%2Fproducts%2Fextract%2F&token=atheer"

    headers = {"accept": "application/json"}

    relatedInfo = requests.get(url, headers=headers)

    print(relatedInfo.text)
    return relatedInfo
#step3: convert the arabic content to the user's target language
def ContenttoTarget(content, targetLanguage='eng'):
    translator = Translator()
    getContent=translator.translate(content, dest='ar')

    return getContent
#step4: find keywords in the content to offer further expansion 
def findKeywords(text):
    return keywords
