import requests

res = requests.post(
    "https://timesheet.team5419.org/sessions",
    data={
        "email" : "",
        "password" : ""
    }
)

session_key = res.cookies.get("_timesheet_session")

def loguser(key):
    res = requests.post(
        "http://timesheet.team5419.org/timelogs",
        data={
            "authenticity_token": session_key,
            "owner_userid": key,
            "multi": "Submit"
        }
    )

  return res

loguser(1)
