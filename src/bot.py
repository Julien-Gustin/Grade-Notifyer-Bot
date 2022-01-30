import json
import crawler
import time
import datetime

credentials = {}

with open("credentials.json") as fp:
    credentials = json.load(fp)


if __name__ == '__main__':
    prec_state = {}

    while True:
        now = datetime.datetime.now()
        submit_web_page_raw = crawler.get_submit_web_page(credentials)
        projects_dict = crawler.extract_project_fields(submit_web_page_raw)

        for project_id, values in projects_dict.items():
            if project_id not in prec_state: # new project 
                print("="*20, " {}\n".format(now), "New project detected !\n\t {} - {}\n".format(values["course_id"], values["project_name"]), "="*20, "\n")
                continue

            if values["grade"] != prec_state[project_id]["grade"]: # grade received
                print("="*20, " {}\n".format(now) ,"Grade received !\n\t {} - {}: {}\n".format(values["course_id"], values["project_name"], values["grade"]), "="*20, "\n")

        prec_state = projects_dict

        time.sleep(15)

