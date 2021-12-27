// NodeJS example with Request
const request = require('request');

const URL = 'https://docs.google.com/forms/.../formResponse';
const DATA = {
    'entry.0123456789':'Answer 1', // Answer for Question 1
    'entry.1234567890':'javascript text entry' // Answer for Question 2
}

request({
    url:URL,
    method:'POST',
    form:DATA,
}, function (error, res) {
    if (error) console.error(error)
    else console.log(res.statusCode, res.statusMessage)
})
