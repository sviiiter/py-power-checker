import json
import sys
from datetime import datetime

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from config import link, query, headers, requestList
from logger import planActivitiesLogger, outOfRegulationsActivitiesLogger, accidentActivitiesLogger, debugLogger
from notify import Notification
from repository import ResponseFileRepository as repository

# Configure request module: off ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

loggers = {
    2: planActivitiesLogger,
    3: outOfRegulationsActivitiesLogger,
    4: accidentActivitiesLogger
}

debugLogger.debug('start request')


def format_response(return_text: list, action_type: str) -> str:
    place = return_text[0]['Place']
    time_from = datetime.strptime(return_text[0]['DisconnectionDateTime'], '%Y-%m-%dT%H:%M:%S').strftime(
        '%d.%m.%Y %H:%M')
    time_to = datetime.strptime(return_text[0]['EnergyOnPlanningDateTime'], '%Y-%m-%dT%H:%M:%S').strftime(
        '%d.%m.%Y %H:%M')
    work_desc = return_text[0]['DisconnectionCause']

    return '{}({}): {}-{} | {}'.format(action_type, work_desc, time_from, time_to, place)


for key, value in requestList.items():
    query['request'] = key
    responseObj = requests.get(link, params=query, verify=False, headers=headers)
    returnText = json.loads(responseObj.text)

    if returnText != 0:
        loggers[int(key)].info(
            json.dumps(returnText, ensure_ascii=False)
        )
        try:
            if isinstance(returnText, list):

                txt_dump = format_response(returnText, value)

                if repository.get_by_activity_type(key) == txt_dump:
                    continue

                # @TODO: It is wrong to save the data inside repo. Use separate class to manage the repo.
                repository.set_by_activity_type(key, txt_dump)

                noty = Notification(txt_dump)
            else:
                noty = Notification(value)
        except:
            noty = Notification(sys.exc_info()[0])
            raise

        noty.telegram_bot()
