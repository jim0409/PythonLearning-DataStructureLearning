# 狀態設計模式
使用state_machine來操作狀態
1. 宣告各個state=State()，其中最初始的state需要加上initial=True
2. 定義每個State可以轉移的狀態，用event = Event(from_states=(I_1s, I_2s, ...), to_state=Fs)，注意`from_states`及`to_state`不能打錯字，因為Event是用get去抓的...
3. 依據之前定義過的Event，額外用裝飾法定義before以及after來確保轉換state時，可以用先後執行這些方法


# refer
https://www.pyfdtic.com/2018/03/27/python-state-machine
https://stackoverflow.com/questions/47541749/state-machine-and-toggling-states-in-a-loop
https://www.zeolearn.com/magazine/writing-maintainable-code-using-sate-machines-in-python
