import sys

from conftest import envProp
from keywords.genKeyword import genKeywords


def demo():
    # obj = genKeywords
    # x = "openBrowser"
    # y=getattr(sys.modules[__name__],'genKeywords')
    #
    # print(y)
    # z = getattr(y,x)
    # print(z)
    # getattr(y,x)(obj)

    obj = envProp[locator]

demo()