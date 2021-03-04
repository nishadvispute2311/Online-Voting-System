###### ONLINE VOTING SYSTEM ######

#Importing The Modules
import random
import datetime
import os
from prompt_toolkit import prompt
import getpass
import time


#Declaring the date of Winner Announcement
win_date="6/3/2021"


#Registration Process Of The Nominee
def nominee_reg():
	nom_vote=open("nominee vote status.txt","a")
	name=input("Enter Full Name : ")
	email=input("Enter Email : ")
	adhar=int(input("Enter Adhar Number : "))
	dob=input("Enter DOB (dd/mm/yyyy) : ")
	curr_date=datetime.date.today()
	age=int(str(curr_date).split('-')[0]) - int(dob.split('/')[2])
	if age>18:
		rdm=random.randint(100000,999999)
		id=f"{name.capitalize()[0]}{rdm}{name.split()[2].capitalize()[0]}{dob.split('/')[2]}"
		print(f"Nominee ID : {id}")
		nom_vote.write(f"0\t\t{name}\n")
		nom_vote.close()
		with open("nominee.txt","a") as nm:
			nm.write(f"{name},{email},{adhar},{dob},{age},{id}\n")
			nm.close()
		print("You Have Successfully Registered as Nominee.......!!!!!")
		
	else:
		print("Your age is below 18 years . You are not eligible for Nominee Registration")

	
#Registration Process Of The New Voter	
def voter_reg():
	name=input("Enter Full Name : ")
	email=input("Enter Email : ")
	adhar=int(input("Enter Adhar Number : "))
	dob=input("Enter DOB (dd/mm/yyyy) : ")
	curr_date=datetime.date.today()
	age=int(str(curr_date).split('-')[0]) - int(dob.split('/')[2])
	if age >= 18:
		rdm=random.randint(100000,999999)
		id=f"{str(rdm)}{name.capitalize()[0]}{dob.split('/')[2]}"
		print(f"Voting ID : {id}")
		
		with open("voter_details.txt","a") as vd:
			vd.write(f"{name},{email},{adhar},{dob},{age},{id},not voted\n")
			vd.close()
		print("You Have Successfully Registered as Voter.......!!!!!")
		
	else:
		print("Your age is below 18 years . You are not eligible for voting")


#Setup Of Secured Admin Panel To Monitor The Voting Process		
def admin_panel():
	pswd=prompt("Enter Password : ",is_password=True)
	if pswd=="Nishad@2311":
		print("\n\t    =======================================================================================================================")
		print("\t      1 : Voter Details \t   2 : Nominee Details \t     3 : Election Record\t  4 : Vote Status\t  5 : Exit")
		print("\t    =======================================================================================================================\n")
		while True:
			admin_choice = int(input("Enter your Admin Choice : "))
			if admin_choice == 1:
				id_of_voter = input("Enter Voter ID : ")
				with open("voter_details.txt") as vd:
					records=vd.readlines()
				for data in records:
						info=data.split(',')
						my_id=info[5][0:11:]
						if (id_of_voter==my_id):
							print("\n\t\t_______________________________________________________________________________________\n")
							print(f"\n\t\t\tName : {info[0]} \t\t Email : {info[1]} \n\t\t\tAdhar Number : {info[2]} \t\t Date Of Birth : {info[3]} \n\t\t\tAge : {info[4]} \t\t\t\t Voter Id : {info[5]} \n\t\t\tStatus : {info[6].capitalize()}")
							print("\t\t_______________________________________________________________________________________\n")
							break
						else:
							pass	
				
			elif admin_choice == 2:
				id_of_nom = input("Enter Nominee ID : ")
				with open("nominee.txt") as nm:
					records=nm.readlines()
				for data in records:
						info=data.split(',')
						my_id=info[5][0:12:]
						if (id_of_nom==my_id):
							print("\n\t\t_______________________________________________________________________________________\n")
							print(f"\n\t\t\tName : {info[0]} \t\t Email : {info[1]} \n\t\t\tAdhar Number : {info[2]} \t\t Date Of Birth : {info[3]} \n\t\t\tAge : {info[4]} \t\t\t\t Nominee Id : {info[5]}")
							print("\t\t_______________________________________________________________________________________\n")
							break
						else:
							pass
							
			elif admin_choice == 3:
				voters=open("voter_details.txt")
				nominee=open("nominee.txt")
				voter_list=voters.readlines()
				nom_list=nominee.readlines()
				count=0
				n_count=0
				for record in voter_list:
					data=record.split(',')
					if data[6][0:5:]=="Voted":
						count=count+1
					if data[6][0:9:]=="not voted":
						n_count=n_count+1
			
				print("\t\t\t\t     CURRENT ELECTION RECORD")
				print("\t\t\t__________________________________________________\n")
				print("\t\t\t\t Particulars \t\t       Counts")
				print("\t\t\t__________________________________________________\n")
				print(f"\t\t\t\tNo. Of Voters \t\t\t{len(voter_list)} \n\t\t\t\tNo. Of Nominees \t\t{len(nom_list)} \n\t\t\t\tNo. Of Voters Voted \t\t{count} \n\t\t\t\tNo. Of Voters Remaining \t{n_count}")
				print("\t\t\t__________________________________________________\n")

			elif admin_choice == 4:
				show_vote_status()
			
			elif admin_choice == 5:
				main()
				print("\n")
			
			else:
				print("Enter Valid Input.......!!!!")
	else:
		print("You Have Entered Incorrect Password.....!!!!\n")
		main()


