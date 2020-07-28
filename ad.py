import conn as c
import menu as m


def admin_1():
	id=input('enter admission number:')
	name=input('enter student\'s name:')
	clas=input('enter student class:')
	dob=input('enter dae of birth in YYYY/MM/DD format:')
	bloodgrp=input('enter blood group of student:')
	phno=input('enter contact number of the student:')
	address=input('enter student\'s address:')
	insert='insert into admission values('+id+',\''+name+'\','+clas+',\''+dob+'\',\''+bloodgrp+'\',\''+phno+'\',\''+address+'\')'
	du.execute(insert)
	dbu.commit()
	fee_insert='insert into fees values('+id+',\''+name+'\','+clas+',10000)'
	du.execute(fee_insert)
	dbu.commit()
	print('Student has been added to the registry.')
	input('press any key to continue...')


def admin_2():
	c.Display_Table('admission')


def admin_3():
	id = input('Enter admission number of the required student:')
	query='select adm_id from admission'
	du.execute(query)
	a=du.fetchall()
	id_list = list(int(i[0]) for i in a)
	if int(id) in id_list:
		query = ' where adm_id='+id
		c.Display_Table('admission',query)
	else:print('Student ID',id,'is not registered in the school.')


def admin_4():
	id=input('Enter the student\'s admission number to be removed from registry:')
	query='select adm_id from admission'
	du.execute(query)
	id_list = list(int(i[0]) for i in du.fetchall())
	if int(id) in id_list:
		query='delete from admission where adm_id='
		query=query+id
		du.execute(query)
		dbu.commit()
		query = 'delete from student where adm_id='
		query = query + id
		du.execute(query)
		dbu.commit()
		query = 'delete from fees where adm_id='
		query = query + id
		du.execute(query)
		dbu.commit()
		print('Record removed...')
		input('press any key to continue...')
	else:print('Student ID', id, 'is not registered in the school.')


def admin_5():
	id = input('enter admission number of the required student:')
	query='select adm_id from admission'
	du.execute(query)
	id_list = list(int(i[0]) for i in du.fetchall())
	if int(id) in id_list:
		while 1:
			print(m.update_menu)
			chi=int(input('Enter your choice(1-7):'))
			q=''
			if chi==7:input('Press any key to continue...');break
			elif chi==1:q='Name=\''+input('Correct name:')+'\' '
			elif chi==2:q='Class='+input('Correct class:')+' '
			elif chi==3:q='DOB=\''+input('Correct date of birth(YYYY/MM/DD):')+'\' '
			elif chi==4:q='BloodGrp=\''+input('Correct blood group:')+'\' '
			elif chi==5:q='Phone_No=\''+input('Correct contact number:')+'\' '
			elif chi==6:q='Address=\''+input('Correct address:')+'\' '
			query='update admission set '+q+'where adm_id='+id
			du.execute(query)
			dbu.commit()
			print('Registry Updated.')
			input('press any key to continue...')
	else:print('Student ID', id, 'is not registered in the school.')



dbu=c.dbu
du=c.du