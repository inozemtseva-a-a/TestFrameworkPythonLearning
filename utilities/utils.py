import softest
from openpyxl import Workbook, load_workbook
import csv


class Utils(softest.TestCase):
    def assertListItemText(self, lists, value):
        for stop in lists:
            print("The text is: " + stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("test passed")
            else:
                print("test failed")

        self.assert_all()

    def read_data_from_excel(file_name, sheet):
        datalist = []
        wb = load_workbook(filename=file_name)
        sh = wb[sheet]
        row_ct = sh.max_row  # how many rows are in the sheet
        col_ct = sh.max_column  # how many columns are in the sheet

        for i in range(2, row_ct + 1): #start from 2 bec. first row is headers
            row = []
            for j in range(1, col_ct + 1):
                row.append(sh.cell(row=i, column=j).value)
            datalist.append(row)
        return datalist

    def read_data_from_csv(filename):
        #create an empty list
        datalist = []

        #Open CSV file
        csvdata = open(filename,"r")

        #create CSV reader
        reader = csv.reader(csvdata)

        #skip header (1-st row)
        next(reader)

        #Add csv rows to list
        for rows in reader:
            datalist.append(rows)
        return datalist