# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random, os

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):            # Initialization Method
        # YOUR CODE STARTS HERE
        self.cid=cid
        self.cname=cname
        self.credits=credits


    def __str__(self):                                  # Method for string representation method
        # YOUR CODE STARTS HERE
        return (f'{self.cid}({self.credits}): {self.cname}')

    __repr__ = __str__

    def __eq__(self, other):                            
        # YOUR CODE STARTS HERE
        if isinstance(other,Course):                    # If other is an instance of the course class and
            if other.cid==self.cid:                     # If the course ID of other matches to that of self instance, then returns True
                return True
            else:
                return False
        return False



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):                                 # Initialization Method
        # YOUR CODE STARTS HERE
        self.courseOfferings={}
        self.course_id = 0

    def addCourse(self, cid, cname, credits):          
        # YOUR CODE STARTS HERE
        add_course = Course(cid, cname, credits)        # An instance of the Course class is created 
        if cid in self.courseOfferings:                 # If cid is not a key in the dictionary, then it is added to the dictionary
            return (f'Course already added')
        else:
            self.courseOfferings[cid]=add_course
            return (f'Course added successfully')

         
         

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:                  # Removes the key, value pair if the course is present in the dictionaryg 
            del self.courseOfferings[cid]
            return (f'Course removed successfully')
        else:
            return (f'Course not found')

    def _loadCatalog(self, file):                        
        target_path = os.path.join(os.path.dirname(__file__), file)
        with open(target_path, "r") as f:
            course_info = f.read()
        # YOUR CODE STARTS HERE
        
        course_info=course_info.strip()
        courses=course_info.split('\n')
        for row in courses:                             # A single row containing cid, cname and credits is taken as a row
            cid, cname, credits = row.split(",")        # These three attributes are split by a comma 
            self.addCourse(cid, cname, credits)         # The addCourse method is called to add to the dicionary


        
        


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses={}



    def __str__(self):
        # YOUR CODE STARTS HERE
        if len(self.courses)==0:                        
            return (f'No courses')
        else:
            return '; '.join(self.courses.keys())           # The cnames are joined using ';'  

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:                  # Adds cid and cname as key:value pair if it is not present in the dict
            self.courses[course.cid]=course
        else:
            return (f'Course already added')


    def dropCourse(self, course):
        # YOUR CODE STARTS HERE         
        if course.cid in self.courses:
            del self.courses[course.cid]                    # Deletes cid and cname as key:value pair if it is present in the dict
        else:   
            return (f'No such course')

    @property
    def totalCredits(self):                                 # Calculates the total number of credits taken this semester
        # YOUR CODE STARTS HERE
        total=0
        for course in self.courses.values():
            total += int(course.credits)
        return total


    @property
    def isFullTime(self):                                   # Checks if the student is a Full Time student or not
        # YOUR CODE STARTS HERE
        if self.totalCredits>=12:
            return True
        else:
            return False

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount=amount
        self.loan_id = random.randint(10000,100000)     # A random integer number such that 10,000 <= x<=99999 is generated as the Loan ID


    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f'Balance: ${self.amount}')

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        if not self.loan_id :                          # Assigns a load ID to the Loan Class object when called
            self.loan_id = self.__getloanID
        return self.loan_id



class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name=name
        self.ssn=ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f'Person({self.name}, ***-**-{self.ssn[-4:]})')

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other,Person):                # Checks if the SSN of the two different objects is the same
            if self.ssn==other.ssn:
                return True
            else:
                return False
        return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)                 # inherits the attributes from Person class with super()
        self.__supervisor = supervisor


    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f'Staff({self.name}, {self.id})')


    __repr__ = __str__


    @property
    def id(self):                                  # An ID for each staff member is generated as per the instructions
        # YOUR CODE STARTS HERE
        initials=''
        names=self.name.lower()                    # First it is converted to lower case
        names=names.split()                        # Splits the name in terms of first and last name
        for n in names:
            initials+=n[0]
        four=self.get_ssn()[-4:]                   # Last four digits of the SSN are extracted
        staff_id='905'+initials+four               # The ID is formed by concatenating the data
        return staff_id

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.__supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor,Staff):      # A new supervisor is set to the supervisor property using an instance
            self.__supervisor=new_supervisor
            return (f'Completed!')
        return None


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):          # If student is an instance of the Student class (a pre-existing student)
            student.hold=True                    # A hold is placed on the student
            return (f'Completed!')
        return None

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):         # If student is an instance of the Student class (a pre-existing student)
            student.hold=False                  # The hold is removed on the student
            return (f'Completed!')
        return None

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student,Student):         # Unenrolls the student 
            student.active=False
            return (f'Completed!')
        return None


    def createStudent(self, person):            # A new student is added to the system and appropriate attributes such as name,ssn, and year are set
        # YOUR CODE STARTS HERE
        return Student(person.name, person.get_ssn(), "Freshman")



