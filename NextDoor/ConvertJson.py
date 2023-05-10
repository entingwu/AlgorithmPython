import re
class ConvertJson:
    # {
    #    "validation_errors": [
    #       {
    #           "first_name": "christy",
    #           "description_msg": "required field",
    #       },
    #       {
    #           "last_name": "wu",
    #           "description_msg": "required field",
    #       },
    #    ],
    #    "request_id": "1234",
    # }

    camel_pat = re.compile(r'([A-Z])')
    snake_pat = re.compile(r'_([a-z])')

    def camel_to_snake(self, s):
        return self.camel_pat.sub(lambda x: '_' + x.group(1).lower(), s)

    def snake_to_camel(self, s):
        return self.snake_pat.sub(lambda x: x.group(1).upper(), s)

    def convert_snake_to_camel(self, s):
        print(s)
        output = {}
        for key in s:
            new_key = self.snake_to_camel(key)
            new_value = s[key]
            if isinstance(s[key], dict):
                new_value = self.convert_snake_to_camel(s[key])
            elif isinstance(s[key], list):
                new_value = self.convert_array_snake_to_camel(s[key])
            output[new_key] = new_value
        return output

    def convert_array_snake_to_camel(self, a):
        newArray = []
        for item in a:
            newItem = item
            if isinstance(item, dict):
                newItem = self.convert_snake_to_camel(item)
            elif isinstance(item, list):
                newItem = self.convert_array_snake_to_camel(item)
            newArray.append(newItem)
        return newArray

    def snake_to_camel1(s):
        s = re.sub(r"_|-+", " ", s).title().replace(" ", "")
        return ''.join([s[0].lower(), s[1:]])