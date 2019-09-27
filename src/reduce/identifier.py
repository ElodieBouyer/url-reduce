import random
import string
 
from django.conf import settings
 
BASE = string.ascii_uppercase + string.ascii_lowercase + string.digits
LEN = 8
 
 
def gen_identifier():
    return ''.join(random.choice(BASE) for x in range(LEN))
 
 
def get_new_identifier():
    identifier = gen_identifier()
    return identifier