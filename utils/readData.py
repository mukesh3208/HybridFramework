from testResources import constants
from utils.readingData import XLSReader


def getData(testCaseName, xlsPath):
    dataList=[]
    xls = XLSReader(xlsPath)
    testStartRowIndex = 1


    while not((xls.getCellData(constants.DATASHEET, testStartRowIndex, 1).value)==testCaseName):
        testStartRowIndex=testStartRowIndex+1

    headerStartRowIndex = testStartRowIndex+1
    dataStartRowIndex = testStartRowIndex+2
    maxRows = 0

    maxRows = xls.totalRows(constants.DATASHEET, testCaseName)
    maxCols = xls.totalCols(constants.DATASHEET, testCaseName)

    for rNum in range(dataStartRowIndex, dataStartRowIndex+maxRows):
        dataDictionary = {}
        for cNum in range(1, maxCols+1):
            dataKey = xls.getCellData(constants.DATASHEET, headerStartRowIndex, cNum).value
            dataValue = xls.getCellData(constants.DATASHEET, rNum, cNum).value
            dataDictionary[dataKey] = dataValue
        dataList.append(dataDictionary)
    return dataList
def isRunnable(testCaseName, xlsPath):
    xls = XLSReader(xlsPath)
    rows = xls.rowCount(constants.TESTCASESHEET)
    for rNum in range(1, rows):
        tName = xls.getCellDataByColName(constants.TESTCASESHEET, rNum, constants.TCID)
        if(tName == testCaseName):
            runMode = xls.getCellDataByColName(constants.TESTCASESHEET, rNum, constants.RUNMODE)
            if(runMode == constants.RUNMODEYES):
                return True
            else:
                return False










