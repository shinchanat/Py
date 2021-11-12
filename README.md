#PyReader Version 0.1.0:-
* Pyreader is a python package used for reading pdf and text files by applying text-to-speech.

#PyReader Open class:-
* This class is used to creats the file object.
###Methods inside open class:-

##How to open a file:-
    
    import PyReader
    
    file = PyReader.Open('filename with extension')

##How use tts to read the file:-

    import PyReader

    file = PyReader.Open('filename with extension')
    file.read()

####It doesn't returns anything ,it just reads the page from the file using tts
####NOTE : read function reads the first page by default.

##How to read a perticular page:-

    import PyReader
    
    file = PyReader.Open('filename with extension')
    file.read(pageno = 'any_page_no')

####NOTE : It raises an error if the given page is empty.

###How to change tts reader voice:-
    
    import PyReader

    file = PyReader.Open('filename with extension')
    file.read(voice = 'm')

####voice is an optional parameter set default to 'f' female version,pass 'm' for male version.
####It raises an error if anyother argument is passed except 'f' & 'm'.

###How to change to volume:-

    import PyReader
    
    file = PyReader.Open('filename with extension')
    file.read(volume = 'pass_a_integer_value')

####volume is an optional parameter set default to zero,here zero represents no change in volume.

###How to change the tts reading speed:-

    import PyReader

    file = PyReader.Open('filename with extension')
    file.read(speech_rate = 'pass_a_integer_value')

####speech_rate is an optional parameter set default to zero,like volume parameter here zero represents no change in speech_rate.

###How to save readed page as a audio:-

    import PyReader

    file = PyReader.Open('filename with extension')
    file.read(save = True)

####save is an optional parameter set default to False,set to True to save the audio. while saveing it won't read anything.
####Note: It saves the audio as 'PyReader_audio.mp3' in the current directory.

###How to change the audio filename while saving:-

    import PyReader

    file = PyReader.Open('filename with extension')
    file.read(save = True,filename = 'any_name.mp3')

####it save the audio as 'any_name.mp3' in the current directory.

###How to read a text:-

    import PyReader
    
    PyReader.readtxt('any_text')

####NOTE : All the parameter used in read method can be in readtxt method also.

###How to print the extracted text on screen.

    import PyReader

    file = PyReader.Open('filename with extension')
    file.print()

####It prints the first page on screen by default. use the pageno parameter to print the text on screen from a perticular page.
####exmaple:
    .........
    file.print(pageno = 'any_page_number')#pageno should be an integer


####Note : It returns the extracted text from pdf file and works only for pdf file.




