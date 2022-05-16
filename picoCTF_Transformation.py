ec_s = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'

for i in range(len(ec_s)):
 print(chr(ord(ec_s[i])>>8))
 var = chr((ord(ec_s[i]))-((ord(ec_s[i])>>8)<<8))
 print(var)
