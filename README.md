# Google Form Spamming

Guide to automating Google form submissions. Mostly proof of concept; don't screw around too much with this.

## Automated Setup

The `automated.py` script scrapes forms and automates the setup/submission process for you.

<img src="https://user-images.githubusercontent.com/77910109/147603875-7726ac8a-36e0-477d-8623-baad371e77ee.png" height="75%" width="75%"/>

If this doesn't work try the manual method.

Note that this requires Python 3.10 as well as [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [Requests](https://pypi.org/project/requests/).


## Manual Setup Method
___

**1. Fill out the form.**

<img src="https://user-images.githubusercontent.com/77910109/147497398-35f06f78-3c7d-498f-bfbe-fea8a03c7dce.png" height="50%" width="50%"/>

___

**2. Select `CTRL + SHIFT + I` to open devtools**

This is the same place you'd go to for Inspect Element. Locate and select the Network panel.

<img src="https://user-images.githubusercontent.com/77910109/147497377-144f8c5b-7900-4e1b-8ee9-77feed8ed2f1.png" height="90%" width="90%"/>

___

**3. Submit the form.**

You should see several entries appear in the Network panel. Select the one that says `formResponse`. This should open up a new menu on the side.

<img src="https://user-images.githubusercontent.com/77910109/147497351-3e73a325-bd99-415c-a78d-544eeec5ef8b.png" height="90%" width="90%"/>

On Chrome, this might look a little bit different:

<img src="https://user-images.githubusercontent.com/77910109/147497322-ee6b2502-a7a1-493f-b680-ed380aec0fc0.png" height="90%" width="90%"/>

___

**4. In the side menu, copy the url under the Headers tab**

This should be the first thing you see after opening the `formResponse` entry.

<img src="https://user-images.githubusercontent.com/77910109/147497857-e739c66a-4e79-46bb-900d-aa71516a95b5.png" height="90%" width="90%"/>

On Chrome:

<img src="https://user-images.githubusercontent.com/77910109/147498063-41dee41b-3d0e-4f9e-b981-944667914511.png" height="90%" width="90%"/>

___

**5. Under the Request/Payload tab, copy the entries that correspond to your form submission.**

On Firefox the tab is called "request", while on chrome it's called "payload."

<img src="https://user-images.githubusercontent.com/77910109/147498175-26299645-ecde-4e3f-8ecf-be106977d99b.png" height="90%" width="90%"/>

<img src="https://user-images.githubusercontent.com/77910109/147498422-b5a7382d-669c-418c-91e7-d20f4787a4cf.png" height="90%" width="90%"/>

___

**6. Fill this information into your script.**

`URL` is the url copied from the headers tab

`DATA` is a dictionary of the payload/request info. 

You can change the values to whatever you want as long as the form permits it.

Python example:

```py
import requests

URL = 'https://docs.google.com/forms/....../formResponse'
DATA = {
    'entry.1251875408':'Answer 1', # Answer for Question 1
    'entry.1304624064':'python text entry' # Answer for Question 2
}

res = requests.post(URL, DATA)
print(res.status_code, res.reason)
```

NodeJS example using the the Request library:

```js
const request = require('request');

const URL = 'https://docs.google.com/forms/....../formResponse';
const DATA = {
    'entry.1251875408':'Answer 1', // Answer for Question 1
    'entry.1304624064':'javascript text entry' // Answer for Question 2
}

request({
    url:URL,
    method:'POST',
    form:DATA,
}, function (error, res) {
    if (error) console.error(error)
    else console.log(res.statusCode, res.statusMessage)
})
```
___

**7. Run**

<img src="https://user-images.githubusercontent.com/77910109/147498948-d47d0443-9bf7-4b41-89ef-00834a9ec4ec.png" height="75%" width="75%"/>

___

## Status Code Examples

- `200` Submission went through. Great success!
- `400` Bad request. You might've forgotten a required question, or submitted a multiple choice option that doesn't exist.
- `404` Not found. Your form doesn't exist. Maybe you copied the url wrong.
- `405` Method not allowed. Probably messed something up, definitely a skill issue.
- `429` Rate limited. You're trolling too hard.
