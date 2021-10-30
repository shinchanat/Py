

__all__ = ['read','readtxt','pdf_info','pdf_pages',
           'pdf_pageNum','pdf_page','pdf_txt']

import PyPDF2
import pyttsx3

class Read:

    def __init__(self,filename:str):

        if filename[-4:] == '.pdf':
            
            self.id = '.pdf'
            self.pdf = PyPDF2.PdfFileReader(filename)
            
        elif filename[-4:] == '.txt':
            self.id = '.txt'
            self.file = open(filename,'r')
        
        else:
            print("Currently PyReader can only read text file and pdf.")
            
        self.driver = pyttsx3.init()
        self.voices = self.driver.getProperty('voices')
        self.rate = self.driver.getProperty('rate')  
        
    def read(self,
             pageno = 0,
             voice:str = 'f',
             speech_rate:int= 0,
             save:bool = False,
             filename:str = 'pdf_audio.mp3'):
        
        if self.id == '.pdf':
            pdf_page = self.pdf.getPage(pageno)
            extracted_text = pdf_page.extractText()
            
            if voice == 'm':
                self.driver.setProperty('voice',self.voices[0].id)
                
            elif voice == 'f':
                self.driver.setProperty('voice',self.voices[1].id)
                
            else:
                print("\nValueError : 'm' or 'f' is valid.")
                return
            
            if speech_rate !=0:
                self.driver.setProperty('rate',self.rate+speech_rate)

            if len(extracted_text) != 0:
                if save == True:
                    self.driver.save_to_file(extracted_text,filename)
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
                print('Blank page')
        else:
            
            sentence = ''
            
            for text in self.file:
                sentence += text

            if voice == 'f':
                self.driver.setProperty('voice',self.voices[1].id)
                
            elif voice == 'm':
                self.driver.setProperty('voice',self.voices[0].id)
                
            else:
                print("ValueError: ['f','m'] are allowed.")

            if speech_rate != 0:
                self.driver.setProperty('rate',self.rate+speech_rate)
                
            if save != False:
                filename = 'textfile_audio.mp3'
                self.driver.save_to_file(sentence,filename)
                self.driver.runAndWait()
                self.file.close()
                
            else:
                self.driver.say(sentence)
                self.driver.runAndWait()
                self.file.close()

    def read_txt(self,
                text:str,
                voice = 'f',
                speech_rate = 0,
                save = False,
                filename = 'text_audio.mp3'):
        
        if voice == 'f':
            self.driver.setProperty('voice',self.voices[1].id)
        elif voice == 'm':
            self.driver.setProperty('voice',self.voices[0].id)

        if speech_rate != 0:
            self.driver.setProperty('rate',self.rate+speech_rate)

        if save != False:
            
            self.driver.save_to_file(text,filename)
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

    def pdf_pageNum(page):

        return self.pdf.getPageNum(page)
