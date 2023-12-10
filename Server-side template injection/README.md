# Server Site Template Injection
```

NOTE: This scrit solve all labs of Server Site Template Injetction on Port Swigger Academy.
```
Usage.

``` 
$ python3 ssti.py -h
    Usage:  ssti.py -h or --help

    ssti.py: error: the following arguments are required: -U/--url

    options:
      -h, --help            show this help message and exit
      -U URL, --url URL     URL (required)
      -u USERNAME, --username USERNAME
                            Username if required
      -p PASSWORD, --password PASSWORD
                            Password if required

Some script unable to fetch lab is solved or not.

```

Example:
1. If credentials are not required.
```
$ python3 ssti.py -U https://xxxxxxxxxxxxxxxxxxxxxxxxx.web-security-academy.net
```

2. If credentials are required.

```
$ python3 ssti.py -u user -p pass -U https://xxxxxxxxxxxxxxxxxxxxxxxxx.web-security-academy.net
```
