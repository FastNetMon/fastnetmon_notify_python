#!/usr/bin/python3

import sys
import logging
import json
import pprint

logging.basicConfig(filename='/tmp/fastnetmon_notify_script.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

# We use modern logic which does not use command line argumetns and reads all information directly from stdin

# Read all data from stdin
stdin_data = sys.stdin.read()

# logging.info("We got following details: " + stdin_data)

parsed_details = json.loads(stdin_data)

# Uncoment to see all available data
# logging.info("Decoded details from JSON: " + pprint.pformat(parsed_details))

# Action could be: ban, unban, partial_block
action = parsed_details["action"]

# Can be empty, per_host or hostgroup
scope = parsed_details["alert_scope"]

if scope == "" or scope == "host":
    ip_address = parsed_details["ip"] 

    logging.info("Callback action " + action + " for host " + ip_address) 
elif scope == "hostgroup":
     hostgroup_name = parsed_details["hostgroup_name"]

     logging.info("Callback action " + action + " for hostgroup " + hostgroup_name)
else: 
    logging.info("Unknown scope " + scope)
