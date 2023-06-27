import csv
import numpy as np  
import os 


class exam_managemet:
    def __init__(self):
        self.stu=np.array([
            ['1','haseeb','mahmood','1','class_9'],
            ['2','abdul','ali','2','class_10'],
            ['3','abdullah','shaikh','3','class_8'],
            ['4','haris','javed','4','class_9'],
            ['5','iyer','seraiki','5','class_8'],
            ['6','jawad','ali','6','class_10'],
         ])
        self.teacher=np.array([
            ['1','sir_kazim','programing','1','class_8'],
            ['2','miss_atiya','pom','2','class_9'],
            ['3','miss_sabika','lab','3','class_10'],
        ])

    def login(self):
        print('Press a For Admin')
        print("Press 1 For Login as a Student")
        print("Press 2 For Login as a Teacher")
        log=input("::")
        if log=='1':
            self.s_id=input("Enter Your Student_ID : ")
            self.s_ps=input("Enter Your Password   : ")
            s.student_info()
            
        if log=='2':
            self.t_id=input("Enter Your Teacher_ID : ")
            self.t_ps=input("Enter Your Password   : ")
            s.teacher_info()
        
        if log=='a':
            self.a_id=input("Enter Your ID       : ")
            self.a_ps=input("Enter Your Password : ")
            
            if self.a_id=='haseeb' and self.a_ps=='123':
                print("-------------Welcome Admin ------------")
                s.admin()
            else:
                print("invalid")
                s.login()
    def teacher_info(self):
        
            for i in range (len(self.teacher)):
                check_pass=self.teacher[i,3]
                self.check_id=self.teacher[i][0]
                if self.check_id==self.t_id and check_pass==self.t_ps:
                    a=i
                    
            try:
                self.tname=self.teacher[a,1]
                self.tsub=self.teacher[a,2]
                self.tcla=self.teacher[a,4]
                print("Your Name:",self.tname)
                print("Your Subject:",self.tsub)
                print("---------------welcome Teacher-----------------")
                print("If You Want To Make paper Press 'm'")
                print("If You Want To check your Subject Results Press 'r'")
                print("If You Want To Exit Press 'e'")
            except:
                print("Invalid Try Again")
                s.login()
            teacher_input=input("::")
            if teacher_input=='m':
                #print("Which Class Paper You Want To Make(Give input eg'class_5')")
                self.paper_making_class=self.tcla
                #print("Which Subject Paper You Want To Make")
                self.paper_subject=self.tsub
                s.Checking_File()
                
            if teacher_input=='r':
                o=f'results\{self.tcla}_results.csv'
                if os.path.exists(o):
                    s.load_file_s_info(o)
                    
                    # for i in range(self.N):
                    #     # a=self.data[i]
                    #     # print(a)
                else:
                    print("No Result")
                    
                s.teacher_info()
            if teacher_input=='e':
                print("You Are Logged out")
                exit


    def student_info(self):
        for i in range (len(self.stu)):
            check_pass=self.stu[i,3]
            self.check_id=self.stu[i][0]
           
            if self.check_id==self.s_id and check_pass==self.s_ps:
                    a=i
                   
        try:
            sclass=self.stu[a,4]
            self.sname=self.stu[a,1]
            self.lname=self.stu[a,2]
            self.sclass=self.stu[a,4]
            print("Your Name:",self.sname,self.lname)
            print("Your Class:",self.sclass)
            print("---------------welcome----------------")
            print("If You Want TO Give Paper Press 'g'")
            print("If You Want TO Check Your Results 'r'")
            print("For Exit Press'e'")
            s_in=input('::')
            if s_in=='g':
                print("Available Papers:")
                s.show_avaiable_paper(sclass)
                self.filename=f"{self.sclass}\{self.csv_files[self.chosen_exam]}"
                s.load_file_s_info(self.filename)
                s.give_paper()
            elif s_in =='r':
                o=f'indivisual_results\{self.sname}_results.csv'
                if os.path.exists(o):
                    s.load_file_s_info(o)
                    for i in range(self.N):
                        print(self.data[i])
                    s.student_info()
                else:
                    print("No Result")
                    s.student_info()
            if s_in=='e':
                    print("You Are Logged out")
                    exit
        except:
            print("invalid")
            s.login()
       
    def admin(self):
            print("If You Want To Check Any Class Paper Uploaded And Data In It Press 'c'")
            print("If You Want To Check Any Specific Class Result Press 'r1'")
            print("If You Want To Check Any Specific Student Result Press 'r2'")
            print("For Exit Press 'e'")
            a_in=input('::')
            if a_in=='c':
                c_in=input(' A Class Paper You Want To Check')
                s.show_avaiable_paper(c_in)
                o=f"{c_in}\{self.csv_files[self.chosen_exam]}"
                s.load_file_s_info(o)
                for i in range(self.N):
                    print(self.data[i])
                s.admin()
            elif a_in=='r2':
                c_in='indivisual_results'
                s.show_avaiable_paper(c_in)
                o=f"{c_in}\{self.csv_files[self.chosen_exam]}"
                s.load_file_s_info(o)
                for i in range(self.N):
                    print(self.data[i])
                s.admin()
            elif a_in=='r1':
                c_in='results'
                s.show_avaiable_paper(c_in)
                o=f"{c_in}\{self.csv_files[self.chosen_exam]}"
                s.load_file_s_info(o)
                for i in range(self.N-1):
                    print(self.data[i])
                s.admin()   
            elif a_in=='e':
                    print("You Are Logged out")
                    exit
    def show_avaiable_paper(self,vclass):
        
        all_files = os.listdir(f'{vclass}')    
        self.csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))
        w=0
        for i in range(len(self.csv_files)):
            self.v=self.csv_files[i].replace('.csv','')
            print(f"Press {i} for {self.v} Exam")
            w+=1
        if w == 0:
            print("No Paper Available")
            s.login()
        else:    
            self.chosen_exam=int(input("::"))
        
    def load_file_s_info(self, filename):
        self.N = 0
        self.data = np.array([['' for i in range(6)]for j in range(20)],dtype=object)
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for i in range(len(row)):
                        self.data[self.N][i] = row[i]
                    self.N += 1
                    
                
        else:
            print(f'{filename} file not found')
        self.line_have=self.N-1
        for i in range(self.line_have):
            self.v=self.data[i]
            print(self.v)
        
    def give_paper(self):
        self.correct_ans=[]
        self.results=0
        for i in range(self.N):
            # for  j in range(len(self.data[0])-1):
            print(f'Question{i+1}:{self.data[i,0]}')
            print(f'1){self.data[i,1]}')
            print(f'2){self.data[i,2]}')
            print(f'3){self.data[i,3]}')
            print(f'4){self.data[i,4]}')
            answer=input("Enter Correct Answer In Number(eg_1)::::")
            if answer== self.data[i][5]:
                self.results+=5
                self.correct_ans.append(i+1)
                print("correct")
            else :
                print("incorrect")
       
        # os.remove(self.filename)
       
        
        s.final()
    def Checking_File(self):
        if os.path.exists(f'{self.paper_making_class}\{self.paper_subject}.csv'):
            print("Already Exist")
            print("If You Want To Add Question In Already Exist File Input 'a'")
            print("If You Want To Write Question In Already Exist File Input 'w'")
            self.exist=input("::")
            s.make_paper()
            
        else:
            self.exist='w'
            s.make_paper()
    def file_making(self):
        
        if self.exist=='w':
            with open(f'{self.paper_making_class}\{self.paper_subject}.csv','w',newline='') as file:
                writer = csv.writer(file)
                
                writer.writerows(self.question)
        elif self.exist=='a':
            with open(f'{self.paper_making_class}\{self.paper_subject}.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.question)
    def make_paper(self):
        self.total_question = int(input("how many question you want to enter"))
        self.question =np.array([['' for i in range(6)]for j in range(self.total_question)],dtype=object)
        self.Qcount=0
        for i in range(self.total_question):
            question = input('Enter Your Question : ')
            a1 = input('Give Option 1: ')
            a2 = input('Give Option 2: ')
            a3 = input('Give Option 3: ')
            a4 = input('Give Option 4: ')
            right = input('Give Right Option: ')
            self.ques=np.array([question,a1,a2,a3,a4,right])
            self.question[self.Qcount][0]= question
            self.question[self.Qcount][1]= a1
            self.question[self.Qcount][2]= a2
            self.question[self.Qcount][3]= a3
            self.question[self.Qcount][4]= a4
            self.question[self.Qcount][5]= right
            self.Qcount+=1
        
        
        s.file_making()
        print("Sucessfully Uploaded")  
        s.teacher_info()
    def final(self):
        w="Id:",self.check_id
        a="Name:",self.sname,self.lname
        b="Class:",self.sclass
        c="Exam:",self.filename
        d="Correct Answers:",self.correct_ans
        e="Marks:",self.results
        print("---------------Result-----------------")
        print(w)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        re=[w,a,b,c,d,e]

        
        with open(f'results\{self.sclass}_results.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(re)
        if os.path.exists(f'indivisual_results\{self.sname}_results.csv'):
            with open(f'indivisual_results\{self.sname}_results.csv','w') as file:
                writer = csv.writer(file)
                writer.writerow(re)
        else:
            with open(f'indivisual_results\{self.sname}_results.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(re)
        print("If You Want To Exit Press 'e'")
        print("If You Want To Go To Your Dashboard Press 'd'")
        i=input("::")

        if(i=='d'):
            s.student_info()
        else:
            exit

s=exam_managemet()
s.login()