# lst = [1,2,3,4,'x','y']
# print(lst[2:])
# lst[2:] = []
# print(lst)
# lst.remove(2)
# print(lst)
# lst1 = [1,2,4,5,7]
# print(lst1.pop(3))
# print(lst1)
lst3 = [1,2,3,5]


lst4 = lst3  #浅拷贝
lst3.append(7)
print(lst3)
print(lst4)
print(id(lst3), id(lst4))

import copy
#深度拷贝、
lst5 = copy.deepcopy(lst3)
print(lst5)
print(id(lst5))

