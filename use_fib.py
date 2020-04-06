from fib_basic import fib_gen
import sys
all_num=fib_gen()
print("all_num size: ",sys.getsizeof(all_num))
for num in all_num:
     print(num**2)
