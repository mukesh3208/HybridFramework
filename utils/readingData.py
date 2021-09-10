import xlrd

class XLSReader:
    def __init__(self, path):
        self.path=path
        self.readXLS = xlrd.open_workbook(path)
    def getCellData(self, sheetname, rowNum, colNum):
        sheet = self.readXLS.sheet_by_name(sheetname).cell_value(rowNum, colNum)
        



