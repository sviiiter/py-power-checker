from config import link, query, headers, requestList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from notify import Notification
import json

# off ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


for key, value in requestList.items():
    query['request'] = key
    returnCode = requests.get(link, params=query, verify=False, headers=headers).text

    if json.loads(returnCode) != 0:
        noty = Notification(value)
        noty.show_notification()
        noty.telegram_bot()
