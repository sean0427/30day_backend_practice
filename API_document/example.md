** name **
===

WHAT API DO

- URL
    `URL`

- Method
    `GET` | `POST` | `DELETE` | `PUT`

- URL Params
    key=[TYPE]

- Data Params
    key=[TYPE]

- Success Response:
    Code: CODE
    Content: {
        //response content
    }

- Error Reponse:
    Code: CODE
    Content: {
        //response content
    }

- Simple:
``` Javascript (ES6 Style)
    fetch("/URL", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${encode}`
        },
    }).then(reponse => /*do something*/);
```

