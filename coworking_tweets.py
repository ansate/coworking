import sys
import twitter
#https://pypi.python.org/pypi/twitter
import random

max_len = 140
tco_len = len(" http://t.co/vdWeWnab4d4444")

mesg = sys.argv[1]
url = sys.argv[2]

t = twitter.Twitter(auth=twitter.OAuth('Access Token', 'Access Token Secret', 'API Key','API Secret'))

#fill in both screen_name and user_id http://tweeterid.com/
coworkingers = t.followers.ids(screen_name="", user_id=)

ids = coworkingers['ids']

print ids


names = []
for uid in ids:
    user = t.users.show(user_id=uid)
    names.append(user['screen_name'])

random.shuffle(names)

namespace = max_len - tco_len - len(mesg)

tweet = ""

for name in names:
    full = "@" + name + " "
    if namespace - len(full) < 0:
        print tweet + mesg + " " + url
        namespace = max_len - tco_len - len(mesg) - len(full)
        tweet = full
    else:
        tweet = tweet + full
        namespace = namespace - len(full)
print tweet + mesg + " " + url
