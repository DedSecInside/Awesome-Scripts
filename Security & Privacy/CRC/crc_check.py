import argparse
from PyCRC.CRC16 import CRC16
from PyCRC.CRC16DNP import CRC16DNP
from PyCRC.CRC16Kermit import CRC16Kermit
from PyCRC.CRC16SICK import CRC16SICK
from PyCRC.CRC32 import CRC32
from PyCRC.CRCCCITT import CRCCCITT


parser = argparse.ArgumentParser(description="chose crc method")
parser.add_argument('crc_type', metavar="type", type=str, help="Chose crc  method: crc16, crc16dnp, crc16kermit, crc16sick, crc32, crcccitt")
parser.add_argument('data_to_generate_crc', metavar="data", type=str, help="Enter data to preform checksum")
parser.add_argument('--compare', nargs='?', help='use to compare with given crc')
args = parser.parse_args()

if __name__ == "__main__":
    data = args.data_to_generate_crc    
    
    if args.crc_type == 'crc16':
        calculated_crc = CRC16().calculate(data)
        print("CRC : ", calculated_crc)

    elif args.crc_type == 'crc16dnp':
        calculated_crc = CRC16DNP().calculate(data)
        print("CRC : ", calculated_crc)

    elif args.crc_type == 'crc16kermit':
        calculated_crc = CRC16Kermit().calculate(data)
        print("CRC : ", calculated_crc)

    elif args.crc_type == 'crc16sick':
        calculated_crc = CRC16SICK().calculate(data)
        print("CRC : ", calculated_crc)

    elif args.crc_type == 'crc32':
        calculated_crc = CRC32().calculate(data)
        print("CRC : ", calculated_crc)

    elif args.crc_type == 'crcccitt':
        calculated_crc = CRCCCITT().calculate(data)
        print("CRC : ", calculated_crc)
        
    if args.compare:
        if int(args.compare) == int(calculated_crc):
            print('Crc are the same!')
        else:
            print('Crc are not matching!')
