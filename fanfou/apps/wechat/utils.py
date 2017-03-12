from hashlib import sha1

def  check_signature(signature, timestamp, nonce, echostr, token):
    tmp_list = [token, timestamp, nonce]
    tmp_list.sort()
    tmp_str = "%s%s%s" % tuple(tmp_list)
    tmp_str_bytes = tmp_str.encode('utf-8')
    tmp_str = sha1(tmp_str_bytes).hexdigest()
    if tmp_str== signature:
        return True
    else:
        return False