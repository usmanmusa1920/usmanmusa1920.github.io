# My Portfolio!

👋 🐦 💻 🔗 📫 🔭 🌱 👯 🤔 💬 😄 ⚡ 🛠️ 😼 🕵️ 🚗 ✨ 🚀 ✅ 🇳🇬

Personal <a href="https://usmanmusa1920.github.io">website</a> repositories <a href="https://github.com/usmanmusa1920/usmanmusa1920.github.io">github</a> & <a href="https://hub.docker.com/r/usmanmusa/usman-site">dockerhub</a> repo.

# Build image from source

First clone the git repository

```sh
git clone https://github.com/usmanmusa1920/usmanmusa1920.github.io
```

Change directory

```sh
cd usmanmusa1920.github.io
```

Change git branch

```sh
git checkout docker-container
```

Run the docker-compose command

```sh
docker-compose up --build
```

After the services comes up, visit the app on <a href="http://localhost:80">http://localhost:80</a> or <a href="http://localhost:88">http://localhost:88</a>

# Docker shell

You can run the container and access its shell using the `docker run` command with the `-it` (interactive + TTY) flag, and specify `/bin/sh` or `/bin/bash` as the shell (since Alpine-based images typically use `sh`):

```sh
docker run -it usmanmusa/usman-site /bin/sh

# or

docker run -it usmanmusa/usman-site sh
```
