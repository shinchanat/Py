"""
MIT LICENSE

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


__all__ = ['read','readtxt','print']

version = '0.1.0'

import PyPDF2
import pyttsx3

tts_engine = pyttsx3.init()#initalizing text-to-speech object.
tts_voices = tts_engine.getProperty('voices')#storing the text-to-speech voices property in voices variable.
tts_speech_rate = tts_engine.getProperty('rate')#storing the text-to-speech rate property in rate variable.
tts_default_volume = tts_engine.getProperty('volume')#storing

def voice_error(voice):
        
        if type(voice) == str:
            return ValueError("voice takes 'm' or 'f' as arguments,"
                              +"but got an unexpected keyword argument {}.".format(voice))
        
        else:
            return TypeError("voice got an unexpected keyword argument {}.".format(voice))
        
def page_error():
        
        return ValueError("pageno takes a text containing page,but got a empty page.")
        

class Open:

    def __init__(self,filename:str):
            
        self.id = filename[-4:]#for knowing which filetype is passed to the constructor's filename argument.

        
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
                tts_engine.setProperty('volume',tts_default_volume+float(volume))#setting up the volume.

        if voice == 'm':

                tts_engine.setProperty('voice',tts_voices[0].id)
                
        elif voice == 'f':
                tts_engine.setProperty('voice',tts_voices[1].id)
                
        else:
            raise voice_error(voice)#througs an error if anything else is passed other than 'f'/'m'

            
        if speech_rate !=0:
                    tts_engine.setProperty('rate',tts_speech_rate+speech_rate)
                
        if self.id == '.pdf':

                if len(self.pdf.getPage(pageno).extractText()) != 0:
                        
                        if save != False:
                                tts_engine.save_to_file(self.pdf.getPage(pageno).extractText(),filename)#saving the audio
                        else:
                                tts_engine.say(self.pdf.getPage(pageno).extractText())

                        tts_engine.runAndWait()
                else:
                        raise page_error()
                
        
        

        else:
            
            sentence = ''
            
            for text in self.file:
                sentence += text
                
            if save != False:
                    tts_engine.save_to_file(sentence,filename)
            else:
                    tts_engine.say(sentence)
                
            tts_engine.runAndWait()
            self.file.close()


    def print(self,pageno:int = 0):
        extracted_text_list = ((self.pdf.getPage(pageno).extractText()).split())
        sentence = ''
        for word in extracted_text_list:
                sentence += word+' '

        return sentence
                                
def readtxt(text:str,
            voice = 'f',
            speech_rate = 0,
            volume = 0,
            save = False,
            filename = 'text_audio.mp3'):
        
        if voice == 'f':#checking engine voice.
            tts_engine.setProperty('voice',tts_voices[1].id)#changing engine voice.
            
        elif voice == 'm':
            tts_engine.setProperty('voice',tts_voices[0].id)
            
        else:
            raise voice_error(voice)#throughs an error if something else is passed.

        if volume !=0:
            tts_engine.setProperty('volume',tts_default_volume+float(volume))

        if speech_rate != 0:#checking engine rate.
            tts_engine.setProperty('rate',tts_speech_rate+speech_rate)#changing engine rate

        if save != False:
            
            tts_engine.save_to_file(text,filename)#saving as audio
            
        else:
            
            tts_engine.say(text)
        tts_engine.runAndWait()
