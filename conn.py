import mysql.connector as msc


def connect():
	host_name =input('Enter Hostname*:')
	user_name =input('Enter Username*:')
	password =input('Enter Password*:')

	factor=0
	try:connection_object=msc.connect(host=host_name,user=user_name,passwd=password);factor=1
	except msc.errors.ProgrammingError:factor=-1;print('ERROR due to wrong data.')

	if factor==-1:
		print('Please fill correct data.To exit type "-/exit" instead of data.')
		return connect()
	else:
		print('Connection Successful ☻')
		print('Please wait for database selection to be completed...')
		return connection_object



def data_selector():
	du.execute('show databases')
	databases = list(i[0] for i in du.fetchall())
	if all(i != 'student_management_system' for i in databases):
		f = open('commands.txt', 'r+')
		a = [i[:-1] for i in f.readlines()]
		for i in a[:5]: du.execute(i)
		for i in a[5:24]: du.execute('insert into admission values(' + i + ')');dbu.commit()
		for i in a[24:43]: du.execute('insert into student values(' + i + ')');dbu.commit()
		for i in a[43:]: du.execute('insert into fees values(' + i + ')');dbu.commit()
		print('database created')
	else:du.execute('use student_management_system');print('database selected')


def Display_Table(table,where='',fees='', fields='*'):
	fields_str = fields

	if fields != '*':
		fields_list = list(fields.split(','))

		fields = '('
		for i in fields_list[0:-1]: fields += "'" + i + "'" + ','
		fields += "'" + fields_list[-1] + "'" + ')'

		show_columns = 'show columns from ' + table + ' where field in' + fields
		du.execute(show_columns)
		a = du.fetchall()
		d = {}

	else:
		describe_table = 'describe ' + table
		du.execute(describe_table)
		a = du.fetchall()
		d = {}

	for i in a:
		if i[3] == 'PRI':
			d[i[0] + '*'] = i[1][0:3]
		else:
			d[i[0]] = i[1][0:3]

	display_table = 'select ' + fields_str + ' from ' + table +where
	keys = tuple(d.keys())
	du.execute(display_table)
	returner=du.fetchall()
	records = returner + [keys]
	ll = []

	for i in range(len(d)):
		length = max(list(len(str(j[i])) for j in records))
		ll.append(length)

	for i in range(len(keys)): print('||', ' ' * (ll[i] - len(keys[i])) + keys[i], end=' ')
	print('||')
	for i in records[:-1]:
		for j in range(len(i)): print('||', ' ' * (ll[j] - len(str(i[j]))) + str(i[j]), end=' ')
		print('||')
	if fees!='':return returner


dbu=connect()
du=dbu.cursor()