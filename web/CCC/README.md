# CCC

Author: [roerohan](https://github.com/roerohan)

## Description

This challenge is based on Path Traversal and JWTs.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Knowledge of JWT

## Sources

```
You can steal a car if you steal its key.
```

## Exploit

First, in the website source, you can see that there's a route to login (`/login`) and a route to get the names of the admins (`/adminNames`). So, when you try to visit `/login`, you see a form. Post that and check the response on the Network Tab in your browser. You can see there's a header called `token` which stores a JWT. You can decode the token (maybe on [jwt.io](https://jwt.io)) to see that the payload is of this format (I typed username: asd, password: asd):

```
{
  "username": "nfq",
  "password": "nfq",
  "admin": "snyfr",
  "iat": 1593506966
}
```

We can see that the `username` changed from `asd` to `nfq`. So this hints that this could be `rot13`. When you apply the `rot13` cipher on the admin value `snyfr`, you see that it returns a string `false`. So, we can change this to a rot13 encrypted string for `true`, but to do that, we need the JWT secret.
<br />

On going back to the page, you see there's a route called `/adminNames`. It downloads a file for you, which has sort of a URL: `csivitu/authorized_users/blob/master/`. Seems familiar? This looks like a GitHub URL. So, if you visit that repository on GitHub, and checkout the `root` file [here](https://github.com/csivitu/authorized_users/blob/master/csivit/root), you can see a list of usernames.

```
thebongy
roerohan
namsnath
sudo-nan0-RaySK
theProgrammerDavid
sauravhiremath
```

These are the usernames of the website admins! Now, in the JWT you were creating, you can change the `username` key to a rot13 encrypted version of one of these, for example, `ebrebuna` is the rot13 encrypted ciphertext for `roerohan`. Here's what our JWT payload looks like now:

```
{
  "username": "ebrebuna",
  "password": "nfq",
  "admin": "gehr",
  "iat": 1593506966
}
```

But, we still need the JWT secret. If you observe the request on `/adminNames`, you see that it actally redirects to `/getFile?file=admins`. This route seems suspicious. We can try to include other files using this. When you try `/getFile?file=.env`, it returns `No such file or directory: /app/public/.env`. So, we can try `../.env` to come out of the public folder. You get a file in return, which is the `.env` containing the secret!

```
JWT_SECRET=Th1sSECr3TMu5TN0Tb3L43KEDEv3RRRRRR!!1
```

Use this secret to create a new token. Now, visit the `/admin` route. It says:

```
{
  "success": false,
  "message": "Invalid Token, Headers?"
}
```

Which means, you'll have to pass the JWT in the headers. Auth tokens are generally passed in the Authorization header, so let's try that. When you pass the new formed JWT in the Authorization header. You can do this using python.

```python
>>> import requests
>>> r= requests.get('http://localhost:3000/admin', headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVicmVidW5hIiwicGFzc3dvcmQiOiJuZnEiLCJhZG1pbiI6ImdlaHIiLCJpYXQiOjE1OTM1MDY5NjZ9.LCbBdHCDlx64bTFeErtBAeoL000HIqyFStvUxlTtVE8'})
>>> r.text
```

The text in the response is:

```
Hey roerohan! Here's your flag: pfvpgs{1a_gu3_3aq_1g_q0rfa'g_3i3a_z4gg3e}
```

rot13 decrypt this flag to get the real flag.
<br />

The flag is:

```
csictf{1n_th3_3nd_1t_d0esn't_3v3n_m4tt3r}
```