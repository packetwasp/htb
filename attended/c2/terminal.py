from cmd import Cmd

import main

class Terminal (Cmd):
    prompt = '$ > '

    def default(self, args):
        main.cmd = args

