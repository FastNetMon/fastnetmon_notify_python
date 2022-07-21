#!/usr/bin/python3

import sys
import logging
import json
import pprint

logging.basicConfig(filename='/tmp/fastnetmon_notify_script.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

if len(sys.argv) != 3:
    logging.error("Please provide two arguments for script: action and IP address")
    sys.exit(1)

# Action could be: ban, unban, partial_block
action = sys.argv[1]
ip_address = sys.argv[2]

logging.info("Start for action %s and IP %s" % (action, ip_address))

# Read all data from stdin
stdin_data = sys.stdin.read()

logging.info("We got following details: " + stdin_data)

parsed_details = json.loads(stdin_data)

logging.info("Decoded details from JSON: " + pprint.pformat(parsed_details))

# You can use attack details in this form:
# logging.info("Attack direction: " + parsed_details['attack_details']['attack_direction'])
