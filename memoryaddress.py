a = [1, 2, 3, 4, 5]
print(id(a))

from ctypes import c_int, addressof, c_wchar_p

a = 44
print(addressof(c_int(a)))

c_wchar_p