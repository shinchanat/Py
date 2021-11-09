"""MIT LICENSE

Copyright 2021 (c) Harish.



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

version = '0.0.9'

import PyPDF2
import pyttsx3

tts_engine = pyttsx3.init()#initalizing text-to-speech object.
tts_voices = driver.getProperty('voices')#storing the text-to-speech voices property in voices variable.
speech_rate = driver.getProperty('rate')#storing the text-to-speech rate property in rate variable.
default_volume = driver.getProperty('volume')#storing the text-to-speech default vloume level in default_volume variable.

    
def voice_error(voice):
        
        """this function throws a value error if the voice object has not got the desired value,
        else throws a type error if the voice object is not a string."""
        
        if type(voice) == str:
            return ValueError("voice takes 'm' or 'f' as arguments,"
                              +"but got an unexpected keyword argument {}.".format(voice))
        
        else:
            return TypeError("voice got an unexpected keyword argument {}.".format(voice))
        
def page_error():
        
        """throws a value error if the page is empty."""
        
            return ValueError("pageno takes a text containing page,but got a empty page.")
        

class Open:

    def __init__(self,filename:str):
            
        self.id = filename[-4:]#for knowing which filetype is passed to the constructor's filename argument.

        """if the input file is a pdf,opening the Pdf by the PyPdf2 module for performing operations on pdf.

        if the input file is a text file then opens the file and assigns the data to self.file object.

        else if the input file is not a pdf nor a text file the throws a type error."""
        
        if filename[-4:] == '.pdf':
            self.pdf = PyPDF2.PdfFileReader(filename)#initializing the PdfFileReader class object.
            
        elif filename[-4:] == '.txt':
            self.file = open(filename,'r')
            
        else:
            raise TypeError('__init__() got an unexpected keyword argument {}.'.format(filename))#througs an error if anyther file is passed.
            
        
    def read(self,
             pageno = 0,
             voice:str = 'f',
             volume = 0,
             speech_rate:int= 0,
             save:bool = False,
             filename:str = 'PyReader_audio.mp3'):
        
        if volume !=0:
                
                """checks wether the user wanted to increased/decreased the volume.
                   0 means the user don't wanted to increased/decreased the volume."""
                
            driver.setProperty('volume',default_volume+float(volume))#setting up the volume.

        if voice == 'm':

                """checks wether to apply the female/male voice for the text-to-speech engine
                   f = female, m = male"""
                
                driver.setProperty('voice',voices[0].id)
                
        elif voice == 'f':
                driver.setProperty('voice',voices[1].id)
                
        else:
            raise voice_error(voice)#througs an error if anything else is passed other than 'f'/'m'.

            
            if speech_rate !=0:
                    
                    """checks wether the user wanted to increased/decreased the text-to-speech engine speech_rate.
                   0 means the user don't wanted to increased/decreased the text-to-speech engine speech_rate."""
                    
                driver.setProperty('rate',rate+speech_rate)
                
        if self.id == '.pdf':
                """this block runs only if the input file is a pdf,otherwise jumps to the else block."""
                
            if len(self.pdf.getPage(pageno).extractText()) != 0:
                    """checks wether the page is containing text or not.
                        if not jumps to else block."""
                
                if save != False:
                        """checks wether the user wanted to save the text-to-speech audio
                           if set it to True,then saves the audio in the current dir where your .py is stored."""
                        
                    driver.save_to_file(self.pdf.getPage(pageno).extractText(),filename)#saving the audio.
                
                elif save == 'sr':
                        """ save is set it to 'sr' then it save the audio and reads the content."""
                    driver.save_to_file(self.pdf.getPage(pageno).extractText(),filename)
                    driver.say(self.pdf.getPage(pageno).extractText())
                    
                else:
                        """save is set to False ,it just reads the content."""
                        
                    driver.say(self.pdf.getPage(pageno).extractText())
                driver.runAndWait()
                
            else:
               raise page_error()#throughs an error if it's empty page.

        else:
            
            sentence = ''
            
            for text in self.file:#extracting text from textfile.
                sentence += text
                
            if save != False:
                        """checks wether the user wanted to save the text-to-speech audio
                           if set it to True,then saves the audio in the current dir where your .py is stored."""
                driver.save_to_file(sentence,filename)#saving as audio.
            else:
                    """save is set to False ,it just reads the content."""
                driver.say(sentence)
                
        driver.runAndWait()
        self.file.close()#closing the textfile.

    
    
        

    def pdf_pages(self):
            """returns totals number of pages """
        return self.pdf.getNumPages()

    def pdf_info(self):
            """returns the information about tthe pdf."""
        return self.pdf.getDocumentInfo()

    def print(self,pageno:int = 0):
            """return the extracted text from the pdf."""
        return ((self.pdf.getPage(pageno).extractText()).split())

    def pdf_page(self,pageno:int):
            """returns a  perticularpage page."""
        return self.pdf.getPage(pageno)

    def pdf_pageNum(self,page):
            """returns the pagenumber of a perticular page,must pass a page object."""
        return self.pdf.getPageNum(page)


def readtxt(text:str,
            voice = 'f',
            speech_rate = 0,
            volume = 0,
            save = False,
            filename = 'text_audio.mp3'):
        
        if voice == 'f':#checking engine voice.
            driver.setProperty('voice',voices[1].id)#changing engine voice.
            
        elif voice == 'm':
            driver.setProperty('voice',voices[0].id)
            
        else:
            raise voice_error(voice)#throughs an error if something else is passed.

        if volume !=0:
            driver.setProperty('volume',default_volume+float(volume))

        if speech_rate != 0:#checking engine rate.
            driver.setProperty('rate',rate+speech_rate)#changing engine rate

        if save != False:
            
            driver.save_to_file(text,filename)#saving as audio
            
        else:
            
            driver.say(text)
        driver.runAndWait()
