import os

while True:
    command = input("Komandani kiriting (ls, touch, mkdir, cd, \\q): ")

    if command == "ls":
        files = os.listdir()
        print("Fayllar: ", files)

    elif command == "touch":
        file_name = input("Fayl nomini kiriting: ")
        file_content = input(f"{file_name} fayliga yoziladigan malumotni kiriting: ")

        with open(file_name, 'w') as file:
            file.write(file_content)

        print(f"{file_name} yaratildi va unga malumot yozildi.")

    elif command == "mkdir":
        folder_name = input("Papka nomini kiriting: ")
        os.mkdir(folder_name)
        print(f"{folder_name} papkasi yaratildi.")

    elif command == "cd":
        destination = input("Ochish kerak bo'lgan papka nomini kiriting: ")
        if destination == "..":
            os.chdir(os.path.dirname(os.getcwd()))
        else:
            os.chdir(destination)
        print(f"{destination} papkasiga o'tildi.")

    elif command == "\\q":
        print("Dastur to'xtatildi.")
        break

    else:
        print("Noto'g'ri komanda! Qaytadan kiriting.")
