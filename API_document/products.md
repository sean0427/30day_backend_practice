** Products **
---
get list of products or insert product.

- URL
    `/api/products`

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
        Content [ { id: 12, type: 1 }, {...}, ... ]
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
    fetch("/api/products", {
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
    `/api/products/:id`

- Method
    `GET`, `PUT`, `DELETE`

- URL Params
    None

- Data Params
    None

- Succuss Reponse:
    - GET:
        Code: 200 OK
        Content: { id: 12, type: 1 }
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
    fetch("/api/products/:id", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
        },
        body: JSON.stringfy({
            //DATA
        }),
    }).then(reponse => /*do something*/);
```
