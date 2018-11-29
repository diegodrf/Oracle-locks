import datetime
import os
from time import sleep

username = 'diegodrf'
timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
project = str(os.path.split(os.path.abspath(os.path.curdir))[1]).lower()
imageName = '{}/{}:{}'.format(username, project, timestamp)
imageNameLatest = '{}/{}:latest'.format(username, project)
isFinal = ''

for image in [imageName, imageNameLatest]:
    try:
        print(os.system('docker build -t {} .'.format(image)))
        sleep(3)
        print('#' * 50)
        print('## Imagem {} criada!'.format(image))
        print('#' * 50)
        sleep(3)
    except Exception as error:
        print(error)
