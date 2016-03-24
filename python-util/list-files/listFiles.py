#!python3
# 说明：
# 列出当前文件夹下指定扩展名的所有文件。例如：
# python lisFile.py xlsx，列出当前文件夹下所有xlsx格式的文件

import sys, os

def listFile(ext):
    # 根据扩展名，返回文件清单
    files = [file for file in os.listdir() if file.endswith('.' + ext)]
    return files

def fileAbsPath(file):
    # 返回文件的绝对路径
    absPath = os.path.abspath('.')
    file_abs_path = os.path.join(absPath, file)
    return file_abs_path

def getFile(file_list):
    # 根据sys.argv清单，返回文件名及绝对路径
    result = []
    for file in file_list:
        if os.path.isfile(file):
            fileAbsPath = os.path.join(os.path.abspath('.'), file)
            result.append( (file, fileAbsPath) )
    return result


try:
    # 获取文件清单
    # files = listFile(sys.argv[1])

    # 获取某个文件的绝对路径
    # path = fileAbsPath(files[0])

    # 从sys.argv获取文件，及文件的绝对路径
    get_files = getFile(sys.argv[1:])
    print(get_files)

except IndexError:
    # 如果没有在命令行中指定扩展名，则会显示以下提示

    print('说明：请在命令行中指定一个文件扩展名或文件名。\n'
          '例如：python listFiles.py xls')
