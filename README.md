[![csivit][csivitu-shield]][csivitu-url]
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/csivitu">
    <img src="https://csivit.com/images/favicon.png" alt="Logo" width="80">
  </a>

  <h3 align="center">CTF Challenges</h3>

  <p align="center">
    CTF challenges for <b>csictf</b> 2020.
    <br />
    <a href="https://github.com/csivitu/ctf-challenges"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/csivitu/ctf-challenges">View Demo</a>
    ·
    <a href="https://github.com/csivitu/ctf-challenges/issues">Report Bug</a>
    ·
    <a href="https://github.com/csivitu/ctf-challenges/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Template](#Template)
* [Contributing](#contributing)
* [License](#license)
* [Contributors](#contributors-)



<!-- ABOUT THE PROJECT -->
## About The Project

This is a repository to store CTF challenges to be deployed for `csictf`.

<!-- GETTING STARTED -->
## Getting Started

> Note: This is a beginner CTF, hence the challenges should be of easy / moderate difficulty.
<br />

> Note: DO NOT PLAGIARIZE challenges from other CTFs. You can take inspiration but not have the exact same challenge.

The following are the categories of challenges that are to be made:

- Pwn
- Web
- OSINT
- Linux
- Crypto
- Forensics
- Reversing
- Miscellaneous

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/csivitu/ctf-challenges.git
```

## Template

### Flag Format

- The flags must be enclosed in `csictf{}`.
- They can have numbers, alphabets, `_`s, `'`s, `!`s, `.`s, `+`s, `-`s, `@`s, `#`s, `$`s, `%`s, `:`s, `>`s.
- They must be related to the challenge.
- They must not be so simple that you can guess them.

Here's a regex for the flag format.

```
/^csictf{[\w_!@#?$%\.'"+:->]{5,50}}$/
```

Here's a sample flag.

```
csictf{th1s_i5_4_s4mpl3_fl4g'+!-.@#$%?}
```

### Directory Structure

The following are guidelines for creating challenge folders.

- Each challenge has it's own folder, which is placed in the relevant directory amongst the ones enlisted above.
- Each challenge **must** have a `README.md` file describing how to solve the challenge, along with the relevant code / files that needs to be run / deployed on the server.
- The flag must be present in the `README.md` for the challenge.
- We prefer having each challenge in it's own docker container, so that it's simple to deploy.

```
- pwn/
  - n00binary/
    - static/
      - img1.png
    - README.md
    - n00binary
    - n00binary.c
    - Dockerfile
- web/
  - localize/
    - README.md
    - localize.php
    - Dockerfile
```

> The static folder contains images that may be used in the `README.md`.

### Template for Challenge README

As mentioned earlier, each challenge requires a `README`. The README must be written in such a way that this can serve as an **official write-up** later. This should have the following format.

```
# Challenge Name

Author: [author](https://github.com/author)

## Description

Brief Description about challenge

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [sample.py](./sample.py)
- [sample.txt](./sample.txt)

<!-- Remove this comment, and the '\' before '```' -->
\```
Challenge description to go up on the website.

Hint 1: If any - Points 100
Hint 2: If any - Points 200
\```

## Exploit

<!-- Much more detailed description than the following. -->
Reverse `sample.py` to decrypt the flag in `sample.txt.`
<br />

The last line should be the flag.
<br />

The flag is:

\```
csictf{some_flag_here}
\```
```

> Refer to this [sample](https://github.com/csivitu/CTF-Write-ups/tree/master/HSCTF%207/Binary%20Exploitation/boredom#exploitation) for writing the exploit section.

### challenge.yml

Every challenge must have a `challenge.yml`, in the format specified in [challenge-example.yml](./challenge-example.yml). This is **MANDATORY**, without this the challenge will not be deployed. Remove the comments in the specified format, leave out the `value`, `decay` and `minimum` keys as they are in the template. Every challenge has 500 points initially and decays to 100 points over 450 solves.

### Dockerfiles

Here are some Dockerfiles you can refer to while making your own. Make sure you test it locally before making the PR.

- [Node.js Server](./web/File20%Library/Dockerfile)
- [Flask Server](./web/Mr.20%Rami)
- [Netcat to Python](./miscellaneous/Prison%20Break/Dockerfile)
- [Pwn Binary](./pwn/pwn%20intended%0x1/Dockerfile)

Make sure you read the `Dockerfile`s and include the necessary files like the `flag.txt`. **REMEMBER TO ADD THE `README.md` and `challenge.yml` FILES TO `.dockerignore`, BECAUSE IT HAS THE SOLUTION.**.

<!-- CONTRIBUTING -->
## Contributing

Besides contribution of challenges, contribution of *ideas* for challenges is also appreciated. You can put forward your ideas to [@roerohan](https://github.com/roerohan), [@theProgrammerDavid](https://github.com/theProgrammerDavid) and [@thebongy](https://github.com/thebongy).
<br />

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Submit your idea for the challenge in the respective `README`.
3. File a Pull Request with the `challenge-idea` tag. Each challenge must have it's own PR.
4. Once the challenge is approved, the tag is changed to `challenge-approved`, we comment on the PR.
5. Build the final challenge and update the *same* PR.
6. Make sure all commit messages are in accordance with the guidelines in [CONTRIBUTING.md](./CONTRIBUTING.md).
7. Any issues in the challenge will be addressed using GitHub Issues.

You are requested to follow the contribution guidelines specified in [CONTRIBUTING.md](./CONTRIBUTING.md) while contributing to the project :smile:.

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[csivitu-shield]: https://img.shields.io/badge/csivitu-csivitu-blue
[csivitu-url]: https://csivit.com
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/csivitu/ctf-challenges/issues

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/roerohan"><img src="https://avatars0.githubusercontent.com/u/42958812?v=4" width="100px;" alt=""/><br /><sub><b>Rohan Mukherjee</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=roerohan" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/thebongy"><img src="https://avatars1.githubusercontent.com/u/7080652?v=4" width="100px;" alt=""/><br /><sub><b>Rishit Bansal</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=thebongy" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/theProgrammerDavid"><img src="https://avatars2.githubusercontent.com/u/35698009?v=4" width="100px;" alt=""/><br /><sub><b>theProgrammerDavid</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=theProgrammerDavid" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/AJ1479"><img src="https://avatars2.githubusercontent.com/u/67030839?v=4" width="100px;" alt=""/><br /><sub><b>AJ1479</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=AJ1479" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=AJ1479" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/alias-rahil"><img src="https://avatars2.githubusercontent.com/u/59060219?v=4" width="100px;" alt=""/><br /><sub><b>alias-rahil</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=alias-rahil" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=alias-rahil" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashikka"><img src="https://avatars1.githubusercontent.com/u/58368421?v=4" width="100px;" alt=""/><br /><sub><b>ashikka</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=ashikka" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=ashikka" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/parthkgh24"><img src="https://avatars3.githubusercontent.com/u/60440835?v=4" width="100px;" alt=""/><br /><sub><b>parthkgh24</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=parthkgh24" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=parthkgh24" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Atharva-Gundawar"><img src="https://avatars0.githubusercontent.com/u/54273198?v=4" width="100px;" alt=""/><br /><sub><b>Atharva-Gundawar</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=Atharva-Gundawar" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=Atharva-Gundawar" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/SrishtiGohain"><img src="https://avatars2.githubusercontent.com/u/59062633?v=4" width="100px;" alt=""/><br /><sub><b>SrishtiGohain</b></sub></a><br /><a href="https://github.com/csivitu/ctf-challenges/commits?author=SrishtiGohain" title="Documentation">📖</a> <a href="https://github.com/csivitu/ctf-challenges/commits?author=SrishtiGohain" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!