class InnerException(Exception):
    def __init__(self, code, msg, data=None):
        self.code = code
        self.msg = msg
        self.data = data


class UserNotExistsException(InnerException):
    def __init__(self, msg=""):
        super().__init__(code='0001', msg='USER NOT FOUND')


class UserPasswordError(InnerException):
    def __init__(self, msg=""):
        super().__init__(code='0002', msg='USER PASSWORD INCORRECT')


class UserAlreadyExistsException(InnerException):
    def __init__(self, msg=""):
        super().__init__(code='0003', msg='USER ALREADY EXISTS')
