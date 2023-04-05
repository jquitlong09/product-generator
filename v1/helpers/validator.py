class Validator:
    def __init__(self):
        pass

    def validate_required(self, required, param):
        # check if required field names are present in the request body
        status = True
        for field in required:
            if field not in param.keys():
                status = False
        return status
