import time

import pytest
from pyjavaproperties import Properties

from DriverScript.driverScript import driverScript
from keywords.genKeyword import genKeywords

prod=Properties()
envProp=Properties()

Dlist=[]
Glist=[]

@pytest.yield_fixture(scope="session", autouse=True)
def base_fixture():
    try:
        prodPath=open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\production.properties")
        prod.load(prodPath)
        prod.list()
        envPath = open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\environment.properties")
        envProp.load(envPath)
        envProp.list()

        d = driverScript()
        Dlist.append(d)
        gen = genKeywords()
        Glist.append(gen)
    except Exception as e:
        print(e)
    yield locals()
    time.sleep(10)
    gen.closeApp()