import json
import crawler
import time
import datetime
import notification # Use your o

credentials = {}

with open("credentials.json") as fp:
    credentials = json.load(fp)


if __name__ == '__main__':
    prec_state = {}

    while True:
        now = datetime.datetime.now()
        submit_web_page_raw = ""

        try:
            submit_web_page_raw = crawler.get_submit_web_page(credentials)
        except:
            print("An error occured")
            continue

        projects_dict = crawler.extract_project_fields(submit_web_page_raw)

        for project_id, values in projects_dict.items():
            if values["grade"] != prec_state[project_id]["grade"]: # grade received
                notification.send_notification("Grade received !\n{} - {}: {}\n".format(values["course_id"], values["project_name"], values["grade"]))

        prec_state = projects_dict

        time.sleep(10)

