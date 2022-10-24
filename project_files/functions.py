import urllib.request
import urllib.parse


def send_SMS(apikey, *numbers, author, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'author': author})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.txtlocal.com/send/?")
    send = urllib.request.urlopen(request, data)
    sms = send.read()
    return(sms)