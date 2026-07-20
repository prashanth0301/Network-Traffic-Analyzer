from scapy.all import sniff
def start_packet_capture(
    interface,
    packet_handler,
    packet_limit=0,
    capture_filter=None
):

    print("\nStarting packet capture...")
    print(f"Interface      : {interface}")

    if capture_filter:
        print(f"Filter         : {capture_filter.upper()}")
    else:
        print("Filter         : ALL")

    if packet_limit == 0:
        print("Packet Limit   : Unlimited")
    else:
        print(f"Packet Limit   : {packet_limit}")

    print("Press CTRL + C to stop.\n")

    try:

        sniff(
            iface=interface,
            prn=packet_handler,
            store=False,
            count=packet_limit,
            filter=capture_filter
        )

    except KeyboardInterrupt:

        print("\nPacket capture stopped by user.")

    except PermissionError:

        print("\nPermission denied.")
        print("Run the program as Administrator.")

    except Exception as error:

        print(f"\nCapture Error : {error}")