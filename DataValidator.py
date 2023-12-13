class ValidateData:
    def __init__(self):
        self.validate_data = []

    def validate_data_input(self, validate_input):
        for input in validate_input:
            if self.valid_positive_integer(input):
                self.validate_data.append(int(input))

    def valid_positive_integer(self, input):
        try:
            num = int(input)
            if num > 0:
                return True
            else:
                return False
        except ValueError:
            return False
        
validating_data = ValidateData()

user_inputs = ['1','2','3','knock knock','-1','4','5']

validating_data.validate_data_input(user_inputs)
print('valid data input', validating_data.validate_data_input())

