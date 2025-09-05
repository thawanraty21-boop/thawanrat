#1.function: no parameter no return
# parameter คือ ตัวแปรประเภทนึ่ง ที่ใช้ได้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น
# return  คือ คำสั่งที่บงบอกถึงการจบการทำงานของฟังก์ชั่นนั้นๆ และส่งค่าทีี่อยู่หลัง return กลับไปที่จุดเรียกใช้ฟังก์ชั่น(ถ้ามี)

'''
def func_name() :
    คำสั่ง
    คำสั่ง
    ......
'''
print( 'wow...')

def showHi():
    print('Hi...')
    
print('woo...')

def showHey():
    print('Hey...')
    
print('Wee...')

showHi()
showHi()
showHey()
showHey()