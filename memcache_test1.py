import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import memcache
client = memcache.Client([('127.0.0.1', 11211)])
# sample_obj = {"name" : "Jackson",
# "lang": "Python"}
# client.set("sample_user", sample_obj, time=15)
# print "Stored to memached, will auto-expire after 15 seconds"
# print client.get("sample_user")

# client.set("counter","10")
# client.incr("counter")
# print "Counter was incremented on the server by 1, now it's %s" 
# client.get("counter")
# client.incr("counter",9)
# print "Counter was incremented on the server by 9, now it's %s" 
# client.get("counter")
# client.decr("counter")
# print "Counter was decremented on the server by 1, now it's %s" 
# client.get("counter")

data = {"some_key1": "value1",
"some_key2":"value2"}
client.set_multi(data, time=15, key_prefix="pfx_")
print "saved the dict with prefix pfx_"
print "getting one key: %s" % client.get("pfx_some_key1")
print "Getting all values: %s" % client.get_multi(["some_key1", "some_key2"], key_prefix="prx_")