** Users **
---
register a user.

- URL
    `users`

- Method
    `POST`

- URL Params
    None

- Data Params
    content { 
        email: 'email@address.com'
        password: 'PASSWORD'
    }

- Success Response:
    Code: 201
    Content: { REGISTER USER DATA }

- Error Reponse:
    - Code: 404
      Content: {}

    - Code: 400
      Content: {}

- Simple:
``` Javascript (ES6 Style)
    fetch("/user", {
        method: 'POST',
        headers: {
            Accept: 'application/json',
        },
        body: JSON.stringfy({
            email: 'email@address.com'
            password: 'PASSWORD',
        }),
    }).then(reponse => /*do something*/);
```
