import sys
import os
import venv
import subprocess
import tempfile
import shutil


current_dir = tempfile.mkdtemp()
venv.create(current_dir, with_pip=True)
subprocess.run([os.path.join(current_dir, 'bin', 'pip'), 'install', 'pyfiglet'])
subprocess.run([os.path.join(current_dir, 'bin', 'python3'), '-m', 'figdate', *sys.argv[1:]])
shutil.rmtree(current_dir)