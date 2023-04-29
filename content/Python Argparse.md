---
aliases: []
date created: Sep 4th, 2022
date modified: Oct 5th, 2022
---
- [argparse — Parser for command-line options, arguments and sub-commands — Python 3.10.6 documentation](https://docs.python.org/3/library/argparse.html)  
- [Argparse Tutorial — Python 3.10.7 documentation](https://docs.python.org/3/howto/argparse.html)

## Argparse

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("argumentName", help="display help msg", type=int) # no --
parser.add_argument("-v","--verbosity", help="increase output verbosity", action="store_true") # with --
args = parser.parse_args()

if args.argumentName:
	# do sth
elif args.verbosity:
	print("verbosity turned on")
```

- `action="store_true"` This means that, if the option is specified, assign the value `True` to `args.verbose`. Not specifying it implies `False`.
- `action="count"` to count the number of the argument. eg: `-vvv`, use with `default=0`

## Sub-command Parser
[argparse — Parser for command-line options, arguments and sub-commands — Python 3.10.6 documentation](https://docs.python.org/3/library/argparse.html#sub-commands)  
Many programs split up their functionality into a number of sub-commands, for example, the `svn` program can invoke sub-commands like `svn checkout`, `svn update`, and `svn commit`. Splitting up functionality this way can be a particularly good idea when a program performs several different functions which require different kinds of command-line arguments. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") supports the creation of such sub-commands with the [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers") method. The [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers") method is normally called with no arguments and returns a special action object. This object has a single method, `add_parser()`, which takes a command name and any [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor arguments, and returns an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") object that can be modified as usual.

- action
- dest
- help
- default
- nargs
