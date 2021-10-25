import PyPDF2
import pyttsx3

class Read:

    def __init__(self,filename:str):
        
        self.pdf = PyPDF2.PdfFileReader(filename)
        self.driver = pyttsx3.init()
        
    def read(self,
             pageno:int,
             voice = 'f',
             speed = 0):
        
        pdf_page = self.pdf.getPage(pageno)
        extracted_text = pdf_page.extractText()
        voices = self.driver.getProperty('voices')
        
        if voice == 'm':
            
            self.driver.setProperty('voice',voices[0].id)
            
        elif voice == 'f':
            
            self.driver.setProperty('voice',voices[1].id)
            
        else:
            print("\n ValueError : 'm' or 'f' is valid.")
            return
            

        if speed !=0:
            
            rate = self.driver.getProperty('rate')
            self.driver.setProperty('rate',rate+speed)
        
        if len(extracted_text) != 0:
            
            self.driver.say(extracted_text)
            self.driver.runAndWait()
            
        else:
            print("Blank_page.")

    def num_of_pages(self):
        
        return self.pdf.getNumPages()

    def info(self):

        return self.pdf.getDocumentInfo()

    def text(self,page_num:int):
        
        page = self.pdf.getPage(page_num)
        extracted_text = page.extractText()
        for sentence in extracted_text:
            print(sentence,end ='')

    def page(self,pageno:int):

        return self.pdf.getPage(pageno)

    def pageNum(page):

        return self.pdf.getPageNum(page)
        
