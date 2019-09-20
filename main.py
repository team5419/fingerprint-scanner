import requests
import getpass

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
    login(
        session=session,
        email="felix@tacocat.com",#input("Enter email: "),
        password="felixmo2006894"#getpass.getpass()
    )

    loguser(session, 2)

    logout(session) #logout dosent work