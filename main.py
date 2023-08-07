import os

path_2017 = 'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2017'
path_2018 = 'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2018'
path_2019 = 'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2019'

infile = open("SpreadSheet.csv", 'r')

for line in infile:
    split_line = line.split(",")
    last_name = split_line[0][1:]
    first_name = split_line[1][:-1]
    file_name = last_name+','+first_name
    if os.path.exists(f'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2017\\{file_name}'):
        print("huzzah")
        continue
    if os.path.exists(f'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2018\\{file_name}'):
        print("huzzah")
        continue
    if os.path.exists(f'C:\\Users\\mmarras\\Desktop\\File Project\\Investigation Files 2019\\{file_name}'):
        print("huzzah")
        continue
    if split_line[2].__contains__('2017'):
        print("boo")
        os.chdir(path_2017)
        os.makedirs(file_name)
    if split_line[2].__contains__('2018'):
        print("apple")
        os.chdir(path_2018)
        os.makedirs(file_name)
    if split_line[2].__contains__('2019'):
        print("orange")
        os.chdir(path_2019)
        os.makedirs(file_name)
