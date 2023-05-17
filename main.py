#by mohammad mohammad soltani
#-ایجاد حلقه برای تکرار کد
a='true'
while a=='true' :
    #-ایجاد متغیر 
    b=int(input('enter your number:\n'))
    #-چاپ پاسخ
    print(b,'**',b,'=',b**b)
    #-پرسیدن سوال برای ادامه دادن
    c=input('bazam edameh bedam?\ny for yes\nn for no\n')
    #-چک کردن اینکه کاربر میخواهد ادامه بدهیم یا نه
    if c=='n' :
        a='falss'
        print('good bye')
    else :
        a='true'
print('tank you mr.sanei')
