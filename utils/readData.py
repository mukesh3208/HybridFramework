from utils.readingData import XLSReader


def getData():
    xls = XLSReader("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\runner.xlsx")
    xls.readXLS.sheet_by_name()