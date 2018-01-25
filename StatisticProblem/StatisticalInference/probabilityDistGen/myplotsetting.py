import matplotlib.pyplot as plt


# class mypltsetting():
#     def __init__(self, xl, xf, yl, yf, title):
#         self.__xLabelName = xl
#         self.__xFontsize = xf
#         self.__yLabelName = yl
#         self.__yFontsize = yf
#         self.__titleName = title
#
#     def mypltSetting(xLabelName='', xFontsize=10, yLabelName='', yFontsize=10, titleName='no title'):
#         plt.figure()
#         plt.title(titleName)
#         plt.xlabel(xLabelName, fontsize=xFontsize)
#         plt.ylabel(yLabelName, fontsize=yFontsize)


def mypltSetting(xLabelName='', xFontsize=10, yLabelName='', yFontsize=10, titleName='no title'):
    plt.title(titleName)
    plt.xlabel(xLabelName, fontsize=xFontsize)
    plt.ylabel(yLabelName, fontsize=yFontsize)



