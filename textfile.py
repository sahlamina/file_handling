class TextFileHandling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # going to read in two ways and write in two ways
    def readTextFile(self):
    # we will open file
    # read file
    # close the file


        file = open(self.file_path, 'r')
        # self.text_storage = file.read()
        # file.close()
        # file = open(self.file_path, 'r')
        # self.text_storage = file.read(3) # this reads 3 characters in the text file
        self.text_storage = file.readline()
        self.text_storage = file.readline()
        print(file.tell()) # will start reading from the insertion point of the pointer
        file.seek(3) # takes two args and starts from 0th position (beginning) telling the pointer to go back
        self.text_storage = file.readline() #
        file.close()
        return self.text_storage

    def writeTextFile(self):
        file = open(" writer.txt", "w") # w+ means write and read
        file.write("My first python created file")
        file.close()
        file = open(" writer.txt", "a+") # a is the append mode, a+ means append and read
        file.write("\nI am overriding the file")
        self.text_storage = file.read()
        file.seek(5) # this tells the interpreter where to find the seek, starting from 0
        self.text_storage = file.read() # storing what i read from the file to the instance variable
        file.close()
        print(file.closed) # give me the status of the closure
        print(file.name) # give me the name of the current file
        print(file.mode) # give m
        return self.text_storage

    def readTextFileUsingWith(self):
        # To reduce the overhead of closing files, we use with
        # Open the file and just read it. No overhead of closing
        # Automatically closes the file and also closed it durign the times of exception being raised
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    def writeTextFileUsingWith(self):

        with open("writer.txt", "w+") as file:
            file.write("Will it work????")
            print(file.tell())
            file.seek(0)
            self.text_storage = file.read()
            return self.text_storage

    def playingWithPythonOSModule(self):
        import os
        print(os.getcwd()) # current working directory
        # os.remove("writer.txt") # .remove deletes the named file
        print(os.listdir())
        os.rename('order.txt', 'modified.txt') # .rename renames the named directory
        os.chdir("/Users/saheedlamina/PycharmProjects/file_handling") # change directory
        os.mkdir("Agbo") # make directory
        os.rmdir("Agbo") # remove directory

    def playingWithException(self):
        try:
            file = open(self.file_path, 'r')
            a = 10
            b = 0
            c = a / b
        except Exception as e:
            print(e)
            print("File is not present")
        else:
            print("I am in the else clause!")
            self.text_storage = file.redline()
            file.close()
        finally:
            print("Will run for sure!!!")
            return self.text_storage


    def raiseException(self):
        try:
            firstValue = (input("Enter your name "))

                if (len(firstValue)) == 0:
                    raise Exception # you are throwing an exception which python might not have # used to let the customer know what we want them to know

        except Exception:
            print("We do not accept empty names!!")

        else:
            print("thank you for entering your name::", first)


















