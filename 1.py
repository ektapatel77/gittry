zxczxcczczcczcimport os
import subprocess

for top, dirs, files in os.walk('/home/pdf'):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('lowriter --invisible --convert-to doc "{}"'
                            .format(abspath), shell=True)
