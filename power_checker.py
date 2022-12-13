from logger import planActivitiesLogger, outOfRegulationsActivitiesLogger, accidentActivitiesLogger, debugLogger
from repository import ResponseFileRepository as repository
from config import link, query, headers, requestList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from notify import Notification
import json
from datetime import datetime
import sys

# Configure request module: off ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

loggers = {
    2: planActivitiesLogger,
    3: outOfRegulationsActivitiesLogger,
    4: accidentActivitiesLogger
}

debugLogger.debug('start request')

for key, value in requestList.items():
    query['request'] = key
    responseObj = requests.get(link, params=query, verify=False, headers=headers)
    returnText = json.loads(responseObj.text)

    if returnText != 0:

        txt_dump = json.dumps(returnText, ensure_ascii=False)
        loggers[int(key)].info(txt_dump)
        try:
            if isinstance(returnText, list):
                if repository.get_by_activity_type(key) == txt_dump:
                    continue

                # @TODO: It is wrong to save the data inside repo. Use separate class to manage the repo.
                repository.set_by_activity_type(key, txt_dump)

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

        noty.telegram_bot()
