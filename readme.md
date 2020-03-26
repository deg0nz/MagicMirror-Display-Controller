# MagicMirror Display Controller

A small python script that controls the display of a [MagicMirror](https://github.com/MichMich/MagicMirror) independent from the MagicMirror application. It turns off the display when a given amount of time has elapsed after the last motion has been recognized.

Basically it can control any display connected to a Raspberry Pi which has Raspbian installed.

I added a `systemd` service file to use it as `systemd` service and start it at boot time.

## Installation

Clone the repository to wherever you want:

`git clone https://github.com/deg0nz/MagicMirror-Display-Controller`

If you want it started as a `systemd` service, you have to copy the `.service` file to `/lib/systemd/system` and reload the `systemd` daemons.

Here's an example of the commands needed (cwd is the repository):

```
# cp ./pir_sensor.service /lib/systemd/system
# systemctl daemon-reload
# systemctl start pir_sensor.service
```

If you cloned the repository somewhere else than your home directory, you have to change line 7 to the location of the `pir.py` file like this:

`ExecStart=/usr/bin/python -u /path/to/pir.py`

Line 7 defaults to `/home/pi/MagicMirror-Display-Controller/pir.py`. So if you cloned the repository to your home folder, you don't have to change anything.


## Logs

You can see the logs with `journalctl -u pir_sensor.service`

## Configuration

You can configure the amount of the countdown time via the `timeUntilDisplayOff` variable. The value is given in seconds. 

The `pin` variable should be set to the connected data pin of the PIR sensor. Default is `14`.

## License

The MIT License (MIT)   
Copyright (c) 2016 Benjamin Gericke

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
