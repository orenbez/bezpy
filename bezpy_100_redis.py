# Redis (REmote DIctionary Server) is a NoSQL, In-Memory db (stores the data in RAM).  Only uses disk for persistence
# Alternative to 'Memcached'
# Redis can be used as a message broker
# Stores all data as key-value strings
# https://realpython.com/python-redis/
# https://redis.io/commands/
# https://www.w3resource.com/redis/


# ======================================================================================================================
# For Windows: https://www.youtube.com/watch?v=188Fy-oCw4w
# ======================================================================================================================
# 1. got to https://github.com/MicrosoftArchive/redis/releases
# 2. download the latest .zip file
# 3. extract to C:\redis\Redis-x64-<version>\
# 4. main files are C:\redis\Redis-x64-3.0.504\redis-server.exe,  C:\redis\Redis-x64-3.0.504\redis-cli.exe
# 5. double-click on redis-server.exe to start the server, default Port is set to  6379 (WINDOWS)
# 6. double-click on redis-cli.exe to start the client on the local server (WINDOWS)

# Notes: 
# if you use the .msi installer then the redis-server will be always running in the background
# modify redis.windows.conf to change the port or set a password for access (on unix, redis.conf)
# to start server with config $> redis-server redis.windows.conf
# to enter a password to access the db  enter `AUTH <password>` in cli
# Use ACL (Access Control List) commands to set users/roles  see https://redis.io/commands/acl-setuser/
# redis is single threaded so some of the commands are very costly and can block the system
# persist data to RDB (snapshot file - good for backups OR AOF=Append Only File) with 'SAVE' command (not PERSIST command)
# see redis.conf file which has a line  "dbfilename dump.rdb"

# redis-cli --help                                    
# redis-cli -h x.x.x.x   -p 6379 -a <passwd>      # enter in command line to start client (LINUX)  -- can authenticate after entering cli with `AUTH <passwd>`
# redis-cli -h 127.0.0.1 -p 6379 -a <passwd>      # enter in command line to start client (LINUX)  -- for server running on local host
# redis-cli -u redis://user:password@host:port    # enter in command line to start client (LINUX)
# redis-cli -u redis://password@host:port         # enter in command line to start client (LINUX)   -- NO USER HAS BEEN ADDED 
# redis-cli -u redis://host:port -a <passwd>      # enter in command line to start client (LINUX)   -- SAME AS ABOVE

# ======================================================================================================================
# Redis Commands:
# ======================================================================================================================
# Sets:     SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, 
#           SSCAN, SUNION, SUNIONSTORE

# Hashes:   HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HLEN, HMGET, HMSET, HSCAN, HSET, HSETNX, 
#           HSTRLEN, HVALS

# Lists:    BLPOP, BRPOP, BRPOPLPUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSH, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, 
#           RPOPLPUSH, RPUSH, RPUSHX, 

# Strings:  APPEND, BITCOUNT, BITFIELD, BITOP, BITPOS, DECR, DECRBY, GET, GETBIT, GETRANGE, GETSET, INCR, INCRBY, 
#           INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN

# General:  KEYS, INFO, PING, QUIT, CLEAR, FLUSHALL, FLUSHDB, SAVE, BGSAVE, LASTSAVE, DEL, SCAN
# ======================================================================================================================

# A redis key is any binary string up to 512 MB

