import conn
import menu as m


def fees_1():
	id = input('Enter admission number of the required student:')
	query='select adm_id from fees'
	du.execute(query)
	id_list=list(int(i[0]) for i in du.fetchall())
	if int(id) in id_list:
		query = ' where adm_id=' + id
		a=conn.Display_Table('fees',query,'1')
		b=a[0]
		c=b[-1]
		print(c,'is the pending fees to be paid.'if c!=0 else 'You have already Cleared all due fees.Thank you.')
		return c,id
	else:return id,-1


def fees_2():
	a,id=fees_1()
	if id==-1:print('Student ID',a,'not registered in the school.')
	else:
		if a>0:
			ch=input('Do you wish to clear the dues now?(y/n):').lower()
			if ch=='y':
				x=input('enter value of the deposit money:')
				query='update fees set Pending_fees=Pending_fees-'+x+' where adm_id='+id
				du.execute(query)
				dbu.commit()
				x=int(x)
				print('You have cleared all your dues.Thank you'if a-x==0 else 'You still have '+str(a-x)+' Rs. due.')

			else:input('Press any key to continue...')
	print(m.main_menu)


dbu=conn.dbu
du=conn.du