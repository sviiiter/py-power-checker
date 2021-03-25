from config import link, query, headers, requestList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from notify import Notification
import json
from datetime import datetime
import sys

# off ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


for key, value in requestList.items():
    query['request'] = key
    responseObj = requests.get(link, params=query, verify=False, headers=headers)
    returnText = json.loads(responseObj.text)

    if returnText != 0:
        try:
            if isinstance(returnText, list):
                place = returnText[0]['Place']
                timeFrom = datetime.strptime(returnText[0]['DisconnectionDateTime'], '%Y-%m-%dT%H:%M:%S').strftime('%d.%m.%Y %H:%M')
                timeTo = datetime.strptime(returnText[0]['EnergyOnPlanningDateTime'], '%Y-%m-%dT%H:%M:%S').strftime('%d.%m.%Y %H:%M')
                placeEquipment = returnText[0]['EquipmentName']
                workDesc = returnText[0]['DisconnectionCause']

                noty = Notification('{}({}): {}-{} | {}'.format(value, workDesc, timeFrom, timeTo, place))
            else:
                noty = Notification(value)
        except:
            noty = Notification(sys.exc_info()[0])
            raise

        noty.show_notification()
        noty.telegram_bot()
