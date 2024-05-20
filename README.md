# League of Legends Worlds 2024 Finals Ticket Notifier

This script will run every minute and check if the button has the text "On sale TBA". A Home Assistant Notification will be send if not.

## Getting Started

```sh
pip install -r requirements.txt
python ./main.py
```

## Docker

```sh
docker buildx build --platform linux/amd64 -t glup3/lol2024-notifier:latest-amd64 .
docker push glup3/lol2024-notifier:latest-amd64

# troubleshoot - check for "Architecture"
docker image inspect glup3/lol2024-notifier:latest-amd64
```

## Note

You need to build for AMD64 since my Synology NAS requires AMD64 build. `docker-compose.yml` is for local building.
