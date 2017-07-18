import sys
from os.path import join, dirname, abspath
root_dir = abspath(join(dirname(dirname(dirname(__file__)))))
sys.path.append(root_dir)
