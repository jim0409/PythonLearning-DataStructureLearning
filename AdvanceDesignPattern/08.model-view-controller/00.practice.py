grades = ('a', 'b', 'c')

class GradeModel:
    def get_grade(self, n):
        try:
            value = grades[n]
        except IndexError as err:
            print("Error happened in GradeModel: {}".format(err))
            value = "Not found"

        return value

class GradeTerminalView:
    def show(self, grade):
        print('the grade is {}:'.format(grade))

    def error(self, msg):
        print("Error: {}".format(msg))
    
    def select_grade(self):
        return input("Which grade would you like to choose?  ")

class GradeTerminalController:
    def __init__(self):
        # 先建立兩種類別，分別為Model與TerminalView，方便下面控制Model對應View的關係
        self.model = GradeModel()
        self.view = GradeTerminalView()
    
    def run(self):
        valid_input = False
        while not valid_input:
            try:
                # 如果是False則宣告為View
                n = self.view.select_grade()
                n = int(n)
                # 設定valid_input為True，跳出Controller的while迴圈
                valid_input = True
            # 如果有錯誤，回報錯誤訊息。
            except ValueError as err:
                # 因為這邊沒有設定valid_input為True，所以程式會繼續執行Controller的while迴圈
                self.view.error("Error happened in GradeTerminalController: {}".format(n, err))
        
        # 跳出while迴圈的同時，會拿到要查詢grade的值n
        grade = self.model.get_grade(n)
        self.view.show(grade)

def main():
    controller = GradeTerminalController()
    while True:
        controller.run()

if __name__ == "__main__":
    main()