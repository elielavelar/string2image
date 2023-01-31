<p style="text-align: center">
    <a href="http://172.20.28.201:3000/Muhlbauer_El_Salvador" target="_blank">
        <img src="https://mb.citas-dui-sv.com/img/logo-alt.png" height="100px" alt="MB Logo">
    </a>
</p>
<h1 style="text-align: center">String to Image - Log Scraper</h1>
<br/>
Script application to scrap logs and convert base64 strings to images and save related message data.

DIRECTORY STRUCTURE
-------------------
```
venv/              Virtual environment
string2image.py    Main script to scrap logs and convert base64 strings to images
.env               Environment variables
```

REQUIREMENTS
~~~~~~~~~~~~
- Python 3.6.9
- pip 21.2.4
- Virtual environment
- pyinstaller
- auto-py-to-exe *optional
~~~~~~~~~~~~

INSTALLATION
~~~~~~~~~~~~
METHOD 1: Using virtual environment
- Create virtual environment
- Activate virtual environment
- Install requirements
- Create .env file
- Run script with python3

METHOD 2: Building executable file
- Create virtual environment
- Activate virtual environment
- Install requirements
- Create .env file
- Run pyinstaller or auto-py-to-exe *optional
- Run executable file
~~~~~~~~~~~~

CONFIGURATION
~~~~~~~~~~~~
- Create .env file
- Set environment variables:
    + FILE_SOURCE_PATH: Path to the file to scrap
    + DIRECTORY_PATH: Path to the directory where the images will be saved
    + RESULTS_PATH: Sub-directory's name where the results will be saved 
    + IMAGE_EXTENSION: Extension of the image to save
    + IMAGES_PATH: Sub-directory's name where the images will be saved
    + MESSAGE_EXTENSION: Extension of the message file to save
    + MESSAGES_PATH: Sub-directory's name where the messages will be saved
    + STRING_TO_FIND_START: String to find the start of the base64 string
    + STRING_TO_FIND_END: String to find the end of the base64 string
~~~~~~~~~~~~

BUILT WITH
~~~~~~~~~~~~
- Python 3.11.0
- Virtual environment
- IDE: IntelliJ IDEA
~~~~~~~~~~~~

AUTHOR
- Eliel Avelar
<br/>
<a href="mailto:ElielAbisai.AvelarJaimes@muehlbauer.de">E-mail address</a>

