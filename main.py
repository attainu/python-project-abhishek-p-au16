#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil


def by_extension(path):

    audio = ['.mp3', '.wma', '.aac']

    vedio = ['.mp4', '.wmv', '. mkv', '.avi']

    images = ['.jpg', '.png', '.bmp']

    docs = ['.pdf', '.md', '.txt']

    softwear_files = ['.exe', '.apk']

    python = ['.py']

    folders = os.listdir(path)

    os.mkdir(path + '\\' + 'vedio')

    os.mkdir(path + '\\' + 'audio')

    os.mkdir(path + '\\' + 'images')

    os.mkdir(path + '\\' + 'docs')

    os.mkdir(path + '\\' + 'python')

    os.mkdir(path + '\\' + 'softwears')

    os.mkdir(path + '\\' + 'others')

    for folder in folders:

        extension = str(os.path.splitext(folder)[-1].lower())

        # print(extension)

        if extension == '':

            # print("this is a folder")

            files = os.listdir(path + '\\' + folder)

            for file in files:

                ext = os.path.splitext(file)[-1].lower()

                # print ext

                new_path = path + '\\' + folder + '\\'

                if ext in audio:

                    shutil.move(new_path + file, path + '\\audio')
                elif ext in vedio:

                    shutil.move(new_path + file, path + '\\vedio')
                elif ext in images:

                    shutil.move(new_path + file, path + '\\images')
                elif ext in docs:

                    shutil.move(new_path + file, path + '\\docs')
                elif ext in python:

                    shutil.move(new_path + file, path + '\\python')
                elif ext in softwear_files:

                    shutil.move(new_path + file, path + '\\softwears')
        elif extension in audio:

            shutil.move(path + '\\' + folder, path + '\\audio')
        elif extension in vedio:

            shutil.move(path + '\\' + folder, path + '\\vedio')
        elif extension in images:

            shutil.move(path + '\\' + folder, path + '\\images')
        elif extension in docs:

            shutil.move(path + '\\' + folder, path + '\\docs')
        elif extension in python:

            shutil.move(path + '\\' + folder, path + '\\pyhton')
        elif extension in softwear_files:

            shutil.move(path + '\\' + folder, path + '\\softwears')
        else:

            shutil.move(path + '\\' + folder, path + '\\others')

    print ('-----successfully Arranged your files by extension-----')


def by_size(cpath):
    files = os.listdir(cpath)
    os.mkdir(cpath + '\\' + 'byte_files')

    os.mkdir(cpath + '\\' + 'mb_files')

    os.mkdir(cpath + '\\' + 'kb_files')

    os.mkdir(cpath + '\\' + 'gb_files')

    for file in files:
        size = os.path.getsize(cpath + '\\' + file)

        # print(size)

        if size < 1024:

            shutil.move(cpath + '\\' + file, cpath + '\\byte_files')

        if size in range(1024, 1000000):

            shutil.move(cpath + '\\' + file, cpath + '\\kb_files')
        if size in range(1000000, 1000000000):

            shutil.move(os.path.join(cpath, file), cpath + '\\mb_files')
        if size > 1000000000:

            shutil.move(cpath + '\\' + file, cpath + '\\gb_files')
    print ('--------successfully arranged by size-----------')


if __name__ == '__main__':
    print("-------junk file organizer-------")
    path= input("please enter your path :  ")
    print("select your options....")
    print("enter 1 for arrange by extension")
    print("enetr 2 for arrange by size")
    option =input()
    if option == "1":
        by_extension(path)
    elif option== "2":
        by_size(path)
    else:
        print("enter a valid input")