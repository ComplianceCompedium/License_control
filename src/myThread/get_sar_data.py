from src.myThread.ConnectToDB import connect
from base64 import b64encode, b64decode
import rsa, datetime

def getDataFromDb():
    print("using POSTgres I am coning here ")
    # cur = connect().cursor()
    # cur.execute("SELECT * FROM sar")
    # # print("cur value", json.dump(cur))
    # count = 0
    # for id in cur.fetchall():
    #     print(id);
    #     count += 1
    #
    return 3


def getTotalLicenseUser():
    cur = connect().cursor()
    cur.execute("SELECT no_of_users, users_left, expary_date FROM license where customer_id=3")

    for i in cur.fetchall():
        print("total no of user allowed for license",i[0]);
        print("no of user left",i[1]);
        print("expiry date",i[2]);
        if i[1] == 0:
            print("----------1")
            return 0
        elif i[2] < datetime.datetime.now():
            print("----------2")
            return 0
        else:
            return 1


