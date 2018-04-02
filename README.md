[![Build Status](https://travis-ci.org/Davide95/telegram-integration-dialogflow.svg?branch=master)](https://travis-ci.org/Davide95/telegram-integration-dialogflow)

# telegram-integration-dialogflow
A substitute for the default Telegram integration on Dialogflow that supports advanced features:
* inline queries;
* incoming voice messages;

## How to use it
### Installation
Before running it, you need the right version of the libraries needed.

You have to run `pip install -r requirements.txt` in the project directory.

Also, if you want to use wit.ai, you have to install [ffmpeg](https://www.ffmpeg.org/download.html) with `libmp3lame` codecs.

### How to run it
If you want to run the script locally, just type in your terminal:

 `python3 run.py --TELEGRAM_TOKEN [your token]  --DIALOGFLOW_TOKEN [your token] [optional arguments]`

You should consider to create an init script if you want to run it on production.

#### Arguments
In order to set your bot you will need to pass as arguments:

|Argument           |Required?           |Description                  |Defaults         |
|-------------------|:------------------:|-----------------------------|:---------------:|
|--TELEGRAM_TOKEN   | :heavy_check_mark: |Define Telegram bot Token    | **_Mandatory_** |
|--DIALOGFLOW_TOKEN | :heavy_check_mark: |Define Dialogflow Token      | **_Mandatory_** |
|--ADMIN_CHAT_ID    | :x:                |Define Telegram admin chatID | `None`	         |
|--WIT_TOKEN        | :x:                |Define Wit Token             | `None`	         |
|--log              | :x:                |Set logging value            | `DEBUG`         |

If you want telegram notifications every time the script will be shut down / turned up you need to set the `ADMIN_CHAT_ID`.  
You can also change the log level: consider using `INFO` in production and `DEBUG` for debugging purposes.

## How to contribute
Before submitting new pull requests, ensure that your code follows the PEP 8 style guide and run pylint3 to find bad practices.

It is recommented to sign every commit with your PGP key, if you have one.
