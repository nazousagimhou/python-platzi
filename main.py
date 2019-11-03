import sys

#clients = ['Cuau','Ricardo','Pepe','Alit','Mau'] Esta fue una lista

clients = [
	{
		'name': 'Pablo',
		'company': 'Google',
		'email': 'pablo@google.com',
		'position': 'Software engineer', 
	},
	{
		'name': 'Ricardo',
		'company': 'Globant',
		'email': 'ricardo@globant.com',
		'position': 'Back end developer',
	},
] #Estuctura de diccionario para guardar los datos de los clientes

def create_client(client):
	global clients # Pregunta, porque se necesita una bariable global en esta funcion y en las demas
	
	if client not in clients:
		clients.append(client)
	else:
		print('Client already is in the clients\'s list')


def list_clients():
	for idx, client in enumerate(clients):
		print('{uid}|{name}|{company}|{email}|{position}'.format(
			uid = idx,
			name = client['name'],
			company = client['company'],
			email = client['email'],
			position = client['position']))

def update_client(client_name, update_client):
	global clients
	isClientFound = False
	
	for client in clients:
		if client['name'] == client_name:
			client['name'] = update_client['name']
			client['company'] = update_client['company']
			client['email'] = update_client['email']
			client['position'] = update_client['position']
			isClientFound = True	

	if not isClientFound:
		print('Client is not in clients\'s list ')

def delete_client(client_id):
	global clients
	clients_lenght = len(clients)

	if client_id <= clients_lenght and client_id >= 0:
		del clients[client_id]
	else:
		print('Client is not in clients\'s list')

def search_client(client_name):
	for client in clients:
		if client['name'] != client_name:
			continue
		else:
			return True

def _get_client_field(field_name):
	field = None

	while not field:
		field =input('What is the client {} ? '.format(field_name))

	return field


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = input('Wha is the client name? :D ')

		if client_name == 'exit':
			client_name = None
			break
	if not client_name:
		sys.exit()

	return client_name

def _get_client_from_user():
	client = {
			 'name': _get_client_field('name'),
			 'company': _get_client_field('company'),
			 'email': _get_client_field('email'),
			 'position': _get_client_field('position'),
		}
	return client
	

def _print_welcome():
	print('WELCOME TO PLATZI')
	print('*-' * 50)
	print('What would you like to do today? ')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')
	print('[L]ist clients')


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client = _get_client_from_user()

		create_client(client)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'S':
		client_name = _get_client_field('name')
		print('Name to be searched: {}'.format(client_name))
		found = search_client(client_name)

		if found:
			print('The client is in the Client\'s list')
		else:
			print('The client: {} is not in the Client\'s list'.format(client_name))

	elif command == 'U':
		client_name = _get_client_field('name')
		found = search_client(client_name)

		if found:
			updated_client = _get_client_from_user()
		
			update_client(client_name, updated_client)
			list_clients()	
		else:
			print('The client: {} is not in the Client\'s list'.format(client_name))

	elif command == 'D':
		client_id = int(_get_client_field('id'))

		delete_client(client_id)
		list_clients()
	else:
		print('Invalid command')
