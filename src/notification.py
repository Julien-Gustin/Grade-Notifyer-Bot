def send_notification(message:str):
    print(message)


"""Here is an example by using pushover service to send notification to your phone"""
# import http.client, urllib

# def send_notification(message:str):
#     conn = http.client.HTTPSConnection("api.pushover.net:443")
#     conn.request("POST", "/1/messages.json",
#     urllib.parse.urlencode({
#         "token": "TOKEN",
#         "user": "USER",
#         "message": message,
#     }), { "Content-type": "application/x-www-form-urlencoded" })
#     conn.getresponse()