'''
    Module for Mapping
    Author: Roshan Thaliath
    Date: December 2022
'''


def perform_map(row: dict, mapper: dict) -> dict:
    '''
        Perform the map operation using the given mapper
    '''
    mapped_row = {}
    for key, value in mapper.items():
        prop_list = value.split('.')

        iter_obj: dict = {}

        for iter_prop in prop_list:
            if not iter_obj:
                if iter_prop not in row:
                    iter_obj = None
                else:
                    iter_obj = row[iter_prop]
            else:
                iter_obj = iter_obj[iter_prop]

        mapped_row[key] = iter_obj

    return mapped_row


def mapr(data: list[dict], mapper: dict) -> list[dict]:
    '''
        Main function that is either exported or run via command line
    '''
    output_data = [perform_map(row, mapper) for row in data]
    return output_data


def parse_args():
    '''
        Parse Command Line Arguments
    '''
    return {}


if __name__ == '__main__':
    args = parse_args()
    mapr(**args)
