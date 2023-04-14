# 删除某个文件夹下所有的.zip文件

import os


def delete_zip_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"成功删除: {file_path}")
                except Exception as e:
                    print(f"删除失败: {file_path}")
                    print(e)


if __name__ == "__main__":
    # 替换为您桌面上的“plugins”文件夹的路径
    plugins_folder_path = os.path.expanduser("/Users/chenlian/Downloads")
    delete_zip_files(plugins_folder_path)
