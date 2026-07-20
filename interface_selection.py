from scapy.all import IFACES, get_if_addr


def get_available_interfaces():

    interfaces = []

    for interface in IFACES.values():

        try:
            interfaces.append({
                "name": interface.name,
                "description": interface.description
                if hasattr(interface, "description")
                else interface.name
            })

        except Exception:
            pass

    return interfaces


def display_interfaces():

    interfaces = get_available_interfaces()

    print("\nAvailable Network Interfaces")
    print("-" * 60)

    for index, interface in enumerate(interfaces, start=1):

        try:
            ip_address = get_if_addr(interface["name"])
        except Exception:
            ip_address = "Unavailable"

        print(f"{index:>2}. {interface['description']}")
        print(f"    IP Address : {ip_address}")
        print()

    return interfaces


def select_interface():

    interfaces = display_interfaces()

    while True:

        try:

            choice = int(input("Select Interface Number : "))

            if 1 <= choice <= len(interfaces):

                selected = interfaces[choice - 1]

                print(f"\nSelected Interface : {selected['description']}")

                return selected["name"]

            print("Invalid selection. Please choose a valid number.")

        except ValueError:

            print("Please enter a numeric value.")