#!/bin/bash

if ! pgrep -f py-smtp.py &> /dev/null 2>&1; then
  nohup python3 /root/py-smtp.py &
  
fi
