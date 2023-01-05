# Easy Pomodoro CLI

<img src="src/media/images/pomodoro_logo.jpeg" alt="Image of clock by Picasso" width="200"/>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Test](#test)

## About <a name = "about"></a>

Small CLI application that implements the Pomodoro routine

## Getting Started <a name = "getting_started"></a>

The default pomodoros are 4 with a time range of 20 minutes each one.
After countdown there will be a chill out time to relax.

To install from PyPI

```
pip install epomodoro
```

To install manually cloning the repository

```
pip install --editable .
```

## Usage <a name = "usage"></a>

```
epomodoro start
```

Change default parameters

```
epomodoro start --length 20 --pomodoros 2 --chill 10
```

```
epomodoro start -l 20 -p 2 -c 10
```

<img src="src/media/images/example.png" alt="Execution example" width="275"/>

You can get the statistics of your pomodoros from last week if there is data

```
epomodoro statistic
```

<img src="src/media/images/example_statistic.png" alt="Execution statistic" width="275"/>

To clean the data store in ` ~/.config/epomodoro`

```
epomodoro clean
```

## Autocomplete for CLI

To add autocomplete in Bash shell

```
_EPOMODORO_COMPLETE=bash_source epomodoro > ~/.epomodoro-complete.bash
. ~/.epomodoro-complete.bash

```

To add autocomplete to CLI when press Tab for ZSH shell

```
_EPOMODORO_COMPLETE=zsh_source epomodoro > ~/.epomodoro-complete.zsh
. ~/.epomodoro-complete.zsh
```

## Test <a name= "test"></a>

See Makefile definition

To run test

```
make test
```
