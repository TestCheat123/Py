class BigBell:

    def __init__(self):
        self.switch = True

    def sound(self):
        if self.switch:
            self.switch = False
            return print('ding')
        else:
            self.switch = True
            return print('dong')


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
