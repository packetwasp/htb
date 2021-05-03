import sys
from base64 import b64decode
import des
#private static byte[] _rgbKey = Encoding.ASCII.GetBytes("7ly6UznJ");
#private static byte[] _rgbIV = Encoding.ASCII.GetBytes("XuVUm5fR");

passwd = b64decode(sys.argv[1])

c = des.DesKey(b'7ly6UznJ')
iv = b'XuVUm5fR'
print(c.decrypt(passwd, initial=iv, padding=True))

