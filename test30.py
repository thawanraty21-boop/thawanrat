#2. have parameter no return

'''
def func_name(param1,param2,...):
    คำสั่ง
    คำสั่ง
    ........
'''
def showHi(your_name) :
    print('----------------')
    print(f'สวัสดี{your_name}')
    print('-----------------')
    
def showNumber(n1, n2) :
    print('----------------')
    print(f'ผลบวกของ {n1} และ {n2} เท่ากับ {n1+n2}')
    print('-----------------')
    
showHi('สมชาย') # ข้อมูลส่งให้ parameter เรียก argument
showHi('สมศรี')
showNumber(10,20)
showHi('sombat')