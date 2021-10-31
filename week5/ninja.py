class phone:
    def __init__ (self,phone_number):
        self.number = phone_number
        self.call_history = []

    def phone_call(self,other_people):
        call_string = f'call from: {self.number} to: {other_people}
        self.call_history 