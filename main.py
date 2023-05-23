import os
import shutil

supported = open('supportedType.csv','r')
for line in supported:
    line = line.split(',')
    if line[0] == 'image':
        image = line[1:-1]
    elif line[0] == 'video':
        video = line[1:-1]
    elif line[0] == 'audio':
        audio = line[1:-1]
    elif line[0] == 'document':
        document = line[1:-1]
    elif line[0] == 'compressed':
        compressed = line[1:-1]
    elif line[0] == 'executable':
        executable = line[1:-1]
    else:
        pass
supported.close()

mainFolder = input("\nEnter the directory contains files need to be sorted:\n")
while not os.path.isdir(mainFolder):
    mainFolder = input("Invalid directory! Please re-enter:\n")

os.chdir(mainFolder)
for file in os.listdir():
    if os.path.splitext(file)[1] in image:
        if not os.path.isdir(mainFolder + '\IMAGE'):
            os.makedirs('IMAGE')
        shutil.move(file, mainFolder + '\IMAGE')
    elif os.path.splitext(file)[1] in video:
        if not os.path.isdir(mainFolder + '\VIDEO'):
            os.makedirs('VIDEO')
        shutil.move(file, mainFolder + '\VIDEO')
    elif os.path.splitext(file)[1] in audio:
        if not os.path.isdir(mainFolder + '\AUDIO'):
            os.makedirs('AUDIO')
        shutil.move(file, mainFolder + 'AUDIO')
    elif os.path.splitext(file)[1] in document:
        if not os.path.isdir(mainFolder + '\DOCUMENT'):
            os.makedirs('DOCUMENT')
        shutil.move(file, mainFolder + '\DOCUMENT')
    elif os.path.splitext(file)[1] in compressed:
        if not os.path.isdir(mainFolder + '\COMPRESSED'):
            os.makedirs('COMPRESSED')
        shutil.move(file, mainFolder + '\COMPRESSED')
    elif os.path.splitext(file)[1] in executable:
        if not os.path.isdir(mainFolder + '\EXECUTABLE'):
            os.makedirs('EXECUTABLE')
        shutil.move(file, mainFolder + '\EXECUTABLE')
    else:
        if not os.path.isdir(mainFolder + '\MISSCLANIOUS'):
            os.makedirs('MISSCLANIOUS')   
        shutil.move(file, mainFolder + '\MISSCLANIOUS')

print("\nORGANIZING COMPLETE!")
os.startfile(mainFolder)