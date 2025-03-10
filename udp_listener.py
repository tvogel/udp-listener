#!/usr/bin/env python3

import socket
import sys
import select

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)

    port = int(sys.argv[1])

    # Create a UDP socket for IPv4
    sock_ipv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_ipv4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_ipv4.bind(('0.0.0.0', port))

    # Create a UDP socket for IPv6
    sock_ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock_ipv6.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_ipv6.bind(('::', port))

    # Write the "Listening" message to stderr
    print(f"Listening for UDP packets on port {port}...", file=sys.stderr)

    while True:
        try:
            ready_socks, _, _ = select.select([sock_ipv4, sock_ipv6], [], [])
            for sock in ready_socks:
                data, addr = sock.recvfrom(4096)
                print(f"Received packet from {addr}", file=sys.stderr)
                # Replace null bytes with newlines
                data = data.replace(b'\x00', b'\n')
                # Ensure the packet is terminated by a single newline
                if not data.endswith(b'\n'):
                    data += b'\n'
                # Write the processed packet to stdout
                sys.stdout.buffer.write(data)
                sys.stdout.flush()
        except Exception as e:
            print(f"Error receiving packet: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
