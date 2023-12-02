filenames = ["1.Raw data.txt", "2.reports.txt", "3.presentations.txt"]

for file in filenames:

    file = file.replace(".","-",1)
    print(file)


print(filenames)