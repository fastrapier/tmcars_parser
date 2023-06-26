from parser import Parser

if __name__ == '__main__':
    parser = Parser('iphone 11')

    parser.parse()

    parser.serialize_into_csv()
