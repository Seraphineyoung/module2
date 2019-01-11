import requests
#
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxaefaacd34fc64849bca7491733dadc3f.mailgun.org/messages",
        auth=("api", "my mailgun api key"),
        data={"from": "Exicited User <seraphine_ene@yahoo.com>",
              "to": "Seraphine <kate.sorotos@bt.com>",
              "subject": "Hello Seraphine",
              "text": "Congratulations Seraphine, you just sent an email with Mailgun!  You are truly awesome!"})
    
    
send_simple_message()


