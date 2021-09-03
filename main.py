from csv import DictReader
import os

if os.stat("test.csv").st_size == 0:
    print("Input csv file is empty")

else:

    file_handle = open("./test.csv", "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    data_list = []

    for row in csv_reader:
        data_list.append(row)

    print(data_list)
    file_handle.close()
