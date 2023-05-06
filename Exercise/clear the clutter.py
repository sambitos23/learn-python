import os

files = os.listdir("clutter floder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutter floder/{file}", f"clutter floder/{i}.png")
        i += 1
