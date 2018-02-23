** Product type **
---
get product type list.

- URL
    `/api/product_type`

- Method
    `GET`

- URL Params
    None

- Data Params
    None

- Success Response:
    Code: 200 OK
    Content: [
        { id: 1, , name: 'colse' },
        { id: 2, , name: '3c' },
    ]

- Error Reponse:
    - Code: 404 NOT FOUND
      Content: {}

    - Code: 404 BAD REQUEST
      Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/api/product_type", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
        },
    }).then(reponse => /*do something*/);
```

