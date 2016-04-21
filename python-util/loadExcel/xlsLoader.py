import win32com.client as win32
import os, sys

def getArgvFile(file_list):
    # 根据sys.argv清单，返回文件名及绝对路径
    result = []
    for file in file_list:
        if os.path.isfile(file):
            fileAbsPath = os.path.join(os.path.abspath('.'), file)
            result.append( (file, fileAbsPath) )
    return result

def getExcelRows(file):
    '''
      the parameter *file* should be a tuple which
      consists of file_name, abs_path_with_file_name
    '''

    excel = win32.DispatchEx('Excel.Application')
    wb = excel.Workbooks.Open(file[1])
    ws = wb.Worksheets(1)
    cellValue = ws.Range('A10000').Value
    print(cellValue)

    wb.Close()

excelFiles = getArgvFile(sys.argv[1:])
for file in excelFiles:
    # here file should be a 
    # tuple (file_name, abs_path_with_file_name)
    getExcelRows(file)

