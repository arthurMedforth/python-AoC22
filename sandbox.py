import numpy as np
list = [0,1,2,3,4,5]
print(list)
ind_to_delete = [0,3]
list_arr = np.array(list)

list_arr = np.delete(list_arr,ind_to_delete)
new_list = list_arr.tolist()
print(new_list)
