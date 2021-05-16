import struct
import pprint


D_SIZE = 4 + 8 + 4 + 8 + 2 + 1 + 4 * 4
C_SIZE = 4 + 1 + 2 + 4 + 1 + D_SIZE
B_SIZE = C_SIZE + 4 + 1 * 8
A_SIZE = 8 + 4 + 4 + 1


def parse_d(offset, byteString):
    dBytes = byteString[offset:offset + D_SIZE]
    dParsed = struct.unpack('>fdiQhbffff', dBytes)
    return {'D1': dParsed[0],
            'D2': dParsed[1],
            'D3': dParsed[2],
            'D4': dParsed[3],
            'D5': dParsed[4],
            'D6': dParsed[5],
            'D7': dParsed[6],
            'D8': dParsed[7:]}


def parse_c(offset, byteString):
    c1234Bytes = byteString[offset:offset + 12]
    c1234Parsed = struct.unpack('>ibHIb', c1234Bytes)
    c3Bytes = byteString[c1234Parsed[3]:c1234Parsed[3] + c1234Parsed[2] * 2]
    c3Parsed = struct.unpack('H' * c1234Parsed[2], c3Bytes)
    c5Parsed = parse_d(offset + 12, byteString)
    return {'C1': c1234Parsed[0],
            'C2': c1234Parsed[1],
            'C3': list(c3Parsed),
            'C4': c1234Parsed[4],
            'C5': c5Parsed}


def parse_b(offset, byteString):
    b1Parsed = parse_c(offset, byteString)
    b23Bytes = byteString[offset + C_SIZE:offset + C_SIZE + 12]
    b23Parsed = struct.unpack('>ibbbbbbbb', b23Bytes)
    return {'B1': b1Parsed,
            'B2': b23Parsed[0],
            'B3': b23Parsed[1:]}


def parse_a(offset, byteString):
    aBytes = byteString[offset: offset + A_SIZE]
    aParsed = struct.unpack('>qIIb', aBytes)
    a2Bytes = byteString[aParsed[2]:aParsed[2] + aParsed[1] * 4]
    a2Parsed = struct.unpack('>' + 'I' * aParsed[1], a2Bytes)
    a2_list = [parse_b(addr, byteString) for addr in a2Parsed]
    return {'A1': aParsed[0],
            'A2': a2_list,
            'A3': aParsed[3]}


def f31(byteString):
    return parse_a(4, byteString)


# pprint.pprint(f31(b'ZFZe\xd4\x9dT\x03x\x90>\xd9\x00\x00\x00\x02\x00\x00\x00\xa7\x9f\xbb=\xdd'
# b'\xec\x01c\xd0dm\xc1\xf5\x00\x03\x00\x00\x00\x15\xd5\xbfO\xcc\x9b\xbf'
# b'\xd5\x86Z\xb3\xf6\x00\xac\xdf\x18R\xbez\x8c"|\xb5v\x1c=A\x11,\xbc\xef'
# b"\x8c\x1c\xbfQ\xe8!\xbf'Y/\xbfd\xab3#\xb6\xf8<\xb3\xd6N\xa2^\xc3\x94#\xb6\xaf"
# b'\xb6~(\x1f\x02\x7f\xaf3\x8c\x00\x03\x00\x00\x00^@\xbf\x08\xd9\x9c'
# b'\xbf\xe9\xdb\xb1\xbf\x81\xb8r\xa4bH\xb6\xd9I7\xc5\xf6\xea\xf0\x00s\x1b\xac>'
# b'\xe9\xcc\xb9\xbeJ;\x98?*\xb4\xf8?Y\xc5\x95\n\xee\x90KG\xc5\x01\xb2D'
# b'\x110\xb3\x00\x00\x00\x1b\x00\x00\x00d'))

# pprint.pprint(f31(b'ZFZe\xb5\xb7\\ d\xa5Z\xb1\x00\x00\x00\x02\x00\x00\x00\xb1\xb5\x81\xb5\xca'
# b'\x18\x10{Y\xed\x16\xd9M\xc7\x0b\xe7\xd1\x00\x05\x00\x00\x00\x15W\xbf'
# b"6\xb5\x1e?\xd7'\xe6\xe8\x19t\x84\x14\xb7\xf3\xf5\xf1\xa5\x11\x06\xda"
# b'\x17\xfa\x0e\x92K\xf5\xbe\xba[\xe1>0g"=\x89J\x8b\xbeTu\xf3\x9fT6rs\x0b'
# b'me\xa0\x01E_\xbb\xc0c\xd81-\xfe=\xd6\x9eb\xfdY\xf8\xeaZ\x04\x00'
# b'\x06\x00\x00\x00b\xbb>\xab\xce\x98\xbf\xd36\x9a\xb2\x0e\x17T\xc2\x9e'
# b'l\x1a\x03\xad\x8b\x8a\xe6\xbd\xe3\xa3\x88V(?\x1c&\xc1?\x1fY\xf2\xbf-!'
# b'\xce\xbe\xd1)\x86\xb7\x81\x15\x19X\x1b\xa8\xceR\x93 %\x00\x00\x00'
# b'\x1f\x00\x00\x00n'))