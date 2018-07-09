# 文件过滤，将两个目录中重复的文件找出，并删除指定目录中重复文件
# 与本案无关，仅用于本人处理电脑上的重复书籍文件之用


import os

# 遍历目录一，包含其所有子目录下的文件
dir1 = r'F:\书籍\____'

lst = []
for parent, dir_names, file_names in os.walk(dir1):
    # print(1, type(parent), 2, type(dir_names), 3, type(file_names))
    for file_name in file_names:
        if file_name.endswith('.pdf'):
            lst.append(file_name)
            # print(file_name)

# for f in os.listdir(dir1):
#     print(type(f), f)

# 遍历目录二，该目录只有一级，下面直接是pdf文件
dir2 = r'F:\书籍\待整书籍'

for file_name in os.listdir(dir2):
    if lst.__contains__(file_name):
        print(file_name)
        # 这些书籍是重复的，将其重重命名(前面加____前缀，后期手动删除)
        os.rename(r'/'.join([dir2, file_name]), r'/'.join([dir2, '____' + file_name]))
