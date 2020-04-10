import secrets
import numpy as np
from .models import *

def generate_token(tokens:set(), n:int):
    if len(tokens) == n:
        return 
    for i in range(n):
        tokens.add(secrets.token_urlsafe())

    #check for n unique tokens
    return generate_token(tokens, len(tokens) - n)




def add_token(n:int, course_id:int):
    new_tokens = set()
    generate_token(new_tokens, n)

    db_tokens = Token.objects.all()
    print(type(db_tokens))
    couples = np.intersect1d(new_tokens, db_tokens)
    print(len(new_tokens), '-----------', couples)