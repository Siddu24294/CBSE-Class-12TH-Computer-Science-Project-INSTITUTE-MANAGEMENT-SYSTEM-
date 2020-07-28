import conn as c
import menu as m
import ad as a


def std_1():
	id = input('enter admission number:')
	query='select adm_id from admission'
	du.execute(query)
	id_list = list(int(i[0]) for i in du.fetchall())
	if int(id) not in id_list:
		print('Student is not in the admission record.')
		print('Please get register him/her in admission record by filling the following form.')
		a.admin_1();print('Try again to add the student to class registry.')
	else:
		print('Student found in the admission record.')
		print('Fill the following form to add the student to the class registry.')
		name = input('enter student\'s name:')
		clas = input('enter student\'s class:')
		roll=input('enter student\'s roll number:')
		sub=input('enter students\'s stream:')
		marks=input('enter marks out of 100:')
		insert='insert into student values('+id+',\''+name+'\','+clas+','+roll+',\''+sub+'\','+marks+')'
		print(insert)
		du.execute(insert)
		dbu.commit()
		print('student has been added to the class registry.')
		input('press any key to continue...')


def std_2():
	c.Display_Table('student')


def std_3():
	id = input('Enter roll number of the required student:')
	query='select Rollno from student'
	du.execute(query)
	id_list=list(int(i[0])for i in du.fetchall())
	if int(id) in id_list:
		query = ' where Rollno=' + id
		c.Display_Table('student',query)
	else:print('Student ID',id,'is not registered in the class.')


def std_4():
	query='delete from Student where Rollno='
	id=input('Enter the student\'s roll number to be removed from class registry:')
	query='select Rollno from student'
	du.execute(query)
	id_list = list(int(i[0]) for i in du.fetchall())
	if int(id) in id_list:
		query=query+id
		du.execute(query)
		dbu.commit()
		print('Record removed...')
		input('press any key to continue...')
	else:print('Student ID',id,'is not registered in the school.')


def std_5():
	id = input('enter admission number of the required student:')
	query='select adm_id from student'
	du.execute(query)
	id_list = list(int(i[0]) for i in du.fetchall())
	if int(id) in id_list:
		while 1:
			print(m.student_update_menu)
			chi = int(input('Enter your choice(1-6):'))
			q = ''
			if chi==6:input('Press any key to continue...');break
			elif chi==1:q = 'Name=\'' + input('Correct name:') + '\' '
			elif chi==2:q = 'Class=' + input('Correct class:') + ' '
			elif chi==3:q = 'RollNo=' +input('Correct roll number:')+' '
			elif chi==4:q = 'Stream=\'' +input('Correct stream:')+'\' '
			elif chi==5:q = 'Marks='+input('Correct marks Scored out of 100:')+' '
			query = 'update student set ' + q + 'where adm_id=' + id
			du.execute(query)
			dbu.commit()
			print('Registry Updated.')
			input('press any key to continue...')
	else:print('Student ID',id,'is not registered in the school.')


dbu=c.dbu
du=c.du