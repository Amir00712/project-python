import random
import numpy as np
import time

# ejad list tesadofi
my_list = [random.randint(1, 100) for i in range(1000000)]

# miangin list
start_time = time.time()
list_mean = np.mean(my_list)
end_time = time.time()
print("miangin list", list_mean)
print("zeman sarf shode",end_time - start_time)
