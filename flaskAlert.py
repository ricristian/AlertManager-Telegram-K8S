import telegram
import logging
import json
import os
from flask import Flask
from flask import request

app = Flask(__name__)
app.secret_key = 'aYT>.L$kk2h>!'

bot = telegram.Bot(token=os.environ["BOT_TOKEN"])
chatID = os.environ["CHAT_ID"]
@app.route('/alert', methods=['POST'])
def postAlertmanager():
    content = json.loads(request.get_data())
    # with open("Output.txt", "w") as text_file:
    #     text_file.write("{0}".format(content))
    try:
        for alert in content['alerts']:
            message = """Alertname: """+alert['labels']['alertname']+""" \n"""
            message += """Status: """+alert['status']+""" \n"""

            if alert['status'] == "firing":
                message += """Detected: """+alert['startsAt']+""" \n"""

            if alert['status'] == "resolved":
                message += """Resolved: """+alert['endsAt']+""" \n"""

            if 'name' in alert['labels']:
                message += """Instance: """+alert['labels']['instance']+"""("""+alert['labels']['name']+""") \n"""
            else:
                message += """Instance: """+alert['labels']['instance']+""" \n"""

            message += """\n"""+alert['annotations']['description']+""""""
            message += """\n"""+alert['annotations']['summary']+""""""
            message += "\n------ END OF MESSAGE ------"

            bot.sendMessage(chat_id=chatID, text=message)
        return "Alert OK", 200
    except Exception as e:
        print(e)
        bot.sendMessage(chat_id=chatID, text="Error! %s" % e)
        return "Alert nOK %s" %e, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9119, debug=True)

