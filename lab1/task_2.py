import re

f = open('logs.txt', 'r')

s = []
ips = []
date_time = []
capital_words = []
for i in f:
    ips += re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}", i)
    date_time += re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", i)
    capital_words += re.findall("[A-Z]+", i)
    s.append(i)
s = ''.join(s)
f.close()

f = open('logs.txt', 'w')
print(ips)
print(date_time)
print(capital_words)
f.write(re.sub("[\w.-]+@[\w.-]+\.\w+", "[EMAIL_PROTECTED]", s))
f.close()