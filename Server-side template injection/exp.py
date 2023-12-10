import base64


def custom_function():
    # Your custom function code here
    print("Custom function called")

original_data = 'hello'

encoded_data = base64.b64encode(original_data.encode('utf-8')).decode('utf-8')
print(encoded_data)
decoded_data = base64.b64decode(encoded_data).decode('utf-8')
print(decoded_data)

h = ['hello', 'hell']
p = ['a', 'b', 'c', 'd', 'e']

# Print combinations
for element_h in h:
    for element_p in p:
        print(element_h, element_p)
        if element_h == decoded_data and element_p == 'd':
            custom_function()

print(str('p'))
