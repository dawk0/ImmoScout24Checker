import requests
import re
import time
import credentials


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)


url = 'https://www.immobilienscout24.de/Suche/shape/haus-kaufen?shape' \
      '=eWpgd0h3bXloQGhgQ2tmRHR4Q3JsQ2Z1QXN1RXZ6QXt5RW57Q3dkR25iQWFdZnJAeHZAcH1BZVB4X0FhY' \
      '1VudUFraEN4SWdqQml7Qmt0SndyQXVjQXV9UGBdZ3VBdGNBc31CYG5LZ31BamJReW5HfGNOdUFwbkJ8ZEF' \
      'ydUVie0NwdUU.&sorting=2&enteredFrom=result_list#/'
firsttime = 1
i = 0
while True:
    print("Skript läuft schon " + str(i) + " Minuten.")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        telegram_bot_sendtext("Mit dem Skript stimmt was nicht... Response Code: " + str(response.status_code))
    result = re.findall(r'expose/[\s:]*(\d*)', response.text)
    result = list(dict.fromkeys(result))
    result.remove('')
    if firsttime == 1:
        temp = result
        firsttime = 0
    for expose in result:
        if expose not in temp:
            telegram_bot_sendtext("WAS NEUES BEI IMMOSCOUT GOOGOGO " + expose)
            telegram_bot_sendtext("https://www.immobilienscout24.de/expose/" + expose)
            temp.append(expose)
    time.sleep(60)
    i += 1