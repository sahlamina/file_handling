image_path = 'jordanfly.jpg'
# 1.
# Accept from the user some text.Ensure user enters something else raise an
# exception.
# After that# write#that# text# to# a file and then read
# from this file to write# to another file simultaneously
# 2.
# Reading an image to writing to another file simultaneously


class FileHandlingHomework:
    def __init__(self, text_store=None):
        self.text_store = text_store
        pass

    def user_input(self):
        try:
            name = (input("Enter your name: "))
            if len(name) == 0:
                raise Exception
        except Exception:
            print("Please enter at least one letter as your name ")
            self.user_input()
        else:
            print(f"Thank you,your name has been accepted {name}")



    def taketext(self):
        try:
            user = (input("Please enter some text "))
            if len(user) == 0:
                raise Exception
        except Exception:
            print("We asked for some text... ")
            self.taketext()
        else:
            with open("hworkfile.txt", "w+") as file:
                file.write(user)
                file.seek(0)
                self.text_store = file.read()
            with open("workfileii.txt", "w") as file:
                file.write(self.text_store)
            return self.text_store


    def imageread(self):
        with open(image_path, 'rb') as image_file:
            image_string = image_file.read()
            with open("file location.png", 'wb') as dest_image:
                dest_image.write(image_string)








