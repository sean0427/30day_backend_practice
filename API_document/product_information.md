Product Information
===
Get Product's information 

- URL
    `/api/product_info`

- Method
    `GET`

- URL Params
    `language=[integer]`
    `locale=[integer]`

- Data Params
    None

- Success Response:
    Code: 200 OK
    Content [ { id: 12, type: 1 }, {...}, ... ]

- Error Reponse:
    - Code: 404 NOT FOUND
    Content: {}

    - Code: 400 BAD REQUEST
    Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/api/product_info?language=1&locale=1", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
            'Content-Type': 'application/json',
        },
    }).then(reponse => /*do something*/);
```

Product Information
===
Insert new Product's information 

- URL
    `/api/product_info`

- Method
    `POST`

- URL Params
    None

- Data Params
    {
        "product_type": [Integer],
        "manufacturing_id": [Integer],
        "language_id": [Integer],
        "name": [String],
        "describe": [String],
        "image": [URI-String],
        "locale_id": [Integer],
        "price": [Integer],
        "publisher_id": [Integer],
        "start_datetime": [Datetime],
        "end_datetime": [Datetime],
    } 

- Success Response:
    Code: 200 OK
    Content { 
            "product_type": 1,
            "manufacturing_id": 1,
            "language_id": 1,
            "name": "name",
            "describe": "product describe",
            "image": 200,
            "locale_id": 22,
            "price": 200,
            "publisher_id": 1,
            "start_datetime": "",
            "end_datetime": "",
        }

- Error Reponse:
    - Code: 404 NOT FOUND
    Content: {}

    - Code: 400 BAD REQUEST
    Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/api/product_info?language=1&locale=1", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
            'Content-Type': 'application/json',
        },
        body: { JSON.stringfy({
            "product_type": 1,
            "manufacturing_id": 1,
            "language_id": 1,
            "name": "name",
            "describe": "product describe",
            "image": 200,
            "locale_id": 22,
            "price": 200,
            "publisher_id": 1,
            "start_datetime": ,
            "end_datetime": ,
        }) },
    }).then(reponse => /*do something*/);
```
