def decodeRequestHeader(data):
    dataMap = {}
    dataMap['Target'] = None
    dataMap['Body'] = None
    if('GET' in data):
       return decodeGet(data, dataMap)
    elif('POST' in data):
        return decodePost(data, dataMap)
    
def decodeGet(data, dataMap):
    data = data.split('\\r\\n', 20)
    target = data[0].split(' ')
    if('/' in target[1]):
        dataMap['Target'] = target[1][1:]
    else:
        return None
    for string in data:
        pair = string.split(':', 1)
        if(len(pair) != 2):
            continue
        dataMap[pair[0]] = pair[1]
    return dataMap

def decodePost(data, dataMap):
    data = data.split('\\r\\n', 20)
    body = data[-1][0:-1]
    dataMap['Body'] = body
    for string in data:
        pair = string.split(':', 1)
        if(len(pair) != 2):
            continue
        dataMap[pair[0]] = pair[1]
    return dataMap