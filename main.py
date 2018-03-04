from __future__ import print_function
import datetime
import sys

from src.myThread.sarjob import create_sar_job, s

sys.path.append('.')
sys.path.append('..')


if __name__ == '__main__':

    start_time = datetime.datetime.now().replace(microsecond=0)
    print('Sample start: {}'.format(start_time))

    try:
        s.enter(5, 1, create_sar_job, (s,))
        s.run()

    except Exception as err:
            print(err)
            raise

    print()
    input('Press ENTER to exit...')
