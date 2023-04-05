# Discord Markov chain

Make a markov chain out of yourself, using your data package!

## Instructions

First of all, rename your data package to `package.zip` if it isn't already called that.
Next, move it into `data/`

After that, you'll want to run `compile` and `make_markov_chain` using:
```sh
$ python compile.py
$ python make_markov_chain.py
```

Last of all, you'll want to run `generate_messages` and then tell it how many sentences you want, after which it will generate some.

```sh
$ python generate_messages.py
Reading Markov chain...
How many messages do you want to generate? 1
Generating sentences...
> i followed the same person
How many messages do you want to generate? 
```

This will loop on forever until you stop it using Ctrl-C

> **Note**: Next time you want to run it, you'll only have to run `generate_messages.py`
