# UDP Logger

This script listens for UDP packets on a specified port and processes the incoming data. It is designed to accept data from Shelly UDP logging.

## Usage

To run the script, use the following command:

```sh
./udp_listener.py <port>
```

Replace `<port>` with the port number you want to listen on.

## Features

- Listens for UDP packets on both IPv4 and IPv6.
- Replaces null bytes in the received data with newlines.
- Ensures the packet is terminated by a single newline.
- Outputs the processed data to stdout.

## Example

```sh
./udp_listener.py 12345
```

This will start the script and listen for UDP packets on port 12345.

## Requirements

- Python 3.x

# shelly-log

The `shelly-log` script allows you to log UDP packets to a file with timestamps.

## Usage

To run the script, use the following command:

```sh
./shelly-log <port> <file>
```

Replace `<port>` with the port number you want to listen on and `<file>` with the log file path.

## Example

```sh
./shelly-log 12345 /path/to/logfile
```

This will start the script, listen for UDP packets on port 12345, and log the packets to the specified file with timestamps.

## Requirements

- `ts` from the `moreutils` package
- `rotatelogs` from the `apache2-utils` package


# License

This project is licensed under the MIT License.