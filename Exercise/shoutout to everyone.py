from os import system

text_list = ["Hello Sambit", "Good Morning", "How are you", "I think everything will be great"]

for text in text_list:
    print(text)
    system(f"espeak '{text}'")
