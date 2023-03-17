import pandas as pd

class ExcelReader:
    def __init__(self, path, sheet_name='Sheet1'):
        self.path = path
        self.sheet_name = sheet_name

    def read_data(self):
        # Read data from Excel file into a pandas dataframe
        df = pd.read_excel(self.path, sheet_name=self.sheet_name)

        # Access data in the dataframe
        roll_no = df['roll_no'].tolist()
        names = df['name'].tolist()
        phone_number = df['phone_number'].tolist()

        return [roll_no, names, phone_number]
