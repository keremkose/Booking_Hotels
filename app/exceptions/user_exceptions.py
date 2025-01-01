
class UserNotFound(Exception):
    def __init__(self, message="User is not found."):
        self.message=message
        super().__init__(self.message)