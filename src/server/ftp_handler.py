from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
#from pyftpdlib.servers import DummyAuthorizer

import shutil
import os


class MyHandler(FTPHandler):

    def on_connect(self):
        print "%s:%s connected" % (self.remote_ip, self.remote_port)
        
    def on_login(self, username):
        monitored_files = open('files', 'r')
        
        for line in monitored_files:
            abspath = line.strip("\n")
            tmp = abspath.split("/")
            afile = tmp[len(tmp) - 1] 
            shutil.copyfile(abspath, "./" + afile)
        monitored_files.close()

    def on_logout(self, username):
        # do something when client disconnects
        monitored_files = open('files', 'r')

        for line in monitored_files:
            abspath = line.strip("\n")
            tmp = abspath.split("/")
            afile = tmp[len(tmp) - 1]
            os.remove(afile)
        monitored_files.close()

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)
