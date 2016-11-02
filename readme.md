# MagicMirror Display Controller

A small python script that controls the display of a MagicMirror independent from the MagicMirror application. It turns off the display when a given amount of time has elapsed after the last motion recognition.

Basically it can control any display connected to a Raspberry Pi which has Raspbian installed.

I added a `systemd` service file to use it as `systemd` service and start it at boot time.

## Installation

Clone the repository to wherever you want:

`git clone https://github.com/deg0nz/MagicMirror-Display-Controller`

If you want it started as a `systemd` service, you have to copy the `.service` file to `/lib/systemd/system` and reload the `systemd` daemons.

Here's an example of the commands needed:

```
# cp ./pir_sensor.service /lib/systemd/system
# systemctl daemon-reload
# systemctl start pir_sensor.service
```

You have to change line 7 to the location of the `pir.py` file like this:

`ExecStart=/usr/bin/python /path/to/your/pir.py`

Line 7 defaults to `/home/pi/pir.py`. So if you put the `pir.py` there, you doun't have to change anything.


## Configuration

You can configure the amount of the countdown time via the `timeUntilDisplayOff` variable. The value is given in seconds. 

The `pin` variable should be set to the connected data pin of the PIR sensor. Default is `14`.

## License

MIT
