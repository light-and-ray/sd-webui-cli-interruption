## cli-interruption

Sets interrupt generation flag on `KeyboardInterrupt` (Ctrl+C) for [sd-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), instead of closing the server. Can be useful for people who are used to interrupt via command-line, and for extensions which doesn't have interruption button inside ui, but use stable diffusion pipeline

```log
INFO:modules.shared_state:Starting job task(xjhhoo54s2mwdp1)
  6%|▋         | 3/48 [00:03<00:44,  1.02it/s]^C
Caught KeyboardInterrupt, interrupting generation...
```

It still closes the server if there's no generation in process or crtl-c is pressed two times
