import os

# 指定你的图片文件夹
directory = '/Users/chenlian/Downloads/pic'

# 使用os模块的listdir函数获取文件夹中的文件名列表
filenames = os.listdir(directory)

# 对每个文件名进行处理
for i, filename in enumerate(filenames):
    # 为每个文件生成新的文件名
    new_name = "step_" + str(i+1) + os.path.splitext(filename)[1]

    # 使用os模块的rename函数修改文件名
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
