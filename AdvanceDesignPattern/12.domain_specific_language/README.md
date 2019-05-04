# 解釋器模式
對於有固定pattern的字串，但是字串解釋會依據選擇種類不同而得到不同含義的時候使用。

# 角色介紹
解譯器模式簡單說就是`把一句有特殊規則的語句，透過解釋器，將它真正的意思表現出來`。
Context：等待解讀的語句
- AbstractExpression：只所有規則都要實作的介面
- TerminalExpression：只無法再展開的規則，也是最小的單位
- NonterminalExpression：可以再展開的規則，可以展開成NonterminalExpression和TerminalExpression的組合

優點，解釋器模式會針對每個語法規則都設計相對應的類別，供改變或擴充。
缺點，當語法規則的種類變多時，宣告的類別也會變多。

# refer
http://corrupt003-design-pattern.blogspot.com/2017/01/interpreter-pattern.html
https://xyz.cinc.biz/2013/08/interpreter-pattern.html
https://en.wikipedia.org/wiki/Interpreter_pattern
https://en.wikipedia.org/wiki/Composite_pattern

# extend
1. Context-free grammar(CFG)
2. Backus-Naur form(BNF)
3. Compiler