# ======================================================================================================================
# Strings {key: str}
# ======================================================================================================================
# 127.0.0.1:6379> SET name fred                  # returns OK, sets key-value pair   keys/values are case-sensitive
# 127.0.0.1:6379> MSET color1 red color2 green   # returns OK, sets multiple key-value pairs
# 127.0.0.1:6379> GET name                       # returns "Fred", note GET only works for type string
# 127.0.0.1:6379> MGET color1 color2             # returns values for both of the keys
# 127.0.0.1:6379> EXISTS name                    # returns 1, for true
# 127.0.0.1:6379> TTL name                       # returns time to live (expiration time in secs, default is -1 meaning no expiration)
# 127.0.0.1:6379> PTTL name                      # returns time to live (expiration time in mili-secs, default is -1 meaning no expiration)
# 127.0.0.1:6379> EXPIRE name 10                 # name will expire in 10 secs
# 127.0.0.1:6379> PEXPIRE name 10                # name will expire in 10 mili-secs
# 127.0.0.1:6379> SETEX name2 10 david           # Sets key:value pair with TTL=10 secs to expire
# 127.0.0.1:6379> PERSIST name2                  # removes any expiration
# 127.0.0.1:6379> GET name2                      # returns (nil) - after 10 secs have passed
# 127.0.0.1:6379> DEL name                       # returns OK, key deleted  (python equivalent for redis is r.delete('name') - see below)
# 127.0.0.1:6379> SET 192.168.1.1 1              # sets key "192.168.1.1" to  "1"
# 127.0.0.1:6379> INCRBY 192.168.1.1 1           # Increments value by 1 to "2"  (works for values that are represented as integers)
# 127.0.0.1:6379> DECRBY 192.168.1.1 1           # Increments value by 1 to "2"
# 127.0.0.1:6379> SET david:score 3.7            # sets key b'david:score' to b'3.7'
# 127.0.0.1:6379> INCRBYFLOAT david:score 2.9    # increments by float to value b'6.6'

# ======================================================================================================================
# Lists {key: List[str]}
# ======================================================================================================================
# 127.0.0.1:6379> LPUSH friends sally david      # Creates key:list with adding new values to the left and returns total 'friends' count
# 127.0.0.1:6379> RPUSH friends andy             # appends friend to list from the right and returns total 'friends' count
# 127.0.0.1:6379> LRANGE friends 0 -1            # returns list from 0th to last term ...  1) "david"  2) "sally"  3) "andy"
# 127.0.0.1:6379> LLEN friends                   # returns lenght of list
# 127.0.0.1:6379> LPOP friends                   # Removes a friend from left and returns it
# 127.0.0.1:6379> RPOP friends                   # Removes a friend from right and returns it
# 127.0.0.1:6379> DEL friends                    # Removes entire list

# ======================================================================================================================
# Sets {key: set}
# ======================================================================================================================
# 127.0.0.1:6379> SADD hobbies running "weight lifting" swimming  # Creates a Set of 'hobbies'
# 127.0.0.1:6379> SMEMBERS hobbies                                # returns all members of set ... 1) "swimming" 2) "weight lifting" 3) "running"
# 127.0.0.1:6379> SCARD hobbies                                   # returns number of elements of set (integer) 3
# 127.0.0.1:6379> SREM hobbies swimming                           # Removes item from set
# 127.0.0.1:6379> DEL hobbies                                     # Removes entire
# 127.0.0.1:6379> SADD hobbies2 motorcycling swimming             # Creates a new Set of 'hobbies'
# 127.0.0.1:6379> SINTER hobbies hobbies2                         # Intersection of sets
# 127.0.0.1:6379> SDIFF  hobbies hobbies2                         # Set difference
# 127.0.0.1:6379> SUNION  hobbies hobbies2                        # Set Union

# ======================================================================================================================
# Hashes (nested keys) {key: dict}
# ======================================================================================================================
# 127.0.0.1:6379> HSET person name dave                      # Sets key:value pair "name"="dave"
# 127.0.0.1:6379> HSET person age 25                         # Sets "age"="25"
# 127.0.0.1:6379> HINCRBY person age 1                       # Sets "age"="26"  (increase by 1)
# 127.0.0.1:6379> HMSET person color brown height "5 ft 7"   # sets multiple key: values for 'person'  (NOT AVAILABE WITH PYTHON - DEPRICATED)
# 127.0.0.1:6379> HGET person age                            # returns person.age="26"
# 127.0.0.1:6379> HLEN person                                # returns number of keys for person
# 127.0.0.1:6379> HKEYS person                               # returns all keys for 'person'
# 127.0.0.1:6379> HVALS person                               # returns all values for 'person'
# 127.0.0.1:6379> HGETALL person                             # returns all key/values for 'person'
# 127.0.0.1:6379> HEXISTS person name                        # returns 1 for true
# 127.0.0.1:6379> HDEL person age                            # deletes age from person
# 127.0.0.1:6379> DEL person                                 # deletes entire dictionary

