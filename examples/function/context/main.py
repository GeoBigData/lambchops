import json

import ais


def lambda_handler(event, _):
    print(json.dumps(event, indent=4))
    print('Imported ais package')

    return True
