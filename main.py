from textfile import TextFileHandling

file_path = "/Users/saheedlamina/PycharmProjects/file_handling/venv/bin/python "

text_file_object = TextFileHandling(file_path)

print(text_file_object.readTextFile())
#
# text_file_object.writeTextFile()
# print(text_file_object.writeTextFile())

# print(text_file_object.readTextFileUsingWith())
# print(text_file_object.writeTextFileUsingWith())

text_file_object.playingWithPythonOSModule()