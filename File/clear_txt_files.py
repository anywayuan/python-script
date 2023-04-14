# 清空某个文件夹下所有.txt文件的所有内容

import os


def clear_txt_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'w') as file:
                        file.write('')
                    print(f"成功清空: {file_path}")
                except Exception as e:
                    print(f"清空失败: {file_path}")
                    print(e)


if __name__ == "__main__":
    # 替换为您桌面上的“plugins”文件夹的路径
    plugins_folder_path = os.path.expanduser("/Users/chenlian/Downloads")
    clear_txt_files(plugins_folder_path)
