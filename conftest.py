from pyjavaproperties import Properties

prod=Properties()
envProp=Properties()
def base_fixture():
    prodPath=open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\production.properties")
    prod.load(prodPath)
    prod.list()
    envPath = open("C:\\Users\\kumarmu\\Documents\\pythonSelenium\\HybridFramework\\environment.properties")
    envProp.load(envPath)
    envProp.list()

base_fixture()

