import random as r
class Door:
    def __init__(self):
        self.a = r.choice(['car','sheep'])
        if self.a == 'car':
            self.b = 'sheep'
            self.c = 'sheep'
        else:
            self.b = r.choice(['car','sheep'])
            if self.b == 'car':
                self.c = 'sheep'
            else:
                self.c = 'car'
        self.selected = [self.a,self.b,self.c]
    def stay_select(self):
        select = r.choice(self.selected)
        if select == 'car':
            return True
    def switch_select(self):
        select = r.choice(self.selected)
        temp = self.selected[:]
        temp.remove(select)
        if temp[0] == 'sheep':
            if temp[1] == 'car':
                return True
        if temp[1] == 'sheep':
            if temp[0] == 'car':
                return True
door = Door()
count2 = 0
for i in range(10000):
    if door.switch_select() == True:
        count2 += 1
print('total:10000')
print('switch: %d' % count2)
print('switch win: %s' % str(count2/100)+'%')
count1 = 0
for i in range(10000):
    if door.stay_select() == True:
        count1 += 1
print('total:10000')
print('stay: %d' % count1)
print('stay win: %s' % str(count1/100)+'%')
                          
            
