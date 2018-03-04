import sched, time
from get_sar_data import getDataFromDb, getTotalLicenseUser

import docker

s = sched.scheduler(time.time, time.sleep)


def create_sar_job(sc):

    totalCount = getDataFromDb();
    totalUserCount = getTotalLicenseUser();

    print(totalUserCount)

    if totalUserCount == 0:
        kill_docker_process(sc)

    else:
        s.enter(5, 1, create_sar_job, (sc,))

def kill_docker_process(sc):
    # print("more than 5 tinmes")
    client = docker.from_env(assert_hostname=False)
    list1 = client.containers.list(all=True)
    print(list1)
    for i in list1:
        print(i.name, i.status)
        if i.name == 'postgres':
            container = client.containers.get(i.name)
            container.stop()

            s.enter(5, 1, create_sar_job, (sc,))

