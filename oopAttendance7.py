attendancech = ["bhavya", "shreya", "aleena"]
idnumat = [123213, 123124, 123125]
FINALREGIS = []
#attendance app that automatically takes student attendance
#how
#dream develop an app that uses AI to recognize student face. 
#get user data to recognize the user by an ID (password)
#track arrival time
#student types in data
#what data?

#register student

def studentRegistration():
  global studentName 
  studentName = input("enter your name")
  if studentName in attendancech:
    print("NAME ACCEPTED!")
  else: 
    print("NAME NOT ACCEPTED!")
    studentRegistration()  
  
      
      
  #not a scalable approach, only one student ormake 32 variables!!

#take attendance
def attendance():
  global userInput
  userInput = input("whats ur student id")
  if userInput.isnumeric():
    userInput = int(userInput)
    if userInput in idnumat:
      print("ID ACCEPTED!")
    else:
      print("ID NOT ACCEPTED!")
      attendance()
  else:
    print("numbers only")
    attendance()

def check(): 
  FINALREGIS.append(studentName + str(userInput))
  
  
    ##no way recursion!!!!!!!!!!!
#student data
#name
studentname = ""
#age or grade level
age = 0
#inclass, present, late, not present
present = ""
#student id
sid = 000
#is the the student late

##isTakingattendance=True
##while isTakingattendance: 
  ##attendance()
def attache():
  studentRegistration()
  attendance()
  check()
  if len(FINALREGIS) < 32:
    attache()
  if len(FINALREGIS) == 32: 
    print("ATTENDANCE COMPLETE")

attache()

  