# ======================================================================================================================
# General:
# ======================================================================================================================
# 127.0.0.1:6379> AUTH foo          # enter password 'foo' for authentication this will match 'requirepass foo' on the redis conf file
# 127.0.0.1:6379> AUTH usr pass     # enter your password for specified user (if users have been added to ACL)
# 127.0.0.1:6379> ACL LIST          # list roles/users
# 127.0.0.1:6379> PING              # returns PONG, this means client is working
# 127.0.0.1:6379> INFO              # returns useful info e.g. number of keys in the 'Keyspace' section at bottom
# 127.0.0.1:6379> INFO Keyspace     # returns Keyspace info only which will list all the databases
                                    # Keyspace
                                    # db0:keys=10,expires=0
                                    # db1:keys=1,expires=0
                                    # db3:keys=1,expires=0

# 127.0.0.1:6379> KEYS *                        # returns all keys matching wild card of all types strings/lists/sets/hashes
# 127.0.0.1:6379> KEYS 'xxx"xxx'                # returns all keys matching xxx"xxx
# 127.0.0.1:6379> KEYS na??                     # returns "name"
# 127.0.0.1:6379> TYPE person                   # returns hash, the variable type i.e. one of {hash, sets, lists, string}
# 127.0.0.1:6379> RANDOMKEY                     # returns a random key from the database
# 127.0.0.1:6379> RENAME oldkey newkey          # renames the key

# Note that 'KEYS' is a 'dangerous' command as it can block the server, better to use 'SCAN' in production
# 127.0.0.1:6379> SCAN <cursor> [MATCH <pattern>] [COUNT <count>]   # uses less resources than the KEYS command, 
#                                                                   # can return 'COUNT' number of keys (default is COUNT=9 returning 8 keys), 
#                                                                   # and a <cursor> value,  examples below
# 127.0.0.1:6379> SCAN 0 COUNT 5                # returns 4 keys using cursor=0  will return a cursor number eg 22
# 127.0.0.1:6379> SCAN 22 COUNT 5               # returns another 4 keys using cursor=22 ,  if you are returned cursor=0 then you've reached the end of the keys

# By default there are 16 databases (indexed from 0 to 15).
# 127.0.0.1:6379> SELECT 1                    # switch to db1 , default is db0
# 127.0.0.1:6379[1]> SET language python      # commands will now operate on db1
# 127.0.0.1:6379[1]> SETNAME <a-unique-name>  # to set a unique name for the current connection.
# 127.0.0.1:6379[1]> CLIENT LIST              # to get info of all clients that connecting to Redis.
# 127.0.0.1:6379[1]> CLIENT INFO  # Since Redis 6.2.0,  to get the information of current connection.


# 127.0.0.1:6379> SAVE                         # save is synchronous and will have blocking. creates dump.rdb file
# 127.0.0.1:6379> BGSAVE                       # background save is asynchronous, with no blocking. - saves to dump.rdb
# 127.0.0.1:6379> LASTSAVE                     # returns integer representing time last saved
# 127.0.0.1:6379> FLUSHDB                      # deletes all keys in your current db,
# 127.0.0.1:6379> FLUSHALL                     # deletes all keys in all dbs
# 127.0.0.1:6379> CLEAR                        # will clear the screen
# 127.0.0.1:6379> QUIT                         # exit client
# 127.0.0.1:6379> CONFIG GET port              # returns the port number from the .conf file or the default configuration
# 127.0.0.1:6379> CONFIG GET requirepass       # returns password from redis.conf if a password is required to authenticate
# 127.0.0.1:6379> CONFIG GET protection-mode   # returns 'yes'  or 'no' when protected external clients are blocked unless white-listed with 'bind'
# 127.0.0.1:6379> CONFIG SET <...>             # set config value dynamically
# 127.0.0.1:6379> CONFIG REWRITE               # rewrites the redis.conf file which was used to starting the server
# 127.0.0.1:6379> SHUTDOWN                     # shuts down server from the client

