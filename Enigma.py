from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

# 通过密码派生一个或多个密钥
password = b'my super secret'
salt = get_random_bytes(16)
key = scrypt(password, salt, 32, N=2**14, r=8, p=1)
print(key)

