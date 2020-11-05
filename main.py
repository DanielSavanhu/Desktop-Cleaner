import os
import shutil
import send2trash


def delete():
    oldpath = input('Input currect directory:   ')
    if not os.path.exists(oldpath):
        print('Path not found')
        quit()
    filetype = input("Input file extension or if all, Enter '*' :\n")
    for files in os.listdir(oldpath):
        if filetype.lower() in files.lower():
            status = files
            result = input('Do you wanna delete: ' + status +'=>(y, n)  ').lower()

            if 'y' in result:
                send2trash.send2trash(os.path.join(oldpath, status))
                print(status + " has been deleted")


def copy_folder():
    oldpath = input('Input currect directory:   ')
    newpath = input('Enter new path:    ')
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    if not os.path.exists(oldpath):
        print('Path not found')
        quit()
    search = input('Folder: ')
    for folders in os.listdir(oldpath):
        if search.lower() in folders.lower():
            status = shutil.copytree(os.path.join(oldpath, folders), newpath)
            print(status)


def copy_files():
    oldpath = input('Input currect directory:   ')
    newpath = input('Enter new path:    ')
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    if not os.path.exists(oldpath):
        print('Path not found')
        quit()
    filetype = input('Input file extension e.g .jpg\n')
    for files in os.listdir(oldpath):
        if filetype in files:
            status = shutil.copy(os.path.join(oldpath, files), newpath)
            print(status)

def rename():
    oldpath = input('Input currect directory:   ')
    if not os.path.exists(oldpath):
        print('Path not found')
        quit()
    # filetype = input("Input file extension or if all, Enter '*' :\n")
    for files in os.listdir(oldpath):
        if len(files) > 10:
            os.renames(files, files[len(files)-9:])
            print('renamed to:  '+ files[len(files)-9:])


def move_files():
    while True:
        oldpath = input('Input currect directory:   ')
        newpath = input('Enter new path:    ')
        if not os.path.exists(newpath):
            os.mkdir(newpath)
        if not os.path.exists(oldpath):
            print('Path not found')
            quit()
        filetype = input('Input file extension e.g .jpg\n')
        for files in os.listdir(oldpath):
            if filetype in files:
                if not os.path.exists(newpath + files):
                    status = shutil.move(os.path.join(oldpath, files), newpath)
                    print(status)
                else:
                    print('File exists')

def list_files():
    oldpath = input('Input currect directory:   ')
    if not os.path.exists(oldpath):
        print('Path not found')
        quit()
    filetype = input("Input file extension or if all, Enter '*' :\n")
    for files in os.listdir(oldpath):
        if '*' in filetype:
            status = files
            print(status)
        elif filetype.lower() in files.lower():
            status = files
            print(status)

gi
choose = input("ListFiles: '1':  \nCopy Files: '2':  \nCopy Folder: '3':   \nMove Files: 4:\nDelete: 5: \nRename:'6': ")
if '1' in choose:
    list_files()
elif '2' in choose:
    copy_files()
elif '3' in choose:
    copy_folder()
elif '4' in choose:
    move_files()
elif '5' in choose:
    delete()
elif '6' in choose:
    rename()