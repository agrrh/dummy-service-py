# Info

This is a dummy python service which listens on `0.0.0.0:80` and answers with following JSON structure:

```
{
    "hostname": "your-hostname-here", 
    "uuid": "random-uuid-here"
}
```

# Usage

Good idea to run container with ramfs mounted to `/tmp` to speed things up:

```
docker run ... \
  --tmpfs /tmp:rw,noexec,nosuid,size=65536k \
  ...
```

