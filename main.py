from decoder.parser import parse_packet

hex_packet = (
    "78781F12170C0A0B2D"
    "C3A2B14F"
    "8E4D2A90"
    "3201A6"
    "0001"
    "ABCD"
    "0D0A"
)

packet = bytes.fromhex(hex_packet)

decoded = parse_packet(packet)
print(decoded)
