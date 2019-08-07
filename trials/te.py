from gps1 import coordinates
import csv


try:
    la,ln=coordinates()
    print((la,ln))
    def write_csv1():
        la,ln=coordinates()
        row1 = [la,ln]
        with open('Data.csv', mode='a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(row1)
            file.close()
    write_csv1()
except:
    pass
