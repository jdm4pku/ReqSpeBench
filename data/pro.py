import os
import shutil


def copy_feature_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    index = 1
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.sdl'):
                source_file_path = os.path.join(root, file)
                folder_name = "{:02}".format(index)
                target_folder = os.path.join(target_dir, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                target_file_path = os.path.join(target_folder, file)
                shutil.copy2(source_file_path, target_file_path)
                index += 1


if __name__ == "__main__":
    source_directory = r'./data'  # 请替换为实际源文件夹路径
    target_directory = r'./SDL'  # 请替换为实际目标文件夹路径
    copy_feature_files(source_directory, target_directory)