# coding=utf-8
f = open("ww.txt","w")
i = 0
while i<200:
    i+=1
    f.write("hello world!i=%d\n"%i)
    
f.close()

