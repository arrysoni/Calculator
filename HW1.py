# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math
def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
        
    """
    #- YOUR CODE STARTS HERE

    width=(perimeter-math.sqrt(perimeter**2-16*area))/4     # The width of the rectangle was found by placing it in the discriminant equation
    breadth=area/width                                      # The breadth is the other side of the rectangle

    if breadth.is_integer() and width.is_integer():         # Checking if both sides are integers
        if width>breadth:
            return round(int(width))                        
        else:                                               # Rounding off the sides
            return round(int(breadth))
        
    else:
        return False
    


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    count=0
    dec_num=0
    while oct_num>0:
        rem=oct_num%10                                      # Getting the remiander ( last digit ) of the octal number
        dec_num+=(rem*(8**count))                           # Decimal Number = Decimal Number + (last digit * 8^(the number of iterations))
        oct_num=oct_num//10                                 
        count+=1                                            # Counting the number of digits in the octal number

    return dec_num



def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE

    if num<0:
        num=num*(-1)                                        # Converts the number to a positive if it is negative
    
    
    if num<=100:                                            # The number shouldn't be a two or one digit number
        return False
    else:

        while (num>=100):                               
            rem=num%10                                      # Gets the remainder of the number
            sig_dig=(num//100)%10                           # Significant digits stored
            if rem==sig_dig:
                return True
            else:
                num=num//10
    return False
   

def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    least_sig=None
    new_num_1=0
    new_num_2=0

    while(num_1)>0:                                     
        rem=num_1%10                     
        num_1=num_1//10

        if rem!=least_sig:
            new_num_1=new_num_1*10+rem                      # new_num_1 is updated
            least_sig=rem                                   # least significant digit is updated
    least_sig=None

    while(num_2)>0:                                         # The same process is done for num_2
        rem=num_2%10
        num_2=num_2//10

        if rem!=least_sig:
            new_num_2=new_num_2*10+rem
            least_sig=rem
    

    if new_num_1==new_num_2:                                # Checks if the new numbers are the same
        return True
    else:
        return False


        
         

        
        
 



def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    seq=[num]                                               # Adds the first digit to the list
    while num!=1:
        if(num%2==0):                                       # If the number is even, then the half of it is appended to the list
            n=num//2
            seq.append(n)
        else:
            n=3*num+1                                       # If the number is odd, then the appended digit uses a different formula
            seq.append(n)
        num=n
    return seq     



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    '''
    for item in d.keys():
        if item==key:
            d[item]=[d[item],value]     isinstance(d[key],list):
        else:
            d[key]=value
        
            '''
    if key not in d.keys():
        d[key]=value                                        # Creates a new key: value pair if it wasn't pre-existing
    else:
        if d[key] in d:                     
            d[key]+=[value]                                 # Adds a new value in the form of a list to pre-existing key:value pair
        else:
            d[key]=[d[key],value]                           # Creates a new key:value pair
        
        
        


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE

    new_D={}
    dic={}
    for key in d.keys():            
        dept=d[key]['department']                           # Stores the department name
        dic={'emp_id':key,'name':d[key]['name'],'position':d[key]['position']} #Stores the details of the employee in form of a dictionary

        if dept not in new_D:
            
            
            new_D[dept] = [dic]                             # Creates a new key department and uses the details as key 
           
        else:
            
            new_D[dept].append(dic)                         # Adds employee details in a pre- existing department dictionary
            
    return new_D
            
        
    



def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()
        contents=contents.split()
        for t in range(len(contents)):
            if not contents[t].isalnum():
                contents[t]=list(contents[t])
                for j in range(len(contents[t])):
                    if not contents[t][j].isalnum():
                        contents[t][j]=" "+contents[t][j]+" "
                contents[t]="".join(contents[t])
        contents=" ".join(contents)
        contents=contents.split()
        d={".":[contents[0]]}
        for i in range(len(contents)-1):
            if contents[i] in d:
                if not contents[i+1] in d[contents[i]]:
                    d[contents[i]]+= [contents[i+1]]
            else:
                d[contents[i]]= [contents[i+1]]
        return d


def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    branch=trie
    for i in word:                                          # For a character in word,
       
        if i in branch:                                     # If the character is a key in the dictionary, then that dictionary will become a value to a new dictionary
            branch=branch[i]        
            
        else:
            branch[i]={}                                    # Else a new dictionary will be created with a new key
            branch=branch[i]                                # then that dictionary will become a value to a new dictionary
           
    branch["word"]=True
    return None




def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    #file_path = get_path(file_name)
    with open(file_name, 'r') as file:   
          # You might change .read() for .readlines() if it suits your implementation better 
        lst=[]
        contents = file.read()
        lst=contents.split()
            
        trie={}
        for i in range(len(lst)):
            addToTrie(trie,lst[i])                          # Sends the list of words to addToTrie to create a new dictinary
    return trie

        

            
    
               



def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    
    branch=trie
    for i in word:
        if i in branch:
            branch=branch[i]                                # Creates a new dictionary with the old dictionary as value
        else:
            return False
    return True
 



def run_tests():
    import doctest
    # Run start tests in all docstrings
    # doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(by_department, globals(), name='HW1',verbose=True)   






if __name__ == "__main__":
    run_tests()