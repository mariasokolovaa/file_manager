#!/usr/bin/python3
import os
import shutil

with open("settings.txt", "r") as settings:
    dir = settings.read()
    start_dir = os.path.dirname(os.path.dirname(dir))
# Функция для создания папки
def create_folder(folder_name):
    try:
        os.mkdir((os.path.join(dir, folder_name)))
        print(f"Folder {folder_name} created successfully.")
    except FileExistsError:
        print('File already exists')
   
# Функция для удаления папки
def delete_folder(folder_name):
    try:
        shutil.rmtree(os.path.join(dir, folder_name))
        print(f"Folder {folder_name} deleted successfully.")
    except FileNotFoundError:
        print(f"Folder {folder_name} does not exist.")

# Функция для перемещения между папками
def change_directory(folder_name):
    global dir
    new_path = os.path.join(dir, folder_name)
    if os.path.isdir(new_path):
        dir = new_path
        print(f"Moved to folder {folder_name}.")
        print(os.path.dirname(dir))
    else:
        print("Directory does not exist.")

# Функция для перемещения на уровень вверх
def move_up():
    global dir
    parent_dir = os.path.dirname(dir)
    print(parent_dir)
    if parent_dir!=start_dir :
        dir = parent_dir
        print(f"Moved up to {os.path.basename(dir)}.")
    else:
        print("Already at the root directory.")

# Функция для создания пустого файла
def create_file(file_name):
    try:
        with open(os.path.join(dir, file_name), "w"):
            pass
        print(f"File {file_name} created successfully.")
    except FileExistsError:
        print(f"File {file_name} already exists.")

# Функция для записи текста в файл
def write_to_file(file_name, text):
    try:
        with open(os.path.join(dir, file_name), "w") as file:
            file.write(text)
        print(f"Text was added to {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

# Функция для просмотра содержимого файла
def view_file(file_name):
    try:
        with open(os.path.join(dir, file_name), "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File {file_name} not found.")

# Функция для удаления файла
def delete_file(file_name):
    try:
        os.remove(os.path.join(dir, file_name))
        print(f"File {file_name} was deleted.")
    except FileNotFoundError:
        print(f"File {file_name} was not found.")

# Функция для копирования файла
def copy_file(file_name, new_dir):
    try:
        shutil.copy2(os.path.join(dir, file_name), os.path.join(dir, new_dir))
        print(f"File {file_name} copied to {new_dir}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")

# Функция для перемещения файла
def move_file(file_name, new_dir):
    try:
        shutil.move(os.path.join(dir, file_name), os.path.join(dir, new_dir))
        print(f"File {file_name} was moved to {new_dir}.")
    except FileNotFoundError:
        print(f"File {file_name} wasn't found.")

# Функция для переименования файла
def rename_file(current_file, new_file):
    try:
        os.rename(os.path.join(dir, current_file), os.path.join(dir, new_file))
        print(f"File {current_file} renamed to {new_file}.")
    except FileNotFoundError:
        print(f"File {current_file} not found.")

# Основной цикл программы
print("Current Directory:", dir)
print("File Manager Menu:")
print("1. Create Folder")
print("2. Delete Folder")
print("3. Change Directory")
print("4. Move Up")
print("5. Create File")
print("6. Write to File")
print("7. Read File")
print("8. Delete File")
print("9. Copy File")
print("10. Move File")
print("11. Rename File")
print("12. Exit")
while True:


    choice = input("Enter your choice: ")
    if choice == "1":
        folder_name = input("Enter folder name: ")
        create_folder(folder_name)
    elif choice == "2":
        folder_name = input("Enter folder name: ")
        delete_folder(folder_name)
    elif choice == "3":
        folder_name = input("Enter folder name: ")
        change_directory(folder_name)
    elif choice == "4":
        move_up()
    elif choice == "5":
        file_name = input("Enter file name: ")
        create_file(file_name)
    elif choice == "6":
        file_name = input("Enter file name: ")
        text = input("Enter text: ")
        write_to_file(file_name, text)
    elif choice == "7":
        file_name = input("Enter filename: ")
        view_file(file_name)
    elif choice == "8":
        file_name = input("Enter filename: ")
        delete_file(file_name)
    elif choice == "9":
        file1 = input("Enter source filename: ")
        file2 = input("Enter destination filename: ")
        copy_file(file1, file2)
    elif choice == "10":
        file1 = input("Enter filename: ")
        file2 = input("Enter folder name: ")
        move_file(file1, file2)
    elif choice == "11":
        current_file = input("Enter current filename: ")
        new_file = input("Enter new filename: ")
        rename_file(current_file, new_file)
    elif choice == "12":
        print("Exiting File Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
    
    input("Press Enter to continue...")
