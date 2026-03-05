class light():
    def __init__(self, stat):
        self.stat = stat

    def toggle(self):
        if self.stat == "on":
            self.stat = "off"
        else: self.stat = "on"
    
    def show(self):
        print(self.stat)
l1 = light("on")
l1.toggle()
l1.toggle()
l1.show()