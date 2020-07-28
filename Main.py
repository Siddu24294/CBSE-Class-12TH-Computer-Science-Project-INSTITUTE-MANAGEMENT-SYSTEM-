import conn as c
import ad as a
import st as s
import fe as f
import menu as m


c.data_selector()


print(
'''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░ Welcome to massachusetts Institute management system ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')


print(m.main_menu)

while 1:
	choice=int(input('enter your choice(1-4):'))

	if choice==4:print('Exiting...');break

	elif choice==1:
		while 1:
			print(m.admission_menu)
			ch=int(input('enter your choice(1-6):'))

			if ch==1:a.admin_1()
			elif ch==2:a.admin_2()
			elif ch==3:a.admin_3()
			elif ch==4:a.admin_4()
			elif ch==5:a.admin_5()
			elif ch==6:print(m.main_menu);break
			else:print('Invalid Choice.Please try again.')

	elif choice==2:
		while 1:
			print(m.student_data_menu)
			ch=int(input('enter your choice(1-6):'))

			if ch==1:s.std_1()
			elif ch==2:s.std_2()
			elif ch==3:s.std_3()
			elif ch==4:s.std_4()
			elif ch==5:s.std_5()
			elif ch==6:print(m.main_menu);break
			else:print('Invalid choice.Please try again.')

	elif choice==3:f.fees_2()

c.du.close()
c.dbu.close()
exit()