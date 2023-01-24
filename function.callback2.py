def send_data(data):
    # sending data to the remote server
    print('4. send_data(data)', data)
    pass


def process_data(input_data, send_data_fn):
    update_data = input_data.copy()
    print('2. update_data = input_data.copy()      ', update_data)
    # action with update_data
    print('3. send_data_fn(update_data)')
    send_data_fn(update_data)


print("1. process_data({'name': 'Roman'}, send_data)")
process_data({'name': 'Roman'}, send_data)
