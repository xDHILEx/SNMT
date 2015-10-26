# Simple Network Monitoring Tool

SNMT is a simple network monit ... hmm

##### Files:
`SNMT.py`: Makes use of `mtr` and `awk` to return alert messages.

`mail.py`: Can be used in conjunction with `SNMT.py` to email said alert messages.

`config.ini`: Where all the magic happens.


##### Installation:

```sh
$ git clone https://github.com/xDHILEx/SNMT.git SNMT
```
###### or

[Download ZIP] [zip]

##### Use:
```sh
$ cd SNMT
$ vim config.ini (I\'m kidding, use whatever you want)
    - Make the magic happen -
$ python SNMT.py
    - or -
$ python mail.py
```


   [zip]: <https://github.com/xDHILEx/SNMT/archive/master.zip>
