import os
import shutil
import numpy as np
import time


StartingPoints = [8000]

tempdir = '/cs/labs/yweiss/aharonchiko/daniel/scripts-DTSR/'
if (os.path.isdir(tempdir)):
    shutil.rmtree(tempdir)
os.mkdir(tempdir)

for s in StartingPoints:
    with open (tempdir + str(s) + '.sh', 'w') as rsh:
        rsh.write('''#!/bin/bash
#SBATCH --mem=32g
#SBATCH -c2
#SBATCH --time=1-0
#SBATCH --gres=gpu:1

module load torch
python3 -u /cs/labs/yweiss/aharonchiko/daniel/DeepTemporalSR/main.py'''
                  )
    time.sleep(5)
    os.system('sbatch ' + tempdir + str(s) + '.sh')
