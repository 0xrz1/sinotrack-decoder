from decoder.crc import crc16_ccitt
from decoder.packets import decode_gps

def parse_packet(packet: bytes) -> dict:
    if packet[:2] not in (b'\x78\x78', b'\x79\x79'):
        raise ValueError("Invalid header")

    length = packet[2]
    protocol = packet[3]

    payload = packet[4:4+length-5]
    crc_recv = int.from_bytes(packet[-4:-2], 'big')
    crc_calc = crc16_ccitt(packet[2:-4])

    if crc_recv != crc_calc:
        raise ValueError("CRC mismatch")

    if protocol == 0x12:
        return {
            "type": "gps",
            "data": decode_gps(payload)
        }

    return {
        "type": "unknown",
        "protocol": hex(protocol)
    }
