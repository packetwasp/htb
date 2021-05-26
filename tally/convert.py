cmd = "C:\FTP\Intranet\payloadd.bat"

for i in range(len(cmd), 0 , -4):
    print(cmd[i-4:i].encode().hex())
#    print(cmd[i-4:i])

