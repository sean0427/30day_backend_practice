** Language Products **
---
get list of language products or insert product.

- URL
    `/api/language_products`

- Method
    `GET`
    `POST`

- URL Params
    `size=[integer]`

- Data Params
    None

- Succuss Reponse:
    - GET:
        Code: 200 OK
        Content: [ {
                    product_id: 1,
                    language_id: 1,
                    name: 'NAME',
                    describe: 'DESCRIBE',
                    image: 'IMAGE',
                },
                {...},
                 ]
    - POST:
        Code: 201 CREATED
        Content { ISERT NEW PRODUCT DATA }

- Error Reponse:
    - GET
        - Code: 404 NOT FOUND
          Content: {}

        - Code: 400 BAD REQUEST
          Content: {}
    - POST
        - Code: 401 UNAUTHORIZED

        - Code: 400 BAD REQUEST
          Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/language products", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
        },
    }).then(reponse => /*do something*/;
```

---

** Product by id **
---
get, update, delete product data by id.


- URL
    `language products/:id`

- Method
    `GET`, `PUT`, `DELETE`

- URL Params
    None

- Data Params
    None

- Succuss Reponse:
    - GET:
        Code: 200 OK
        Content: {
                product_id: 1,
                language_id: 1,
                name: 'NAME',
                describe: 'DESCRIBE',
                image: 'IMAGE',
                }
    - PUT:
        Code: 201 CREATED
        Content: { UPDATE PRODUCT DATA }
    - DELETE:
        Code: 204 NO CONTENT
        Content {}

- Error Reponse:
    - Code: 401 UNAUTHORIZED
    - Code: 400 BAD REQUEST

- Simple:
``` Javascript (ES6 Style)
    fetch("/api/language_products/:id", {
        method: 'PUT',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
        },
        body: JSON.stringfy({
                product_id: 1,
                language_id: 1,
                name: 'NAME',
                describe: 'DESCRIBE',
                image: 'IMAGE',
        }),
    }).then(reponse => /*do something*/);
```
