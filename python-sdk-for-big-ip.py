#!/usr/bin/env python
#
# F5 Friday: Python SDK for BIG-IP
#            https://devcentral.f5.com/articles/f5-friday-python-sdk-for-big-ip-18233
#
import sys
from f5.bigip import BigIP

# Connect to the BigIP
# bigip = BigIP("bigip.example.com", "admin", "somepassword")
bigip = BigIP("sys.argv[1]", sys.argv[2], sys.argv[3])

# Get a list of all pools on the BigIP and print their name and their
# members' name
pools = bigip.ltm.pools.get_collection()
for pool in pools:
    print pool.name
    for member in pool.members:
        print member.name

# Create a new pool on the BigIP
mypool = bigip.ltm.pools.pool.create(name='mypool', partition='Common')

# Load an existing pool and update its description
pool_a = bigip.ltm.pools.pool.load(name='mypool', partition='Common')
pool_a.description = "New description"
pool_a.update()

# Delete a pool if it exists
if bigip.ltm.pools.pool.exists(name='mypool', partition='Common'):
    pool_b = bigip.ltm.pools.pool.load(name='oldpool', partition='Common')
    pool_b.delete()
