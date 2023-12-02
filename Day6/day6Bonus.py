contents = ["Learn Python and some hacking staff from Cisco",
            "Write report about how to enumerate user account",
            "Present what did you find during the test to the customer"]

filenames = ["python.txt","enumerate.txt","report.txt"]

# for i in range(len(contents)):
#     file = open(f"../files/{filenames[i]}","w")
#     file.writelines(contents[i])
#     file.close()

for filename,content in zip(filenames,contents):
    file = open(f"../files/{filename}","w")
    file.write(content)
    file.close()


