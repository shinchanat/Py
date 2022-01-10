"""
MIT LICENSE

Copyright 2021 (c) Harish M.

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

#__AUTHOR_NAME__ = "HARISH M"

__all__,version = ('read','content'),'0.4.5'

import PyPDF2 , pyttsx3

tts_engine = pyttsx3.init()
tts_voices, voice_types = tuple(tts_engine.getProperty('voices')),('m','f')
tts_speech_rate, tts_default_volume = tts_engine.getProperty('rate'),tts_engine.getProperty('volume')

class Open:

    def __init__(self,filename):

        self.type = filename[-3:]
        
        if self.type == 'pdf': self.pdf = PyPDF2.PdfFileReader(filename)
        elif self.type == 'txt': self.file = open(filename,'r')
        else: raise TypeError(f'__init__() got an unexpected file type {filename}.')
            
    def read(self,pgno = 0,voice= 'f',vol = 0,speech_rate= 0,save = False,filename = 'AudioBook.mp3'):

        if vol !=0: tts_engine.setProperty('volume',tts_default_volume+float(volume))
 
        if voice in voice_types: tts_engine.setProperty('voice',tts_voices[voice_types.index(voice)].id)
        else: assert voice in ('m','n'),\
              f"voice takes 'm' or 'f' as arguments,but got an unexpected keyword argument {voice}."
            
        if speech_rate !=0: tts_engine.setProperty('rate',tts_speech_rate+speech_rate)

        if self.type == 'pdf':
                if len(self.pdf.getPage(pgno).extractText()):

                        if save != False: tts_engine.save_to_file(self.pdf.getPage(pgno).extractText(),filename)
                        else: tts_engine.say(self.pdf.getPage(pgno).extractText())
                        tts_engine.runAndWait()

                else: assert False,f"empty page at {pgno}."
        elif self.type == 'txt': tts_engine.save_to_file(''.join(self.file),filename) if save != False else tts_engine.say(''.join(self.file))
        tts_engine.runAndWait()

    def content(self,pgno = 0):
        
        if self.type =='pdf':
            if len(self.pdf.getPage(pgno).extractText()): return ' '.join(((self.pdf.getPage(pgno).extractText()).split()))
        else: return self.file.read()
        
def read(text,voice = 'f',speech_rate = 0,vol = 0,save = False,filename = 'Audio.mp3'):
        
        if voice in voice_types :tts_engine.setProperty('voice',tts_voices[voice_types.index(voice)].id)
        else: assert voice in ('m','f'),\
              f"voice takes 'm' or 'f' as arguments,but got an unexpected keyword argument {voice}."
        
        if vol !=0: tts_engine.setProperty('volume',tts_default_volume+float(volume))
            
        if speech_rate != 0: tts_engine.setProperty('rate',tts_speech_rate+speech_rate)
            
        tts_engine.save_to_file(text,filename) if save != False else tts_engine.say(text)
        tts_engine.runAndWait()
