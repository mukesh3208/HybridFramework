import sys

import conftest
from keywords.genKeyword import genKeywords
from testResources import constants
from utils.readingData import XLSReader


class driverScript:

    def execute(self,key, testCaseName, xlsPath, testData):

        self.testcaseName=testCaseName
        xls = XLSReader(xlsPath)
        rows = xls.rowCount(constants.KEYWORDSHEET)
        testdata = testData

        for rNum in range(1, rows):
            tName = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.TCID)

            if(tName==self.testcaseName):
                keywordKey = xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.KEYWORD)
                objectKey=xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.OBJECT)
                dataKey=xls.getCellDataByColName(constants.KEYWORDSHEET, rNum, constants.DATA)
                #print(str(keywordKey)+" - "+str(objectKey)+" - "+str(dataKey))
                key.set_ObjectKey(objectKey)
                key.set_dataKey(dataKey)
                key.set_testData(testdata)

                y = getattr(sys.modules[__name__], 'genKeywords')
                getattr(y, keywordKey)(key)



