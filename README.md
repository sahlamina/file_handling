# This lesson is on learning how to open, read and close files

### We used class attributes to open, read and close
-  we created a .txt file which was the one we read using our class
- we learned new methods to read:
````python
 file = open(self.file_path, 'r')
 self.text_storage = file.read()
        file.close()
````   
- there was also a way to choose the first 3 characters by putting the number of characters in the file.read(3) command
- the numbers in . seek are the offset and the from
- .tell is telling me my current position
- .readline is reading a line so when you have multiple lines, it does one after the other
- .readlines reads the rest of the lines from teh current position

## Writer
- the writer class helps open new write files
```python
    def writeTextFile(self):
        file = open(" writer.txt", "w")
        file.write("My first python created file")
        file.close()
```
- this creates a new file called writer.txt with "my first python created file" on it

### Exceptions 
- throw up errors during the run time
- we deal with try, except, else and finally with exceptions
##### Try
- Put the code you think will raise an exception
##### Except
- catches the thrown exception
- never write a general exception before the specific exception. It becomes completely unreachable in that case
#### else 
 -if exception is not thrown then the programme can run the following code
#### finally
- whether an exception is raised or not, the code in this part will for sure run.
- usually ued for closing drivers or database connections

#### Debugger
- you can use shift f9
- alternately, you can double tap shift and find debug mode
