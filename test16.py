from datetime import datetime

print('------------------------')
print('    โปรแกรมตรวจสอบวัยวุฒิ')
print('------------------------')
your_name = input('ป้อนชื่อ: ')
your_yearborn = int( input('ป้อนปีเกิด (พ.ศ.): '))
print('----------------------')

your_age = (datetime.now().year + 543) - your_yearborn

if your_age >= 35 :
   print(f'คุณ {your_name} อายุ {your_age} แก่แล้วนะ อย่าคิดมาก...')
else :
   print(f'คุณ {your_name} อายุ {your_age} ยังไม่แก่...')
   
print('-------------------------------')