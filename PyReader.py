"""MIT LICENSE

Copyright 2021 Harish



Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish,distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:



The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
__all__ = ['read','readtxt','pdf_info','pdf_pages',
           'pdf_pageNum','pdf_page','pdf_txt']

import PyPDF2
import pyttsx3

class PyReaderErrors:
    
    def voice_error(self,voice):
        
        if type(voice) == str:
            return ValueError("voice takes 'm' or 'f' as arguments ,but got {} as argument.".format(voice))
        
        else:
            return TypeError("voice takes string as an argument ,but got a different type.")
        
    def page_error(self):
        
            return ValueError("pageno takes a text containing page,but got a empty page.")
        
    
class Read:

    def __init__(self,filename:str):
        
        self.PyReaderError = PyReaderErrors()
        
        #checking the input file is a pdf or text file.
        if filename[-4:] == '.pdf':
            self.id = '.pdf'#just an object variable for identifing which file is currently passed to the constructor.
            self.pdf = PyPDF2.PdfFileReader(filename)#initializing the PdfFileReader class from PyPDF2
            
        elif filename[-4:] == '.txt':
            self.id = '.txt'
            self.file = open(filename,'r')
        else:
            raise FileNotFoundError('__init__ requires a pdf or text file, but got {}.'.format(filename))#througs an error if anyther file is passed.
            
        self.driver = pyttsx3.init()#initalizing tts driver from pyttsx3.
        self.voices = self.driver.getProperty('voices')#taking the voice property
        self.rate = self.driver.getProperty('rate')#taking the rate property.
        
    def read(self,
             pageno = 0,
             voice:str = 'f',
             speech_rate:int= 0,
             save:bool = False,
             filename:str = 'PyReader_audio.mp3'):
        
        if self.id == '.pdf':#check the file type.
            pdf_page = self.pdf.getPage(pageno)#reterving the perticular page from the passed pagenumber.
            extracted_text = pdf_page.extractText()#extracting the text the reterved page.

            #changine engine voice.
            if voice == 'm':
                self.driver.setProperty('voice',self.voices[0].id)
                
            elif voice == 'f':
                self.driver.setProperty('voice',self.voices[1].id)
                
            else:
                raise self.PyReaderError.voice_error(voice)#througs an error if anything else is passed.

            #changing the engine rate
            if speech_rate !=0:
                self.driver.setProperty('rate',self.rate+speech_rate)

            if len(extracted_text) != 0:#check for empty page.
                
                if save == True:
                    self.driver.save_to_file(extracted_text,filename)#saving the audio.
                    self.driver.runAndWait()
                    return
                
                elif save == 'sr':
                    self.driver.save_to_file(extracted_text,filename)
                    self.driver.say(extracted_text)
                    self.driver.runAndWait()
                    
                else:
                    self.driver.say(extracted_text)
                    self.driver.runAndWait()
                
            else:
               raise self.PyReaderError.page_error()#throughs an error if it's empty page.

        else:
            
            sentence = ''
            
            for text in self.file:#extracting text from textfile.
                sentence += text

            #changing engine voice
            if voice == 'f':#checking engine voice.
                self.driver.setProperty('voice',self.voices[1].id)
                
            elif voice == 'm':
                self.driver.setProperty('voice',self.voices[0].id)
                
            else:
                raise self.PyReaderError.voice_error(voice)#throughs an error is something else is passed.

            #changing engine rate.
            if speech_rate != 0:#checking engine rate.
                self.driver.setProperty('rate',self.rate+speech_rate)
                
            if save != False:
                
                self.driver.save_to_file(sentence,filename)#saving as audio.
                self.driver.runAndWait()
                self.file.close()
                
            else:
                self.driver.say(sentence)
                self.driver.runAndWait()
                self.file.close()#closing the textfile.

    
    def readtxt(self,
                text:str,
                voice = 'f',
                speech_rate = 0,
                save = False,
                filename = 'text_audio.mp3'):
        
        if voice == 'f':#checking engine voice.
            self.driver.setProperty('voice',self.voices[1].id)#changing engine voice.
            
        elif voice == 'm':
            self.driver.setProperty('voice',self.voices[0].id)
            
        else:
            raise self.PyReaderError.voice_error(voice)#throughs an error if something else is passed.

        if speech_rate != 0:#checking engine rate.
            self.driver.setProperty('rate',self.rate+speech_rate)#changing engine rate

        if save != False:
            
            self.driver.save_to_file(text,filename)#saving as audio
            self.driver.runAndWait()
            
        else:
            
            self.driver.say(text)
            self.driver.runAndWait()
        

    def pdf_pages(self):
        
        return self.pdf.getNumPages()

    def pdf_info(self):

        return self.pdf.getDocumentInfo()

    def pdf_txt(self,page_num:int = 0):
        
        page = self.pdf.getPage(page_num)
        extracted_text = page.extractText()

        extracted_sentence = ""
        for sentence in extracted_text:
            extracted_sentence += sentence

        return extracted_sentence

    def pdf_page(self,pageno:int):

        return self.pdf.getPage(pageno)

    def pdf_pageNum(self,page):

        return self.pdf.getPageNum(page)
