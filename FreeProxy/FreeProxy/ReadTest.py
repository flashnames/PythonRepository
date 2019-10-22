import csv
def Read():
    with open('C:\\Users\\admin\\Desktop\\PythonCode\\FreeProxy\\FreeProxy\\Data.csv')  as  f:
        reader=csv.reader(f)
        for i in reader:
            print(i)

Read()