# ======================================================================================================================
# PUBSUB COMMANDS ...  watch https://youtu.be/KIFA_fFzSbo?si=eAKC3pm4lEx4UGbq
# ======================================================================================================================
# syncronous communication - publisher / subscriber must be connected at the same time.  Missed messages will not be delivered to the subscriber
# fire & forget - publisher does not receive acknowledgement of delivery. Simply broadcasts the message.
# fan-out only - delivers to all active subscribers irrespective if they need that paticular message
#
# # You don't need to create a channel.  Any client can publish to a channel any client can subscribe to a client even if it hasn't existed yet
# # So you can subscribe to a channel that has not been used yet
#
# 127.0.0.1:6379> SUBSCRIBE  channel_1 channel_2    # returns number of channels you've subscribed to - and enters listening mode
# 127.0.0.1:6379> PSUBSCRIBE  *_chat                # subscribe with pattern match, returns number of channels you've subscribed to - and enters listenting mode
#
# on a seperate command line
# 127.0.0.1:6379> PUBLISH channel_2 "here is my message"     # returns 1 if any subscriber exists online, else 0. Message displayed on the listening screen


# 127.0.0.1:6379> UNSUBSCRIBE <channel-name>                 # Not sure how to operate as subscribers are listening and do not have a commmand prompt
# 127.0.0.1:6379> PUNSUBSCRIBE <channel-name-pattern>        # Not sure how to operate as subscribers are listening and do not have a commmand prompt

# 127.0.0.1:6379> PUBSUB CHANNELS     # List active channels
# 127.0.0.1:6379> PUBSUB <subcommand> [argument [argument ...]]  # Generic pubsub command



# ======================================================================================================================
# Redis Streams used for messaging events
# ======================================================================================================================
# 127.0.0.1:6379> XADD  ...         # create message             
# 127.0.0.1:6379> XRANGE ...        # view message

# ======================================================================================================================
# Redis atomic transactions, locks, watches
# ======================================================================================================================
# In Redis, an atomic transaction starts with 'MULTI' and ends with 'EXEC'. the instructions will be queued and executed
# together.  If the connection is lost then none of the commands are run. rollbacks are not supported in redis

# 127.0.0.1:6379> MULTI
# 127.0.0.1:6379> ...
# 127.0.0.1:6379> ...
# 127.0.0.1:6379> EXEC

# An erroneous command will be skipped but won't block the other commands (unless a WATCH is transgressed (see below)

# 127.0.0.1:6379> WATCH lock_key  # Watches for changes to lock_key OUTSIDE of the subsequent transaction
# 127.0.0.1:6379> INCR lock_key   # execute this change from ANY client - this will cause the subsequent transaction to be blocked if it modifies lock_key
                                  # This INCR is successful however
# 127.0.0.1:6379> MULTI
# 127.0.0.1:6379> ...
# 127.0.0.1:6379> INCR lock_key   # since lock_key was modified outside of this transaction, after the WATCH was in place - this entire MULTI-EXEC transaction is discarded
# 127.0.0.1:6379> ...
# 127.0.0.1:6379> EXEC            # executes all queued commands. and removes the watch, but returns (nil) since the EXEC has been blocked

# 127.0.0.1:6379> UNWATCH         # removes all watches preventing a subsequent EXEC (not required if the EXEC has been performed)
# 127.0.0.1:6379> DISCARD         # will close the transaction without executing. see also 'pipelines' below

# ======================================================================================================================
# redis-py is a Python client library that lets you talk to a Redis server directly through Python calls
# ======================================================================================================================
# python -m pip install redis
# Requires server to be running C:\redis\Redis-x64-3.0.504\redis-server.exe
# py-redis API has a near identical command set as the redis client itself
# redis only accepts int, str, float or bytes for keys or values (not bytearray) but the value is always returned as a byte
# redis will convert the int/str/float to bytes before sending them off to the server
# ======================================================================================================================
from datetime import timedelta
import json
import redis

# These are all default values.  Creates database 0 which is default
r = redis.Redis(host='localhost',
                port=6379,
                db=0,
                username=None,
                password=None,
                socket_timeout=None,
                decode_responses=False,  # <-- this will ensure that binary data is decoded if set to true
    )  # SET THE REDIS CLIENT
