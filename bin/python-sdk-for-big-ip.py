#!/usr/bin/env python
#
"""
    python-sdk-for-big-ip.py

    Demonstration Python program which uses the F5 Python SDK to query, create and update LTM pool memebers.
    The credentials and address of the F5 BigIP are expected to be in a file called 'credentials.py' in the
    same directory as this program. This file can be edited to include one line in the form of:

    credentials = dict(hostname="vf5-mediawiki.sandbox.wwtatc.local", username="admin", password="redacted")
    
    Copyright (c) 2016 World Wide Technology, Inc.
    All rights reserved.

    Author: joel.king@wwt.com

    Revision history:
     5 October  2016  |  1.0 - initial release
    
    Adapted from: F5 Friday: Python SDK for BIG-IP
                  https://devcentral.f5.com/articles/f5-friday-python-sdk-for-big-ip-18233

"""
import requests
from f5.bigip import BigIP

class Connection(object):
    "Python class to manage the connection to the F5 BigIP and associated functions"

    def __init__(self, **kwargs):

        self.hostname = kwargs["hostname"]
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.bigip = None
        requests.packages.urllib3.disable_warnings()

    def login(self):
        "Connect to the BigIP"
        self.bigip = BigIP(self.hostname, self.username, self.password)
        return

    def get_pools(self):
        "get all the pools from the BigIP"
        return self.bigip.ltm.pools.get_collection()

    def get_members(self, pool):
        "get the members of a pool"
        return pool.members_s.get_collection()

    def create_new_pool(self, name='mypool', partition='Common'):
        "create a new pool on the BigIP"
        if self.bigip.ltm.pools.pool.exists(name=name, partition=partition):
            pool = self.bigip.ltm.pools.pool.load(name=name, partition=partition)
        else:
            pool = self.bigip.ltm.pools.pool.create(name=name, partition=partition)
        return pool

    def update_pool(self, name='mypool', partition='Common', description=""):
        "Update the pool description"
        pool = self.bigip.ltm.pools.pool.load(name=name, partition=partition)
        pool.description = description
        return pool.update()

    def delete_pool(self, name='mypool', partition='Common'):
        "Delete the pool if it exists"
        if self.bigip.ltm.pools.pool.exists(name=name, partition=partition):
            pool = self.bigip.ltm.pools.pool.load(name=name, partition=partition)
            return pool.delete()
        return None

def prompt(text):
    "prompting allows the user to view the changes on the F5 BigIP"
    return raw_input("%s, press return to continue." % text)


def main():
    "Sample code using the F5 BigIP SDK"
    try:
        import constants
        credentials = constants.credentials
    except:
        credentials = dict(hostname="192.0.2.1", username="admin", password="admin")
        

    big = Connection(**credentials)
    big.login()

    # Display the pools and members
    for pool in big.get_pools():
        print pool.name
        for member in big.get_members(pool):
            print "\t\t%s" % member.name

    # Create a pool, by not specifying a pool name or partition, we use the defaults
    # defined in the Connection class method.
    new_pool = big.create_new_pool()
    prompt("Created new pool: %s" % new_pool.name)

    # Update the pool we created, the parition isn't provided, use the value specified in the method
    big.update_pool(name=new_pool.name, description="Hello World")
    prompt("Added description to pool: %s" % new_pool.name)

    # Delete a pool logic, note the pool may or may not exist.
    big.delete_pool(name="foo")
    prompt("Attempted to delete pool 'foo'")

    big.delete_pool()
    prompt("Attempted to delete pool: %s" % new_pool.name)
    return

if __name__ == '__main__':
    main()
