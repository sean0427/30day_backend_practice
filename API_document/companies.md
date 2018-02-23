** Companiess **
---
get list of companiess or insert companies.

- URL
    `companiess`

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
        Content: [
            { name: 'NAME', address: 'ADDRESS', telephone: 'TELEPHONE', contant_person_name: 'PRESON_NAME' }
            , {...}, ... ]
    - POST:
        Code: 201 CREATED
        Content { ISERT NEW COMPANY DATA }

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
    fetch("/companiess", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
        },
    }).then(reponse => /*do something*/;
```

---

** Company by id **
---
get, update, delete companies data by id.


- URL
    `companiess/:id`

- Method
    `GET`, `PUT`, `DELETE`

- URL Params
    None

- Data Params
    None

- Succuss Reponse:
    - GET:
        Code: 200 OK
        Content: { name: 'NAME', address: 'ADDRESS', telephone: 'TELEPHONE', contant_person_name: 'PRESON_NAME' }
    - PUT:
        Code: 201 CREATED
        Content: { UPDATE COMPANY DATA }
    - DELETE:
        Code: 204 NO CONTENT
        Content {}

- Error Reponse:
    - PUT & DELETE
        - Code: 401 UNAUTHORIZED
        - Code: 400 BAD REQUEST
          Content {}
    - GET
        - Code: 400 BAD REQUEST
          Content {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/companiess/:id", {
        method: 'PUT',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${TOKEN}`
        },
        body: JSON.stringfy({
            name: 'NAME',
            address: 'ADDRESS',
            telephone: 'TELEPHONE',
            contant_person_name: 'PRESON_NAME',
        }),
    }).then(reponse => /*do something*/);
```