# redis.from_url(url='redis://localhost/0:6379', username='foo', password='bar')    # alternative to above
# redis.client.Redis.from_url('redis://localhost/0:6379', username='foo', password='bar')       # same as above
# ======================================================================================================================
# strings {key:str)
# ======================================================================================================================
r.set("Germany", "Berlin")                        # Set single key/value -  returns True indicating succussful transaction
r.set(b"Germany", b"Berlin")                      # same as above -  returns True
r.mset({"France": "Paris", "England": "London"})  # Set multiple keys as a dictionary -  returns True
r.mset({'Japan': 'Tokyo'})                        # can use mset to set a single k,v pair as a dictionary
r.exists("England")                               # returns 1 for True  (0 for False)
r.get("England")                                  # returns b'London'
r.get("France").decode("utf-8")                   # returns 'Paris'

# convention to use colon in the key 
r.set(name='team:001', value='blue')
r.set(name='team:002', value='green')
r.set(name='team:003', value='red')

# Key (integer) Value (string)
r.set(1, 'one')                                   # Integers treated as strings, single quotes are fine  -  returns True
r.set('1', 'one')                                 # Same as above -  returns True
r.set(b'1', 'one')                                # Same as above -  returns True
r.set(b'1', b'one')                               # Same as above -  returns True
r.get(1)                                          # returns b'one'
r.get('1')                                        # returns b'one'
r.get(b'1')                                       # returns b'one'

# Key (string) Value (integer)
r.set('one', 1)                                   # Integer is stored as a bytestring -  returns True
r.set('one', '1')                                 # Same as above -  returns True
r.set('one', b'1')                                # Same as above -  returns True
r.get('one')                                      # returns b'1'

# Key (float) Value (string)
r.set(3.14, 'pi')                                 # floats treated as strings -  returns True
r.set('3.14', 'pi')                               # same as above  -  returns True
r.set(b'3.14', 'pi')                              # same as above -  returns True
r.get('3.14')                                     # b'pi'
r.get(b'3.14')                                    # b'pi'
r.get(3.14)                                       # b'pi'

# Examples with nested dictionaries using json
x1 = {"name": "John",
     "age": 30,
     "married": True,
     "divorced": False,
     "children": ("Ann", "Billy"),
     "pets": None,
     "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
r.set('person_001', json.dumps(x1))  # STRING OPERATION
json.loads(r.get('person_001'))      # RESTORE the dictionary

x2 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}
r.set('restaurant_001', json.dumps(x2))     # SET - returns True
print(json.loads(r.get('restaurant_001')))  # GET - returns {'name': 'Ravagh', 'type': 'Persian', 'address': {'street': {'line1': '11 E 30th St', 'line2': 'APT 1'}, 'city': 'New York', 'state': 'NY', 'zip': 10016}}

# r.set(name= , value=, ex= )  Full argument list below
# ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.
# ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.
# ``nx`` if set to True, set the value at key ``name`` to ``value`` only if it does not exist.
# ``xx`` if set to True, set the value at key ``name`` to ``value`` only if it already exists.
# ``keepttl`` if True, retain the time to live associated with the key. (Available since Redis 6.0)
# ``get`` if True, set the value at key ``name`` to ``value`` and return the old value stored at key, or None if the key did not exist. (Available since Redis 6.2)
# ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds, specified in unix time.
# ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds, specified in unix time.

# expiration settings
r.setex(name='runner1', time=10, value='this will dissapear')    # sets 'runner1' to expire after 10 secs
r.exists('runner1')    # returns true if not expired
r.setex('runner2', timedelta(seconds=10), value="this will dissapear")   # same as 'runner1'
r.setnx('key', 'va')  # rerturns True and sets k,v only if key does not exist
r.expire("runner2", timedelta(minutes=3))  # resets expire window
r.set("runner3", value='fred', ex=20) # sets expiration in secs
r.set("runner4", value='fred', px=20) # sets expiration in m-secs
r.ttl('runner3')                      # returns seconds to expiration
r.set('192.168.1.1', '1')
r.incr('192.168.1.1')                 # increments key b'192.168.1.1'
r.incrby('192.168.1.1', 2)            # increment by 2
r.decr('192.168.1.1')
r.decrby('192.168.1.1', 3)


