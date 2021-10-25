# PyAPdf a pdf manipulating package v0.0.1:-

#### NOTE: PyAPdf is in beta version.
## Methods inside PyAPdf Read class :-

* read().
* num_of_pages().
* pageNum().
* page().
* info().
* text().


# Installing process:-

* Make sure you have python3 installed in your system.
##### Run the following command in cmd to install krtana.

    
    pip install PyAPdf


# Example:-

## Pdf to Audio using PyAPdf.

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.

    pdf.read(10) # Must pass the page number that you want to read.

    ##################################################
    """parameter of read  methos:

    read(self,pageno , voice = 'f',speed = 0):
    
    read is a tts method.
    
    pageno:int --> 
    voice --> pass 'm' for male and 'f' for female voice.
              Defults to 'f'.

    speed :int --> pass an integer to change the reading speed.
                   Defults to 0.

                   Note: 0 means no chnage in speed."""

## Total pages in a pdf using PyAPDF:

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.
    pdf.num_of_pages() # returns the number of pages.

## Pdf Information using PyAPDF:

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.
    pdf.info() # returns the documents information. 

## Take a specific page from pdf using PyAPdf:

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.
    pagenumber = 10
    pdf.page(pagenumber)# returns the specified page.

    """Parameter in page methos:
    page(self,pageno)

    this method return the page , when a pageno is passed as an argument.


    pageno :int --> pass the page number to get the page."""

## Get the page number of a specific page using PyAPdf:

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.
    page = pdf.page(10)
    pdf.pageNum(page)

    """Parameter in page methods:

    pageNum(self,page)

    this methos return the page num, when a page is passed as an argument.

    page --> pass the page returned by the page method."""

## Text Extraction from pdf using PyAPdf:

    import PyAPdf

    pdf = PyAPdf.Read('filename.pdf') # the path or filename of the pdf.
    pagenumber = 10
    pdf.text(pagenumber)

    """Parameter in text method:

    text(self,pageno)

    this method return the extracted text from the pdf ,when a page number is 
    passed as an argument."""

    pageno --> pass the page number to extract text from that page.


# Contributors:
    * Harish M
# Thanks:

* Thanks to pyttsx3 and PyPdf2.
