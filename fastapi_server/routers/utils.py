
def serialize_id(data):
    data['_id'] = str(data['_id'])
    return data