# r.setex(name, time, value)	    Sets the value of key name to value that expires in time seconds, where time can be represented by an int or a Python timedelta object
# r.psetex(name, time_ms, value)	Sets the value of key name to value that expires in time_ms milliseconds, where time_ms can be represented by an int or a Python timedelta object
# r.expire(name, time)	            Sets an expire flag on key name for time seconds, where time can be represented by an int or a Python timedelta object
# r.expireat(name, when)	        Sets an expire flag on key name, where when can be represented as an int indicating Unix time or a Python datetime object
# r.persist(name)	                Removes an expiration on name
# r.pexpire(name, time)	            Sets an expire flag on key name for time milliseconds, and time can be represented by an int or a Python timedelta object
# r.pexpireat(name, when)	        Sets an expire flag on key name, where when can be represented as an int representing Unix time in milliseconds (Unix time * 1000) or a Python datetime object
# r.pttl(name)	                    Returns the number of milliseconds until the key name will expire
# r.ttl(name)	                    Returns the number of seconds until the key name will expire

# creates 100 keys 'key:0' to 'key:99'
for i in range(0, 100):
    r.set(f'key:{i}', f'value_{i}')

r.scan(cursor=0, match='key:*', count=5)    # Returns cursor = 72  & 4 keys, (72, [b'key:59', b'key:65', b'key:43', b'key:57'])
r.scan(cursor=72, match='key:*', count=5)   # Returns cursor = 120 & 4 keys  (120, [b'key:71', b'key:87', b'key:79', b'key:69'])

# ======================================================================================================================
# lists
# ======================================================================================================================
r.lpush('friends', 'sally', 'david')         # Creates key:list of friends with adding new values to the left
r.rpush('friends', 'andy')                   # appends friend to list from the right
r.lrange('friends', 0, -1)                   # returns full list [b'david', b'sally', b'andy']
r.lpop('friends')                            # left pop and returns b'david'
r.rpop('friends')                            # right pop and returns b'andy'
r.delete('friends')                          # deletes the key 'friends' returns 1 for success   (on cli use DEL)
r.delete('enemies')                          # returns 0 (false) as no such list                 (on cli use DEL)

# ======================================================================================================================
# sets
# ======================================================================================================================
visitors = ('fred', 'john', 'paul')
r.sadd('2020-02-20', *visitors)                   # adds visitors to set, key='2020-02-02
r.smembers('2020-02-20')                          # returns set {b'fred', b'john', b'paul'}
r.scard('2020-02-20')                             # returns 3  (number of elements in set)

# ======================================================================================================================
# hashes (nested dicts)
# ======================================================================================================================
r.hset('person', 'name', 'fred')                  # adds details to 'person'
r.hset('person', key='age', value=25)             # adds details to 'person'
r.hincrby(name='person', key='age', amount=1)     # adds 1 to age, returns the new age as integer
r.hincrbyfloat('person', 'age', 0.5)              # adds 0.5 to age, returns the new age as integer
r.hget('person', 'age')                           # returns b'26'
r.hgetall('person')                               # returns full dictionary of all values
r.hdel('person', 'age')                           # removes detail from person, returns 1 for success
r.delete('person')                                # removes entire hash, returns 1 for success
# r.hmset()                                       # WARNING deprecated


# ======================================================================================================================
# General (for all types)
# Note: keys() & type() allow pattern matching with '*' & '?' (not sure of other characters).
#       get() does not allow pattern matching
# ======================================================================================================================
r.ping()                                        # returns True if succesful Ping of the Redis server
r.info()                                        # same as redis cli
r.info('Keyspace')                              # same as redis cli
r.keys('*')                                     # returns full list of stored keys.  [b'Germany', b'England', b'person', b'France']
r.keys()                                        # same as above
r.keys('Fra?ce')                                # returns matching keys
r.type('France')                                # returns b'string'
r.rename('France', 'French')                    # renames the key
r.randomkey()                                   # returns a random key
r.select(2)                                     # returns True if number is valid (0 < number <=15). switches to db=2   -- default of 16 available, on error returns "redis.exceptions.ResponseError: invalid DB index"
r.client()                                      # returns connection info: Redis<ConnectionPool<Connection<host=localhost,port=6379,db=0>>>
r.config_get('requirepass')                     # retrieves config setting
r.config_set('rdbchecksum', 'no')               # sets a config setting for this shell
# r.config_rewrite()                            # rewrites the redis.conf file with current settings (not working)

