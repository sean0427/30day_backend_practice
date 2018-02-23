** Lanugage **
---
get language list.

- URL
    `/api/language`

- Method
    `GET`

- URL Params
    None

- Data Params
    None

- Success Response:
    Code: 200 OK
    Content: [
        { id: 1, code: 'en', name: 'english' },
        { id: 2, code: 'zh-TW', name: 'hant' },
    ]

- Error Reponse:
    - Code: 404 NOT FOUND
      Content: {}

    - Code: 404 BAD REQUEST
      Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/api/language", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
    }).then(reponse => /*do something*/);
```