class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name, ssn)
        self.classCode=year
        self.semesters={}
        self.hold=False
        self.active=True
        self.account = self.__createStudentAccount() 


    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f'Student({self.name}, {self.id}, {self.classCode})')

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active==True:                       # This indicates that the instance of Student class can be created 
            return StudentAccount(self)             # All attributes will be defined for the active student
        return False


    @property
    def id(self):                                   # An unique ID is generated for the student
        # YOUR CODE STARTS HERE
        initials=''
        name=self.name.lower()  
        name=name.split()                           # Splits the name in terms of first and last name
        for n in name:
            initials+=n[0]
        four=self.get_ssn()[-4:]                    # Last four digits of the SSN are extracted         
        student_id=initials+four                    # The ID is formed by concatenating the data
        return student_id
    
        

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if self.hold==True or self.active==False:   # If the student is inactive or there is a hold on his account, then we won't proceed further
            return (f'Unsuccessful operation')
        else:
            if len(self.semesters) == 0:            # If the student hasn't registered to a course yet, then the student is a Freshman
                self.semesters[1] = Semester()  
                self.classCode = 'Freshman'     
            else:
                Val = max(self.semesters.keys())+1  # If student has registered before,
                self.semesters[Val] = Semester()    # then the number of semesters completed is found 
                if Val <= 2:                        # the classCode is adjusted accordingly
                    self.classCode = 'Freshman'
                elif Val <= 4:
                    self.classCode = 'Sophomore'
                elif Val <= 6:
                    self.classCode = 'Junior'
                else:
                    self.classCode = 'Senior'

                



    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        if self.active == True and self.hold == False:         # Checks if the student is eligible to enroll into any course
            sem = self.semesters[max(self.semesters.keys())]   # Stores the last semester the student has enrolled in
            if cid not in catalog.courseOfferings:
                return 'Course not found'
            obj_course = catalog.courseOfferings[cid]          # The course is added to the latest semester
            if obj_course in sem.courses.values():
                return 'Course already enrolled'
            else:
                sem.addCourse(obj_course)
                self.account.chargeAccount(self.account.CREDIT_PRICE*int(obj_course.credits))
                # The student account is charged here as per the number of enrolled courses (credit price * number of credits) 
                # by calliing the chargeAccount method on the student's account object
                return 'Course added successfully'
        else:
            return 'Unsuccessful operation'


    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if self.active == False or self.hold == True:
            return (f'Unsuccessful operation')
        else:
            sem = self.semesters[max(self.semesters.keys())]
            for c in sem.courses.keys():                       # If the course is being enrolled in the latest semester
                if c == cid :
                    drop_course = sem.courses.pop(c)           # The course is removed for the semester
                    self.account.makePayment((self.account.CREDIT_PRICE*int(drop_course.credits))/2) # Only half the price of the dropped course
                    return 'Course dropped successfully'                                             # is charged to the student account
            return 'Course not found'
            
    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if not self.active:                                    # Person not eligible to get a Loan is they're not a student
            return "Unsuccessful operation"
        
        if not self.semesters[len(self.semesters)].isFullTime:
            return "Not full-time"

        
        
        
        loan = Loan(amount)                                    # Loan object is created with the given amount
        self.account.loans[loan.loan_id] = loan                # Student account makes a payment for loan amount
        self.account.makePayment(amount)




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student=student
        self.balance=0
        self.loans={}


    def __str__(self):
        # YOUR CODE STARTS HERE
        return (f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}')

    __repr__ = __str__


    def makePayment(self, amount):                             # Makes a payment by subtracting amount from the balance.
        # YOUR CODE STARTS HERE
            self.balance-=amount
            return self.balance


    def chargeAccount(self, amount):                           # Adds amount towards the balance.
        # YOUR CODE STARTS HERE
        self.balance+=amount
        return self.balance




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(StudentAccount, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()