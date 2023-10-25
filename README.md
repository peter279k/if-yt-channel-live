# if-yt-channel-live

## Introduction

- We use the IFTTT service to notify specific YouTube channel is live when running the `yt.py`.

## Usage

- Cloning the repository via the `git clone` command.
- Using the `pipenv` to install dependencies.
- Preparing the `.env` file and sample contents are as follows:

```
ifttt_service_url=your requested IFTTT webhook event service URL
channel_name=The specific YouTube channel name
```

- It suggests that using the `cronjob` setting to let `yt.py` run as the scheduler.

## References

- Thanks for the [reposeitory](https://github.com/bogeta11040/if-youtube-channel-live) to let me figure out this project :).
