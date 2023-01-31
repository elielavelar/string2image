import os
import base64
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

currentDate = datetime.now()
filesource = os.getenv('FILE_SOURCE_PATH')
directory_main_path = os.getenv('DIRECTORY_PATH') or os.path.dirname(os.path.realpath(__file__)) + '/'
results_path = os.getenv('RESULTS_PATH') or 'results/'
directory_path = directory_main_path + results_path+currentDate.strftime('%Y%m%d_%H%M%S')+'/'
images_path = os.getenv('IMAGES_PATH') or 'images/'
messages_path = os.getenv('MESSAGES_PATH') or 'messages/'

imageExtension = os.getenv('IMAGE_EXTENSION') or 'jpg'
messageExtension = os.getenv('MESSAGE_EXTENSION') or 'txt'

stringFindStart = os.getenv('STRING_FIND_START') or 'imageAsPNG: '
stringFindEnd = os.getenv('STRING_FIND_END') or 'maskAsPNG:'
messageStart = 'DEBUG d.m.s.c.FaceImageProcessingController.icaoCheck - ' \
               '=========================================START face image icao ' \
               'check============================================='
messageEnd = 'DEBUG d.m.s.c.FaceImageProcessingController.icaoCheck - =========================================END ' \
             'face image icao check!============================================='

fileresult = directory_path + 'result.'+messageExtension


def getbetween(string, start, end):
    return string.split(start)[1].split(end)[0]


def checkdirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


checkdirectory(directory_path)
file_result = open(fileresult, 'w')

image_path = directory_path + images_path
message_path = directory_path + messages_path
checkdirectory(image_path)
checkdirectory(message_path)

messageStarted = False
index = 0

with open(filesource) as f:
    for line in f:
        if stringFindStart in line:
            content = getbetween(line, stringFindStart, stringFindEnd)
            result = content
            index = index + 1
            file_result.write('=========================================================\n')
            file_result.write('Imagen '+str(index)+'\n')
            file_result.write('=========================================================\n')
            file_result.write(line)
            file_result.write(result)

            x = datetime.now()
            file_name = x.strftime('%Y%m%d_%H%M%S_%f.'+imageExtension)

            file_path = image_path + file_name

            fp = open(file_path, 'wb')
            fp.write(base64.b64decode(result))
            fp.close()

        if messageStart in line or messageStarted:
            if messageStart in line:
                messageDate = datetime.now()
                message_file_name = messageDate.strftime('%Y%m%d_%H%M%S_%f.'+messageExtension)
                file_message = open(message_path+message_file_name, 'w')
                messageStarted = True

            if messageEnd in line:
                messageStarted = False
                file_message.write(line)
                file_message.close()

            if messageStarted:
                file_message.write(line)

            file_result.write(line)

file_result.close()
