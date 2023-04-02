import os
folders = os.listdir("data")

print(folders)

print("=====================================")
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
        