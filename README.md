# Google Form Spamming Guide

Most reliable for simple, anonymous forms. Proof of concept, don't fuck around too much with this.
___

**1. Fill out the form.**

<img src="https://user-images.githubusercontent.com/77910109/147497398-35f06f78-3c7d-498f-bfbe-fea8a03c7dce.png" height="50%" width="50%"/>

___

**2. Select `CTRL + SHIFT + I` to open devtools**

This is the same place you'd go to for Inspect Element. Locate and select the Network panel.

<img src="https://user-images.githubusercontent.com/77910109/147497377-144f8c5b-7900-4e1b-8ee9-77feed8ed2f1.png" height="75%" width="75%"/>

___

**3. Submit the form.**

You should see several entries appear in the Network panel. Select the one that says `formResponse`. This should open up a new menu on the side.

<img src="https://user-images.githubusercontent.com/77910109/147497351-3e73a325-bd99-415c-a78d-544eeec5ef8b.png" height="75%" width="75%"/>

On Chrome, this might look a little bit different:

<img src="https://user-images.githubusercontent.com/77910109/147497322-ee6b2502-a7a1-493f-b680-ed380aec0fc0.png" height="75%" width="75%"/>

___

**4. In the side menu, copy the url under the Headers tab**

This should be the first thing you see after opening the `formResponse` entry.

<img src="https://user-images.githubusercontent.com/77910109/147497857-e739c66a-4e79-46bb-900d-aa71516a95b5.png" height="75%" width="75%"/>

On Chrome:

<img src="https://user-images.githubusercontent.com/77910109/147498063-41dee41b-3d0e-4f9e-b981-944667914511.png" height="75%" width="75%"/>

___

**5. Under the Request/Payload tab, copy the entries that correspond to your form submission.**

On Firefox the tab is called "request", while on chrome it's called "payload."

<img src="https://user-images.githubusercontent.com/77910109/147498175-26299645-ecde-4e3f-8ecf-be106977d99b.png" height="75%" width="75%"/>

<img src="https://user-images.githubusercontent.com/77910109/147498422-b5a7382d-669c-418c-91e7-d20f4787a4cf.png" height="75%" width="75%"/>

___

**6. Fill this information into your script.**

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

`URL` is the url copied from the headers tab, while the `DATA` dictionary is the payload/request info. You can change the values to whatever you want as long as the form permits it.

Here's an example with NodeJS using the Request library:

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

### Status Code Examples

- `200` Submission went through. Great success!
- `400` Bad request. You might've forgotten a required question, or submitted a multiple choice option that doesn't exist.
- `404` Not found. Your form doesn't exist. Maybe you copied the url wrong.
- `429` Rate limited. You're trolling too hard.
