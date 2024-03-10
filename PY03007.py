# XỬ LÝ VĂN BẢN

import sys
s = sys.stdin.read().lower()
# s = re.sub(r'[\.\?\!]+','\n',s)
res = ' '.join(s.split())
# res = res.replace('.','\n').replace('?','\n').replace('!','\n')
print(res)
