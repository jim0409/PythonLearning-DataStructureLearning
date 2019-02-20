# 枚舉法- enumerate
# 官方說明
Abstract
This PEP proposes adding an enumeration type to the Python standard library.

An enumeration is a set of symbolic names bound to unique, constant values. Within an enumeration, the values can be compared by identity, and the enumeration itself can be iterated over.

# 使用情境：
1. 利用列舉型別來增進程式的可讀性; if ChosenColor=1 <=> if ChosenColor=COLOR_RED
2. 使用列舉型別增進可靠度; 避免處處修改同樣的值 COLOR_RED
3. 利用列舉型別使程式容易修改; 可以從COLOR_RED=value的定義來修改value <=> 修改一處即可同步更新所以位置的值
4. 利用列舉型別取代布林變數; 增加判斷型別，而非呆板的True/False or 0/1 <=> 定義Info/Warnning/Error


# 參考：
1. https://www.python.org/dev/peps/pep-0435/#id13
2. https://docs.python.org/3/library/enum.html
3. https://ithelp.ithome.com.tw/articles/10029111
4. https://bit.ly/2SMBFSI