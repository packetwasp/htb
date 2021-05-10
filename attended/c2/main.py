from threading import *
from terminal import *
import listener

cmd = ''

if __name__ == '__main__':
    # Terinal stuff
    terminal = Terminal()
    terminal_thread = Thread(target = terminal.cmdloop,)
    terminal_thread.start()
    # Web stuff
    print("Starting webserver") 
    listener.run()