r.delete('England')                             # deletes any key-value pair for any type

# ======================================================================================================================
# Redis pipelining: network optimization where all the commands are buffered on the client side and then sent at once
# ======================================================================================================================
# ======================================================================================================================
# Redis clients and servers communicate with each other using a protocol called RESP (Redis Serialization Protocol) 
# which is a TCP-based protocol where server and client communicate with request/response model.
# The client sends a request, the server processes the command while the client waits for the response in a blocking way. 
# Now consider a case, where we want to SET or GET 100s of commands, if we go by regular route, each command will take 
# up some Round Trip Time (RTT) and that will be repeated for all the commands, which is not optimum. 
# In cases like this, we can use Redis Pipeline.  for exampe RTT of .25ms is very slow.
# ======================================================================================================================
r1 = redis.Redis(db=1) # sets redis to  db=1

# ======================================================================================================================
# a transaction=True will block other redis operations until completed execution
# ======================================================================================================================
pipe = r1.pipeline(transaction=True)  # transaction=True is default, setting to False would remove the blocking
#pipe.multi()  <--- not required in this scenario -
pipe.set('foo1', 'one')
pipe.set('bar1', 'two')
#pipe.discard()  # this would cancel the transaction if appears before pipe.execute
pipe.execute()   # returns [True] if successful

#pipe.close()    # not quite sure what use this command is for as it doesn't seem to do anything
# ======================================================================================================================
# same as above with context manager - not sure what the context manager is
# ======================================================================================================================
with r1.pipeline() as pipe:
    pipe.set('foo2', 'one')
    pipe.set('bar2', 'two')
    pipe.execute()

# ======================================================================================================================
# locks and pipelines
# ======================================================================================================================
lock_expire = 4 * 60 * 60  # release lock after 4 hours as the key with expire
r1.set(name='lock_key', value=1, ex=lock_expire)
r1.exists('lock_key')  # returns 1 if exists, else 0

p = r1.pipeline()      # transaction=True is default 
p.watch('lock_key')    # watch for changes on this key, (can watch multiple keys with .watch('key1', 'key2') 
# p.set('lock_key', 'xxx')  # <----------- this will cause the entire transaction to fail
p.multi()              # MULTI - starts transactional block of pipeline
p.set('string1', 'value1')   # simply use 'p' as you would use 'r' or 'r1'
p.incr('lock_key')
try:
    res = p.execute()   # EXEC - the watch is removed and would need to be reset for another pipeline
    print(f'res={res}')
except redis.exceptions.WatchError: 
    # 'lock_key' has been changed
    print('entire transaction failed')  # lock_key was modified since the watch was implemented
else:
    if res == [True, 2]:
        print('transaction success')
p.unwatch()   # UNWATCH - removes any watches

# ======================================================================================================================
# pubsub()
# ======================================================================================================================
ps = r.pubsub()            # returns pubsub object
ps.subscribe('channel_1')  # subscribe to a channel
ps.connection              # Connection<host=localhost,port=6379,db=0>
ps.channels                # {'channel_1': None}
generator_obj = ps.listen()

# To enter listening mode ...
# for message in generator_obj:
#     print(message)

#
# {'type': 'subscribe', 'pattern': None, 'channel': 'channel_1', 'data': 1}
# {'type': 'message', 'pattern': None, 'channel': 'channel_1', 'data': 'test message'}
# {'type': 'message', 'pattern': None, 'channel': 'channel_1', 'data': 'test message2'}


# from a separate console
r.publish('channel_1', 'test message')
r.publish('channel_1', 'test message2')



# ======================================================================================================================
# Save the db session
# ======================================================================================================================
r.save()                    # creates dump.rdb file. save is synchronous and will have blocking.   Returns True. Redis command: SAVE
r.bgsave(schedule=False)    # background save is asynchronous, with no blocking.   Returns True.  Redis command: BGSAVE
r.lastsave()                # returns datetime.datetime(2022, 6, 28, 1, 29, 31).   Redis command: LASTSAVE
# r.flushdb()               # empties the 'r's db, i.e. db=0
# r.flushall()              # empties all dbs
# r.close()                 # not quite sure what use this command is for as it doesn't seem to do anything