# Tells us that which nominee has got how many votes
def show_vote_status():
	vote_status=open("nominee vote status.txt","r")
	print("\n\t\t\t\t       CURRENT VOTE STATUS")
	print("\t\t\t__________________________________________________\n")
	print("\t\t\t       Votes \t\t\t Name")
	print("\t\t\t__________________________________________________\n")
	for data in vote_status:
		print(f"\t\t\t\t{data}",end="")
	vote_status.close()
	print("\t\t\t__________________________________________________\n")


# Tells the names of the nominees
def nominee_info():
	names=[]
	nom_r=open("nominee.txt","r")
	records=nom_r.readlines()
	for data in records:
		info=data.split(',')
		names.append(info[0])
	for index,item in enumerate(names):
		print(f"\t\t\t\t{index+1} \t:\t {item}")


#Designing the Home UI
def home_ui():
		print("\t\t\t\t\tWelcome To The Online Voting System")
		print("\n\t\t================================================================================================================")
		print("\n\t\t 1 : Voter Login \t\t 2 : Admin Panel \t\t 3 : Nominee Info \t 4 : Voter Registration \n\t\t 5 : Nominee Registration \t 8 : Winner Announcement Date \t 7 : Exit")
		print("\n\t\t================================================================================================================")


#The Process Of Determining the Winner of Election		
def winner_dec():
	fv=open("nominee vote status.txt","r")
	final_votes=fv.readlines()
	winner=[]
	for vote in final_votes:
		get_vote=vote.split('\t\t')
		winner.append(f"{get_vote[0]}:{get_vote[1][0:len(get_vote[1])-1:]}")
	largest=int(winner[0].split(':')[0])
	for data in winner:
		d=data.split(':')[0]
		if int(d)>int(largest):
			largest=d
	for data in winner:
		if largest in data:

			
			print("\n\n\n\n\n\n\t\t\t===========================================================================")
			print(f"\n\n\n\t\t\t\tThe Winner of This Year Election is : {data.split(':')[1]}")
			print("\n\n\n\t\t\t===========================================================================")
		else:
			pass


# Here voter logins to vote the nominee
def voter_login():
	vd_r=open("voter_details.txt","r")
	vd_w=open("temp.txt","w")
	vs_r=open("nominee vote status.txt","r")
	voter_id=input("Enter your Voter ID : ")
	records=vd_r.readlines()
	for data in records:
		infos=data.split(',')
		if infos[5]==voter_id:
			print(f"Welcome {infos[0]} to the Online Voting System\n")
			print("\t\t\t__________________________________________________\n")
			print("\t\t\t\tNominees for this year election are :\n")
			print("\t\t\t__________________________________________________\n")
			nominee_info()
			print("\t\t\t__________________________________________________\n")
			voter_choice=prompt("Enter the number of Nominee to whom you want to vote : ",is_password=True)
			if infos[6][0:9:]=="not voted":
				vd_w.write(f"{infos[0]},{infos[1]},{infos[2]},{infos[3]},{infos[4]},{infos[5]},Voted\n")
				print(f"Thank you so much {infos[0].split()[0]} for your precious Vote........!!!!")
				vs=[]
				nom_det=vs_r.readlines()
				for data in nom_det:
					info=data.split("\t\t")
					vs.append(f"{info[0]}:{info[1][0:len(info[1])-1:]}")
				for i in range(len(vs)):
					if i+1==int(voter_choice):
						vs[i]=f"{int(vs[i][0])+1}:{vs[i][2::]}"
				vote_w=open("temp_votes.txt","w")
				for i in range(len(vs)):
					vote_w.write(f"{vs[i][0]}\t\t{vs[i][2::]}\n")
				vote_w.close()
				os.remove("nominee vote status.txt")
				os.rename("temp_votes.txt","nominee vote status.txt")
			if infos[6][0:5:]=="Voted":
				print(f"Sorry {infos[0].split()[0]} You have Already Voted..........!!!!!!")
				vd_w.write(data)
		else:
			vd_w.write(data)
	vd_r.close()
	vd_w.close()
	os.remove("voter_details.txt")
	os.rename("temp.txt","voter_details.txt")
		

# Taking the User Inputs Here
def main():
	while True:
		user_choice = int(input("\nEnter your User Choice : "))
		if user_choice == 1:
			voter_login()
		elif user_choice == 2:
			admin_panel()
		elif user_choice == 3:
			print("\t\t\t__________________________________________________\n")
			print("\t\t\t\tNominees for this year election are :\n")
			print("\t\t\t__________________________________________________\n")
			nominee_info()
			print("\t\t\t__________________________________________________\n")
		elif user_choice == 4:
			voter_reg()
		elif user_choice == 5:
			nominee_reg()	
		elif user_choice == 6:
			print("\n\t\t__________________________________________________________________________________")
			print("\n\t\t\tThe Winner Of This Year Election Will Be Announced On : 05/03/2021")
			print("\t\t__________________________________________________________________________________\n")
		elif user_choice == 7:
			print("Thank You So Much..........!!!!!!")
			exit()
		else:
			print("Enter Valid Choice")


# The Process Of Announcing the Winner Of Election 
def winner_announce():
	d=win_date.split("/")
	if (len(d[0])==1 and len(d[1])==1):
		datd=f"0{d[0]}0{d[1]}{d[2]}"
	elif (len(d[0])==1):
		datd=f"0{d[0]}{d[1]}{d[2]}"
	elif (len(d[1])==1):
		datd=f"{d[0]}0{d[1]}{d[2]}"
	
	local_date=time.strftime("%d%m%Y")
	
	if int(local_date)>=int(datd):
		winner_dec()
	else:
		home_ui()
		main()



if __name__=='__main__':
			winner_announce()
			

