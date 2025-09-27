from datetime import datetime, timedelta, timezone
import jwt
from configs.keys import settings 


def gen_access_token(email, id, expiry_time: timedelta):
    # create the payload first with id and email as subject
    
    payload= {
        "subject": email,
        "id": id
    }
    # set the expiration time . now + 15-20 mins
    expires = datetime.now(timezone.utc) + expiry_time
    payload.update({'exp': expires})
    return jwt.encode(payload, settings.jwt_key, settings.jwt_algo )

    
