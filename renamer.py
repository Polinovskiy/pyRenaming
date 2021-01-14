import os
import tkinter as tk
from tkinter import filedialog
from msvcrt import getch

def rename(old_name,new_name):
    try:
        os.rename(old_name, new_name)
    except Exception as err:
        print('Не удалось переименовать: ' + str(err))
        input()
def need_to_replace(old_name,new_name):
    print('<- | ->')
    while True:
        key = ord(getch())
        if key == 75:
            break
        elif key==77:
            rename(old_name, new_name)
            break

def readDictionaryFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, "r", encoding="utf-8") as file_handler:
            for line in file_handler:
                line=line.strip()
                if line[0]=='#':
                    continue
                splitedAlphs=line.split(':')
                dict[splitedAlphs[0]]=splitedAlphs[1]
        if len(dict)==0:
            print('Cловарь <' + fileName + '> пуст. Заполните его по следующему принципу: \n<старый символ>:<новый символ>\n<старый символ>:<новый символ>')
            print('и запустите программу снова')
            input()
            exit(1)
    else:
        print('файл словарь <'+fileName+'> не найден. Создайте файл с данным именем в каталоге с программой и запустите ее снова')
        input()
        exit(1)
def replacer(replace_string):
    replaced_string=replace_string
    for indx in range(len(replaced_string)):
        if replace_string[indx] in dict.keys():
            replace_string = replace_string.replace(replace_string[indx], dict[replace_string[indx]])
    return replace_string
def dispatch(dirName,files):
    for file in files:
        new_file=replacer(file)
        if id(file)!=id(new_file):
            print('f: '+ dirName+os.path.sep +file+' -> ..'+os.path.sep +new_file)
            if ans=='y':
                need_to_replace(dirName+os.sep+file,dirName+os.sep+new_file)
            else:
                rename(dirName+os.sep+file,dirName+os.sep+new_file)
    dName=dirName.split(os.path.sep)[-1]
    new_dName=replacer(dName)
    dir_path=os.path.sep.join(dirName.split(os.path.sep)[0:-1])+os.path.sep
    if id(new_dName)!=id(dName):
        print('dir: ' + dir_path+ dName + ' -> ..'+os.path.sep + new_dName)
        if ans == 'y':
            need_to_replace(dir_path+dName,dir_path+new_dName)
        else:
            rename(dir_path+dName,dir_path+new_dName)

dict={}
readDictionaryFile('dictionary.txt')
print('Словарь для замен:')
print(dict)
print('>>> Выберите корневой каталог для переименования <<<')
root = tk.Tk()
root.withdraw()

dir_path = filedialog.askdirectory()
if dir_path=='':
    print('Каталог не выбран, завершаю программу')
    input()
else:
    print('Каталог выбран: '+dir_path)
    print('Ручной режим обработки? y/n')
    ans=input()
    if ans=='y':
        print('<- оставить\n-> заменить')
    print('>>> Процесс замены запущен <<<')
    #d={'И':'ł', 'й':'ę', 'Ш':'ś', 'Ж':'ć', 'Э':'Ł', 'ф':'ń','в':'ó', 'л':'ź', 'е':'ą', 'Ч':'Ś' }
    tree = os.walk(dir_path,topdown=False)
    for i in tree:
         dispatch(i[0],i[2])
    print('>>> Процесс замены завершен <<<')
    input()




