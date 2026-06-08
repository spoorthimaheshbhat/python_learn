# given list:

files = [
    "report.pdf",
    "notes.txt",
    "logs.txt",
    "data.csv",
    "june.txt",
    "pogo.text",
    "image.png"
]

def return_txt_files(file_list):
    return [file for file in file_list if file.endswith(".txt")]

txt_files = return_txt_files(files)
if txt_files:
    print(txt_files)
else:
    print("No .txt files found")


