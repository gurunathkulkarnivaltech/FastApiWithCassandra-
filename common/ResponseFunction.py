def sendResponse(message, data=[], error={}, status=False, statusCode=200):
    return { "message": message, "data": data, "error": error, "status": status, "statusCode": statusCode }
    