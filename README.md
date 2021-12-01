#PyReader Version 0.1.0:-
* Pyreader is a python package used for reading pdf and text files by applying text-to-speech.

#PyReader Open class:-
* This class is used to creats the file object.
###Methods inside open class:-

##How to open a file:-
    
    from PyReader import*
    
    file = open('filename with extension')

##How use tts to read the file:-

    from PyReader import*

    file = open('filename with extension')
    file.read()

####It doesn't returns anything ,it just reads the page from the file using tts
####NOTE : read function reads the first page by default.

##How to read a perticular page:-

    from PyReader import*
    
    file = open('filename with extension')
    file.read(pageno = 'any_page_no')

####NOTE : It raises an error if the given page is empty.

###How to change tts reader voice:-
    
    from PyReader import*

    file = open('filename with extension')
    file.read(voice = 'm')

####voice is an optional parameter set default to 'f' female version,pass 'm' for male version.
####It raises an error if anyother argument is passed except 'f' & 'm'.

###How to change to volume:-

    from PyReader import*
    
    file = open('filename with extension')
    file.read(volume = 'pass_a_integer_value')

####volume is an optional parameter set default to zero,here zero represents no change in volume.

###How to change the tts reading speed:-

    from PyReader import*

    file = open('filename with extension')
    file.read(speech_rate = 'pass_a_integer_value')

####speech_rate is an optional parameter set default to zero,like volume parameter here zero represents no change in speech_rate.

###How to convert page as audio:-

    from PyReader import*

    file = open('filename with extension')
    file.read(save = True)

####save is an optional parameter set default to False,set to True to save the audio. while saveing it won't read anything.
####Note: It saves the audio as 'PyReader_audio.mp3' in the current directory.

###How to change the audio filename while saving:-

    from PyReader import*

    file = open('filename with extension')
    file.read(save = True,filename = 'any_name.mp3')

####it save the audio as 'any_name.mp3' in the current directory.

###How to read a text:-

    from PyReader import*
    
    read('any_text')

###How to print the extracted text on screen.

    from PyReader import*

    file = open('filename with extension')
    print(file.content())

####It prints the first page on screen by default. use the pgno parameter to print the text on screen from a perticular page.
####exmaple:
    
    file.content(pageno = 'any_page_number')#pageno should be an integer


####Note : It returns the extracted text from pdf file and works only for pdf file.
