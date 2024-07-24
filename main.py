# easiest shit i have ever done lmao
import jwt, json

def get_hsw_version(req):
    decoded_jwt_token = jwt.decode(req, options={"verify_signature": False})
    return json.loads(json.dumps(decoded_jwt_token, separators=(",", ":")))['l'] + '/hsw.js'