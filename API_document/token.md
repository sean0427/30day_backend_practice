** Token **
get user token

- URL
    `/token`

- Method
    `GET`

- URL Params
    None

- Data Params
    None

- Success Response:
    Code: 200
    Content: {
      "token": "eyJhbGciOiJIUzI1NiIsImlhdCI6MTUxOTM5NjI2MywiZXhwIjoxNTE5Mzk2ODYzfQ.eyJpZCI6MTB9._Vl7dN2BM_TgCNRFkav8ZWqxZtwHc1LQXxdB7mLmSCM"
    }

- Error Reponse:
    - Code: 401 UNAUTHORIZED

- Simple:
``` Javascript (ES6 Style)
    const encode = btoa(`${username}:${password}`)

    fetch("/token", {
        method: 'GET',
        headers: {
            Accept: 'application/json',
            Authorization: `Basic ${encode}`
        },
    }).then(response => response.json)
    .then(json => {
        const data = json.token.split('.')[1];
        return JSON.parse(window.atob(data));
    }).then(json => {
        if (Date.now() < Date.parse(json.repire_time)) //check token expire
        
        //json.user_email
        //json.user_id
    });
```

