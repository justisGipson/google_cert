#!/usr/bin/env python

import subprocess
import multiprocessing
from multiprocessing import Pool
import os

home = os.path.expanduser('~')
src = home + "/data/prod/"
dest = home + "/data/prod_backup/"

if __name__ == "__main__":
    pool = Pool(multiprocessing.cpu_count())
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest], ))
