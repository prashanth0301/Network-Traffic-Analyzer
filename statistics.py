from collections import Counter
import time


class TrafficStatistics:

    def __init__(self):

        self.start_time = time.time()

        self.total_packets = 0
        self.total_bytes = 0

        self.protocol_counter = Counter()
        self.source_ip_counter = Counter()
        self.destination_ip_counter = Counter()

        self.live_summary_interval = 50

    def update(self, packet_info):

        self.total_packets += 1
        self.total_bytes += packet_info["packet_size"]

        self.protocol_counter[packet_info["protocol"]] += 1
        self.source_ip_counter[packet_info["source_ip"]] += 1
        self.destination_ip_counter[packet_info["destination_ip"]] += 1

        if self.total_packets % self.live_summary_interval == 0:
            self.print_live_statistics()

    def print_live_statistics(self):

        print("\n")

        print("=" * 45)
        print("LIVE STATISTICS")
        print("=" * 45)

        print(f"Packets : {self.total_packets}")
        print(f"Bytes   : {self.total_bytes}")

        print("\nProtocols")

        for protocol, count in self.protocol_counter.items():
            print(f"{protocol:<10}{count}")

        print("=" * 45)

    def get_capture_duration(self):

        return time.time() - self.start_time

    def get_average_packet_size(self):

        if self.total_packets == 0:
            return 0

        return self.total_bytes / self.total_packets

    def get_top_source_ips(self, limit=5):

        return self.source_ip_counter.most_common(limit)

    def get_top_destination_ips(self, limit=5):

        return self.destination_ip_counter.most_common(limit)

    def get_protocol_distribution(self):

        return dict(self.protocol_counter)

    def get_summary(self):

        return {
            "total_packets": self.total_packets,
            "total_bytes": self.total_bytes,
            "capture_duration": round(
                self.get_capture_duration(), 2
            ),
            "average_packet_size": round(
                self.get_average_packet_size(), 2
            ),
            "protocol_distribution":
                self.get_protocol_distribution(),
            "top_source_ips":
                self.get_top_source_ips(),
            "top_destination_ips":
                self.get_top_destination_ips()
        }