# 枚舉法- enumerate
# 官方說明
Abstract
This PEP proposes adding an enumeration type to the Python standard library.

An enumeration is a set of symbolic names bound to unique, constant values. Within an enumeration, the values can be compared by identity, and the enumeration itself can be iterated over.

# StackOverflow
What's the purpose of enums? What value do they create for the language? When should I use them and when should I avoid them?
The Enum type got into Python via PEP 435. The reasoning given is:

The properties of an enumeration are useful for defining an immutable, related set of constant values that may or may not have a semantic meaning.

When using numbers and strings for this purpose, they could be characterized as "magic numbers" or "magic strings". Numbers rarely carry with them the semantics, and strings are easily confused (capitalization? spelling? snake or camel-case?)


# 使用情境：
1. 利用列舉型別來增進程式的可讀性; if ChosenColor=1 <=> if ChosenColor=COLOR_RED
2. 使用列舉型別增進可靠度; 避免處處修改同樣的值 COLOR_RED
3. 利用列舉型別使程式容易修改; 可以從COLOR_RED=value的定義來修改value <=> 修改一處即可同步更新所以位置的值
4. 利用列舉型別取代布林變數; 增加判斷型別，而非呆板的True/False or 0/1 <=> 定義Info/Warnning/Error


# 參考：
1. https://www.python.org/dev/peps/pep-0435/#id13
2. https://docs.python.org/3/library/enum.html
3. https://stackoverflow.com/questions/37601644/python-whats-the-enum-type-good-for
4. https://ithelp.ithome.com.tw/articles/10029111
5. https://bit.ly/2SMBFSI