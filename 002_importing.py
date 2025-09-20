# add.add means [module/file].[function]
import add
print("\nadd.add: 2 + 3 =", add.add(2, 3))

# alternatively you can use "from add import add"
from add import add
print("\nadd: 2 + 3 =", add(2, 3))

# OR YOU CAN RENAME IT like this :
# from add import add as plus
# print(plus(2, 3))

# YOU CAN ALSO ADD STRING (concatenate)
from add import add as plus
print("\nstring:")
print(plus("lan", "ce"))

#YOU CAN ALSO ADD LISTS!!!
from add import add as plus
print("\nlist:")
print(plus([1, 2], [3, 4]))