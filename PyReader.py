import PyPDF2
import pyttsx3

class Read:

    def __init__(self,filename:str):
        
        self.pdf = PyPDF2.PdfFileReader(filename)
        self.driver = pyttsx3.init()
        
    def read(self,
             pageno = 0,
             voice:str = 'f',
             speed:int= 0,
             save:bool = False,
             filename:str = 'pdf_audio.mp3'):
        
        pdf_page = self.pdf.getPage(pageno)
        extracted_text = pdf_page.extractText()
        voices = self.driver.getProperty('voices')
        
        if voice == 'm':
            
            self.driver.setProperty('voice',voices[0].id)
            
        elif voice == 'f':
            
            self.driver.setProperty('voice',voices[1].id)
            
        else:
            print("\nValueError : 'm' or 'f' is valid.")
            return
            

        if speed !=0:
            
            rate = self.driver.getProperty('rate')
            self.driver.setProperty('rate',rate+speed)

        
        
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

    def readtxt(self,text:str,voice = 'f'):
        
        voices = self.driver.getProperty('voices')
        if voice == 'm':

            self.driver.setProperty('voice',voices[0].id)
            
        elif voice == 'f':

            self.driver.setProperty('voice',voices[1].id)
            
        self.driver.say(text)
        self.driver.runAndWait()


    def pdf_pages(self):
        
        return self.pdf.getNumPages()

    def pdf_info(self):

        return self.pdf.getDocumentInfo()

    def pdf_text(self,page_num:int):
        
        page = self.pdf.getPage(page_num)
        extracted_text = page.extractText()
        
        for sentence in extracted_text:
            print(sentence,end ='')

    def pdf_page(self,pageno:int):

        return self.pdf.getPage(pageno)

    def pdf_pageNum(page):

        return self.pdf.getPageNum(page)
        
