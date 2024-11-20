'''ЗАДАЧА № 3'''


names_files_list = ['file_1.txt', 'file_2.txt', 'file_3.txt']
files_dict = {}
count_dict = {}
new_list = []

for name in names_files_list:
    files_dict[name] = open(name, 'r', encoding='utf-8').read()
    count_dict[name] = files_dict[name].count('\n') +1

for name in count_dict:
    new_list.append((count_dict[name], name))

sort_list = sorted(new_list)

file = open('united_file.txt', 'w', encoding='utf-8')

for count, name in sort_list:
    file.write(name + '\n')
    file.write(str(count) + '\n')
    file.write(files_dict[name] + '\n')









