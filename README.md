# Grade Notifyer Bot

 A bot that automatically crawl the [submission platform of montefiore](https://submit.montefiore.ulg.ac.be/index.php/student) to notify the student when a project has been graded.

## Utilisation

1. Install dependencies and create the credential file `./setup`
2. Modify `credentials.json` file with your credentials
3. Launch the bot `./run.sh`

## Extensions

The purposes of this project is to be extended, here is an exemple of utilisation:

- Run it on a raspberry pi that notify the student via discord or telegram

For that purpose just get to `src/bot.py` and modify whatever you want.

