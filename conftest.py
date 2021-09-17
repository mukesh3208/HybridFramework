import time

import pytest
from pyjavaproperties import Properties

from DriverScript.driverScript import driverScript
from keywords.genKeyword import genKeywords

prod=Properties()
envProp=Properties()

Dlist=[]
Glist=[]

@pytest.fixture(scope="function", autouse=True)
def base_fixture():
    try:
        prodPath=open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\production.properties")
        prod.load(prodPath)

        envPath = open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\environment.properties")
        envProp.load(envPath)
        d = driverScript()
        Dlist.append(d)
        gen = genKeywords()
        Glist.append(gen)
    except FileNotFoundError as f:
        print(f)
    yield locals()
    time.sleep(10)
    gen.closeApp()