import openpyxl

from utils.readingData import XLSReader


def readD():
    print("In readD function")
    # flag = False
    # while not (flag):
    #     print("A")

    xls = XLSReader("/testResources/runner.xlsx")
    testcasename = "TestB"
    wb_obj = openpyxl.load_workbook("/testResources/runner.xlsx")
    sheet = wb_obj["TestCase"]

    runMode = xls.getCellDataByColName("TestCase", 3, "RunMode")
    print(runMode)
readD()