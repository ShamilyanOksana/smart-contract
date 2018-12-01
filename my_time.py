import time
import datetime

now = time.time()
deadline = now + 86400

delta = deadline - now
stuct = time.ctime(int(deadline))
print(stuct)