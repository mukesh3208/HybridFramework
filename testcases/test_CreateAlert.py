import pytest

from DriverScript.driverScript import driverScript
from conftest import Dlist, Glist
from testResources import constants
from utils import readData
d= driverScript()
@pytest.mark.usefixtures("base_fixture")
class Test_Login:

    testCaseName="CreateAlert"

    @pytest.mark.parametrize("argVals", readData.getData(testCaseName, constants.XLS_PATH))
    def test_Login(self, argVals):
        dataRunMode = argVals[constants.RUNMODE]
        testrunMode = readData.isRunnable(self.testCaseName, constants.XLS_PATH)
        if(testrunMode):
            if(dataRunMode==constants.RUNMODEYES):
                #calling driverscript
                for i in range(0, len(Dlist)):
                    pass
                for j in range(0, len(Glist)):
                    pass
                Dlist[i].execute(Glist[j], self.testCaseName,constants.XLS_PATH, argVals)
            else:
                pytest.skip("Skipping the test case as RunMode is No on data sheet")
        else:
            pytest.skip("Skipping the test case reason Runmode is No")




