import json
import shutil
import os, sys

file = 'HYH3 CCMS-A 16DO.json'
code = None 

def getAllFiles(fileExt):
    files = [file for file in os.listdir() if file.endswith('.' + fileExt)]
    return files

def getCabientId(dataSet):
    code = ''
    for data in dataSet:
        if not ( data['cabinet_id'] == None ):
            code = data['cabinet_id']
            break;
    if code == '':
        print('Can not find cabinet_id');

    return code

def main(file):
    with open(file, 'r', encoding='utf-8') as openf:
        dataSet = json.loads(openf.read())
        

    code = getCabientId(dataSet)

    if code != None:
        backup = 'backup_' + file

        # this line has nothing to do with logic
        # just to avoiding variable name confusion.
        new_file = file  
        shutil.move(file, backup)

        with open(new_file, 'w') as closef:
            closef.write('[\n');

            count = 0
            for data in dataSet:
                count += 1
                data['cabinet_id'] = code
                stringObj = json.dumps(data, ensure_ascii=False)
                closef.write(stringObj)
                if count < len(dataSet):
                    closef.write(',\n');
                else:
                    closef.write('\n');

            closef.write(']');

if __name__ == '__main__':

    jsonFiles = getAllFiles('json');
    countFiles = 0
    for file in jsonFiles:
        countFiles += 1
        message = str( countFiles ) + '. ' + file + ' : 开始处理...'
        print(message, end='')
        # here file should be a 
        # tuple (file_name, abs_path_with_file_name)
        main(file)
        print('完成')
