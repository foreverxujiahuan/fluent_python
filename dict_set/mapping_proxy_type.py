from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
d_proxy[2] = 'B'
print(d_proxy)
