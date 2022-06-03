# Grade Notifyer Bot

 A bot that automatically crawl the [submission platform of montefiore](https://submit.montefiore.ulg.ac.be/index.php/student) to notify the student when a project has been graded.

## How to Use?

1. Install dependencies and create the credential file `./setup`
2. Modify `credentials.json` file with your credentials
3. Launch the bot `./run.sh`

## Extensions

The purposes of this project is to be extended, here is an exemple of use:

- Run it on a raspberry pi that notify the student via pushover app

For that purpose just modify `src/notification.py`

I personally use the service of [pushover](https://pushover.net/) that allow me to send me notification to my phone via http request.

Here is an example:

```py
def send_notification(message:str):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "TOKEN",
        "user": "USER",
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
```

## Example

<p align="center">
  <img src="https://github.com/Julien-Gustin/Grade-Notifyer-Bot/blob/master/example_alex.jpg?raw=true" 
     height="500" />
  <br>
  <em style="text-align:center">Example using pushover app</em>
</p>

