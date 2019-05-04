# 責任鍊是透過event來開頭，然後旅途中產生物件的一種設計模式
# 事件進入 -> 產生第一個物件 -> 物件跑生成物件流程 -> 依照生成物件流程邏輯產生對應的物件 -> 顯示結果


# 宣告一個Event的class，如此一來所有的責任練生成物件都會透過物件來決定要執行什麼動作
class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# 定義流程上的第一個物件
class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    # 定義一個handler，透過寫入event來決定要使用哪一個handle函數
    def handle(self, event):
        handler = "handle_{}".format(event)

        # hasattr(物件，某個方法__str__)
        # 如果物件具有該方法，則定義method為該方法，且執行該方法
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)

        elif self.parent:
            print("-------execute the method with parent object: {}".format(self.parent.__str__))
            self.parent.handle(event)

        # 如果沒有辦法找到可以執行的方法，回傳default的執行方法
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


# 定義流程上的第二個物件(備註，此處二/三/四並沒有實質的意義)
class MainWindow(Widget):
    def handle_close(self, event):
        print("MainWindow: {}".format(event))

    def handle_default(self, event):
        print("! ==\t\t MainWindow can't find {}.{}. Execute Default method.".format(type(event), event))


# 定義流程上的第三個物件(備註，此處二/三/四並沒有實質的意義)
class SendDialog(Widget):
    def handle_paint(self, event):
        print("SendDialog: {}".format(event))


# 定義流程上的第四個物件(備註，此處二/三/四並沒有實質的意義)
class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    # mw 是sd的parent
    sd = SendDialog(mw)
    # mw, sd 是msg的parent
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print("\nthe input event: {}\n---".format(evt))
        print('Sending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)


if __name__ == '__main__':
    main()
