import json, base64, requests

def lambda_handler(event, context):
    # TODO implement
    payload = {
        'grant_type': 'authorization_code',
        'code': base64.b64decode(event['body']).decode("utf-8").split('&')[0].strip('code='),
        'redirect_uri': 'https://3f5v30il55.execute-api.ap-east-1.amazonaws.com/callback',
        'client_id': 'p4EM9LM5psKQCZM74cYNj4',
        'client_secret': 'e2l6gL7g4R8ZBZowGr0XzN4OmOTicZYbmhVoTN5zaIq'
    }
    r = requests.post('https://notify-bot.line.me/oauth/token', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload)
    access_token = json.loads(r.text)['access_token']
    requests.post('https://script.google.com/macros/s/AKfycbxKeUQT2lnJec67Gfa3HCCcqLOJDoc9YYXIZuABjDj1ZDT0ot3FWMsYOsNJCBX2Gbohnw/exec', data={'access_token': access_token})
    return {
        'statusCode': 200,
        'body': '訂閱成功，請關閉視窗！'
    }
