import requests
import getpass
import pyfingerprint

def login(session, email, password):
    res = session.post(
        "https://timesheet.team5419.org/sessions",
        data={
            "email" : email,
            "password" : password
        }
    )

    print(res.status_code)

    print("logged in!")

    return res.cookies.get("_timesheet_session")

def logout(session):
    res = session.get(
        "https://timesheet.team5419.org/log_out"
    )

    print(res.status_code)

    print("logged out!")

def loguser(session, key):
    print(session.cookies["_timesheet_session"])
    res = session.post(
        "https://timesheet.team5419.org/timelogs",
        data={
            "authenticity_token": session.cookies,
            "owner_userid": key,
            "multi": "Submit"
        }
    )

    print(res.text)

    return res

with requests.Session() as session:
    try:
        sensor = pyfingerprint.PyFingerprint(
            '/dev/ttyUSB0',
            57600,
            0xFFFFFFFF,
            0x00000000
        )

        if sensor.verifyPassword() == False:
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    login(
        session=session,
        email=input("Enter email: "),
        password=getpass.getpass()
    )

    print('Currently used templates: ' + str(sensor.getTemplateCount()) +'/'+ str(sensor.getStorageCapacity()))

    try:
        while True:
            while sensor.readImage() == False:
                pass

            sensor.convertImage(0x01)
            result = sensor.searchTemplate()

            pyfingerprint()

            userID = result[0]
            accuracy = result[1]

            if userID == -1:
                print(f"No match found!")
            else:
                print(f"Loged user with id {userID}, accuracy {accuracy}.")
                loguser(session, userID)
            
    except KeyboardInterrupt:
        print("123")
    finally:
        logout(session) #logout dosent work