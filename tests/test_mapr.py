'''
    Test for Mapr
'''
from rat_utils.mapr import perform_map, mapr

SAMPLE_MAPPER = {
    "legal_name": "name.first_name",
    "passport_number": "id",
    "address": "home.apt"
}
SAMPLE_DATA = [
    {
        "name": {
            "first_name": "Roshan",
            "last_name": "Thaliath"
        },
        "id": 12314,
        "home": {
            "apt": 42,
            "road": "Wallaby Way",
            "city": "Sydney"
        }
    },
    {
        "name": {
            "first_name": "Tarun",
            "last_name": "Thaliath"
        },
        "id": 12314,
        "home": "44 Wallaby Way"
    },
    {
        "home": "argentina",
        "usbek": False
    }
]

TEST_DATA = {
    1: {
        "data": {
            "name": "Roshan",
            "id": 12314,
            "home": {
                "apt": 42,
                "road": "Wallaby Way",
                "city": "Sydney"
            }
        },
        "mapper": {
            "target_name": "name",
            "target_id": "id"
        },
        "result": {
            "target_name": "Roshan",
            "target_id": 12314
        }
    },
    2: {
        "data": {
            "name": "Roshan",
            "id": 12314,
            "home": {
                "apt": 42,
                "road": "Wallaby Way",
                "city": "Sydney"
            }
        },
        "mapper": {
            "target_apt": "home.apt",
            "target_road": "home.road",
            "target_city": "home.city"
        },
        "result": {
            "target_apt": 42,
            "target_road": "Wallaby Way",
            "target_city": "Sydney"
        }
    },
    3: {
        "data": {
            "name": "Roshan",
            "id": 12314,
            "home": {
                "apt": 42,
                "road": "Wallaby Way",
                "city": "Sydney"
            }
        },
        "mapper": {
            "ssn_number": "ssn_id"
        },
        "result": {
            "ssn_number": None
        }
    },
    4: {
        "data": [
            {
                "name": {
                    "first_name": "Roshan",
                    "last_name": "Thaliath"
                },
                "address": 42,
                "ssn_id": 123
            },
            {
                "name": {
                    "first_name": "Bob",
                    "last_name": "Dylan"
                },
                "ssn_id": 45
            }
        ],
        "mapper": {
            "first_name": "name.first_name",
            "address": "address",
            "ssn_id": "ssn_id"
        },
        "result": [
            {
                "first_name": "Roshan",
                "address": 42,
                "ssn_id": 123
            },
            {
                "first_name": "Bob",
                "address": None,
                "ssn_id": 45
            }
        ]
    }
}


def test_perform_map_single_target():
    '''
        Test if perform_map can handle inputs without nesting 
    '''
    test_data = TEST_DATA[1]

    result = perform_map(
        row=test_data['data'],
        mapper=test_data['mapper']
    )

    assert result == test_data['result']


def test_perform_map_nested_target():
    '''
        Test if perform_map can handle inputs with nesting
    '''
    test_data = TEST_DATA[2]
    result = perform_map(
        row=test_data['data'],
        mapper=test_data['mapper']
    )

    assert result == test_data['result']


def test_perform_map_missing_target():
    '''
        Test if perform_map can handle inputs that don't have the target property
    '''
    test_data = TEST_DATA[3]
    result = perform_map(
        row=test_data['data'],
        mapper=test_data['mapper']
    )

    assert result == test_data['result']


def test_mapr_e2e():
    '''
        Test the exported mapr function
    '''
    test_data = TEST_DATA[4]
    result = mapr(
        data=test_data['data'],
        mapper=test_data['mapper']
    )

    assert result == test_data['result']
