from config import link, query, headers, requestList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from notify import Notification
import json
from datetime import datetime
import sys
import os

# off ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_data_file(work_type):
    f_name = 'id_{}.data'.format(work_type)
    if os.path.isfile(f_name):
        f = open(f_name, 'r')
    else:
        f = open(f_name, 'w+')

    data = f.read()
    f.close()

    return data


def set_data_file(work_type, data):
    f = open('id_{}.data'.format(work_type), 'w')
    f.write(data)
    f.close()


for key, value in requestList.items():
    query['request'] = key
    responseObj = requests.get(link, params=query, verify=False, headers=headers)
    returnText = json.loads(responseObj.text)

    if returnText != 0:
        try:
            if isinstance(returnText, list):
                if get_data_file(key) == responseObj.text:
                    continue

                set_data_file(key, responseObj.text)

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
