# Python example
import requests

URL = 'https://docs.google.com/forms/.../formResponse'
DATA = {
    'entry.1234567890':'Answer 1', # Answer for Question 1
    'entry.0123456789':'python text entry' # Answer for Question 2
}

res = requests.post(URL, DATA)
print(res.status_code, res.reason)
