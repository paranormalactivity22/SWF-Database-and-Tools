import time, glob
from binascii import *

# Vars
directory = 'http://yourmice.com/furs/ur_furs.swf'
reference = str()
files = list()
add = list()

def get_files():
    for file in glob.glob('.\Transformice-0\*.class.asasm'):
        files.append(file.replace("\\x", "%"))
    return files

def config_file(file, config):
    config = open(file, config)
    return config

def write_lines(file, text):
    text = '\n'.join(text)
    writer = config_file(file, 'w+')
    writer.write(text)
    writer.close()

def read_lines(file):
    reader = config_file(file, 'r')
    rd = reader.read()
    reader.close()
    return rd.split('\n')

def parse_start():
    fur_archive = 'pushstring          "x_fourrures3.swf"'
    for file in files:
        file_l = read_lines(file)
        i = int()
        while i < len(file_l):
            if file_l[i].startswith('    findproperty'):
                if fur_archive in file_l[i+1]:
                    reference = file_l[i].replace('findproperty', 'getproperty ')
                    get_file_reference(reference)
            i += 1

def get_file_reference(reference):
    getlex = '    getlex'
    for file in files:
        file_l = read_lines(file)
        i = int()
        while i < len(file_l):
            if getlex in file_l[i]:
                if reference in file_l[i+6]:
                    add.extend([file_l[i], file_l[i+8]])
            elif len(add) > 1:
                if file_l[i] == add[1]:
                    file_l[i] += '\n\n'
                    file_l[i] += '%s\n' %(add[0])
                    file_l[i] += '      pushstring          "%s"\n' %(directory)
                    file_l[i] += '%s' %(add[1])
                    write_lines(file, file_l)
                    print('Furs added with successful!')
                    break
            i += 1

if __name__ == "__main__":
    files = get_files()
    parse_start()
    time.sleep(8.0)