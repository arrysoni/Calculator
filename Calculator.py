# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

#THIS IS THE FILE TO BE SUBMITTED

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        if self.top==None:                                          # If the topmost value of the node is None, it means that the Stack is empty
            return True
        return False

    def __len__(self): 
        if self.isEmpty():
            return 0
        else:
            current=self.top
            count=0
            while current is not None:                              # If current exists, then continue the iteration
                count+=1                                            # Counts the number of nodes
                current=current.next
            return count

    def push(self,value):
        nn= Node(value)
        if self.isEmpty():
            self.top=nn                                           # Sets the value to the topmost node
        else:
            nn.next=self.top                                        # Else pushes an element into the Stack
            self.top=nn

     
    def pop(self):
        if self.isEmpty():                                          # Nothing to pop here
            return None
        else:
            top=self.top.value
            self.top=self.top.next
            return top                                              # Removes the topmost value of the node


    def peek(self):                                                 # Returns the topmost value of the node without deleting it
        if self.isEmpty():
            return None
        return self.top.value                   


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):                        # This function uses exception handling to check whether an expression can be converted to float or not
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        try:
            float(txt)
        except:
            return False
        return True
        
    
    
    
    def sign_check(self,txt):                       # This function checks whether the element of the
        try:
            float(txt)
            if '+' in txt or '-' in txt:
                 return False
        except:
            return False
        return True

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3) ^ 2 + (1 +4 ))))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
        '''
        precedences={'^':1, '*':2 , '/':2 ,'+':3 ,'-':3 ,'(':4, None:5}             # A dictionary that defines the preferences of all the operators

        new_list=self.tokenizer(txt)                                                # Our list of tokens

        postfixStack= Stack()

        temp_str=''

        for i in range(len(new_list)):

            if new_list[i] in '+-*/^':                                          

                if postfixStack.isEmpty():
                    postfixStack.push(new_list[i])                                             # We directly push the elements in the Stack if it is empty

                else:

                    if precedences[postfixStack.peek()]>precedences[new_list[i]]:              # Lower precedence elements (according to my dict) are pushed in
                        postfixStack.push(new_list[i])

                    elif postfixStack.peek()=='^' and new_list[i]=='^':                        # A special case where we push '^' into the Stack if the topmost element is also '^'
                        postfixStack.push(new_list[i])                                         # One of the TAs told me about it

                    elif precedences[postfixStack.peek()]<precedences[new_list[i]]:            
                        while precedences[postfixStack.peek()]<=precedences[new_list[i]]:      # Element is popped till the element to be pushed has a lower preference (as per my dict)
                            pop= postfixStack.pop()
                            temp_str+=' '                                                      # These popped elements are stored in a temporary string that will be pushed as a whole
                            temp_str+=pop
                            temp_str+=' '
                        postfixStack.push(new_list[i])

                    else:
                        pop=postfixStack.pop()                                                 # Directly popped and pushed with appropriate spacing added to it
                        temp_str+=' '
                        temp_str+=pop
                        temp_str+=' '
                        postfixStack.push(new_list[i])
                    

            elif new_list[i]=='(':                                                             # Directly pushed in the Stack
                postfixStack.push(new_list[i])

            elif new_list[i]==')':                                                             # If this element is encountered, all the elements within are popped out
                if postfixStack.peek()=='(':                                                   # And then pushed to the Stack as per the conditions
                    postfixStack.pop()

                else:
                    while postfixStack.peek()!='(':
                        pop=postfixStack.pop()
                        temp_str+=' '
                        temp_str+=pop
                        temp_str+=' '
                    postfixStack.pop()
                
                

            else:
                temp_str+=(' '+new_list[i]+' ')                                             # Any other operands here are added to the temporary string with spaces

        while postfixStack.isEmpty()!=True:                                                 # All the remaining elements are popped and added to the string
            pop=postfixStack.pop()
            temp_str+=(' '+pop+' ')

        temp_str=temp_str.split()                                               
        return ' '.join(temp_str)                                                           # Returns the postfix expression

    def tokenizer(self,txt):                                                                                # This function tokenizes the operators and operands
        new_lst=txt.split()
        
        for i in range(len(new_lst)):
            flag=self._isNumber(new_lst[i])
            if flag==False:                                                                                 # If the element is not an expression,
                temp=''
                for j in range(len(new_lst[i])):
                    if len(new_lst[i])==1 and new_lst[i][0]=='-':                                           # Case:  '-2'
                        temp+= (' ' + new_lst[i][j] + ' ')                                                  # Adds spaces: ' -2 '
                    elif len(new_lst[i])==2 and new_lst[i][0]=='-' and self._isNumber(new_lst[i][1]):       
                        temp+= (new_lst[i][j])
                    elif new_lst[i][j]=='-':
                        if self._isNumber(new_lst[i][j+1]) and self._isNumber(new_lst[i][j-1]):             # The element preceeding and succeeding '-' is a number
                            temp+=(' ' + new_lst[i][j] + ' ')                                               # Add spacing
                        elif not self._isNumber(new_lst[i][j+1]):                                           # Adds spacing regardless
                            temp+=(' ' + new_lst[i][j] + ' ')
                        else:
                            temp+=new_lst[i][j]                                                             # Adding spaces not required here
                    elif new_lst[i][j] in '+*/()^':
                        temp+=(' ' + new_lst[i][j] + ' ')
                    else:
                        temp+=new_lst[i][j]                                                                 # Numbers and other symbols
                new_lst[i]= temp
        new_str= ' '.join(new_lst)                                                                          # We get a string where the required elements are separated by a white space
        new_lst=new_str.split()     

        

        for element in range(len(new_lst)):                                                                 # Converts the number into float number 
            if self.sign_check(new_lst[element]):                                                           # Converts to float and then to string only if our expression is valid
                new_lst[element]=str(float(new_lst[element]))
        return new_lst


    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None
        
        lst = self.tokenizer(self.__expr)                          # Tokenized List

        for i in range(len(lst)):
            flag=self._isNumber(lst[i])
            if flag==False:                                         # We are dealing with operators
                if lst[i] not in '+-*/()^':                         # Checks for invalid operators
                  return None
        for i in range(len(lst)-1):                                 # Checks for missing operands
            if lst[i] in '+-*/(' :                      
                if (lst[i+1]!='('):                         
                    if (lst[i+1]!=')'):
                        flag=self._isNumber(lst[i+1])              # Case: 4+(  -->invalid case
                        if flag==False :
                            return None
        if lst[-1] in '+-*/(^':                                    # Expression must not end with an operator or an open parenthesis
            return None
        for i in range(len(lst)-1):                                # Two consecutive operators not allowed
            flag=self._isNumber(lst[i])
            if flag==True:
                if self._isNumber(lst[i+1]):
                    return None
        
        for i in range(len(lst)-2):                                                       # Checks for implied multiplication
            if (self._isNumber(lst[i])) and (lst[i+1] in '('):                            # Case: 3(1)
                return None
            elif (lst[i].isdigit() and lst[i+1]=='>})]') and (lst[i+2].isdigit()):        # Case: (2)1
                return None                                                                       
            elif (lst[i]==')' and lst[i+1]=='('):                                         # Case: (3)(5)
                return None       
            
        left= 0 
        right=0 

        for i in range(len(lst)):                                                         # Checking for unbalanced parenthesis
            if lst[i]=='(':
                left+=1
            if lst[i]==')':
                right+=1
            if right>left:                                                                                       
                return None

        
        calcStack = Stack()  

        expression= self._getPostfix(self.__expr)

        exp_lst= expression.split()

        for i in range(len(exp_lst)):
            flag=self._isNumber(exp_lst[i])             # An operand is directly pushed into the Stack
            if flag:
                calcStack.push(exp_lst[i])
            else:
                op2= float(calcStack.pop())             # op2 & op1 are the first two topmost elements of the list
                op1= float(calcStack.pop())
                if exp_lst[i]=='+':                     # The required operations are performed
                    ans=op1+op2
                elif exp_lst[i]=='-':
                    ans=op1-op2
                elif exp_lst[i]=='*':
                    ans=op1*op2
                elif exp_lst[i]=='/':
                    ans=op1/op2
                elif exp_lst[i]=='^':
                    ans=op1**op2
                
                ans=float(ans)
                calcStack.push(ans)
        
        output= calcStack.pop()
        if isinstance(output,str):                  # If the popped element is a string, we convert it into float
            output=float(output)
        return output
    


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
      >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        word=word.strip()
        if len(word)==0:                        # If the word is an empty string, returns False
            return False
        else:
            if word[0].isalpha():               # The first character of the varibale must be an alphabet
                if word.isalnum():              # The word as a whole must have only numbers and alphabets
                    return True
                return False
            else:
                return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        expr=expr.strip()
        expr_list=expr.split()

        for i in range(len(expr_list)):    
            if self._isVariable(expr_list[i]):        
                if  expr_list[i] not in self.states:                    # The variable must exist as a key in the dictionary
                    return None
                else:
                    expr_list[i]=str(self.states[expr_list[i]])     # The value of the variable is replaced with the variable

        return ' '.join(expr_list)

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        lst = self.expressions.strip().split(';')
        dict = {}                                               # This dictionary keeps track of the expression and the current value of self.states

        for i in range(len(lst)):
            if ('=' in lst[i]):
                l_hand_side=lst[i].split('=')[0].strip()    # The left hand side variable stores the variable part of the expression
                if self._isVariable(l_hand_side) == False:    # It checks if it is a valid variable name or not
                    self.states = {}
                    
                r_hand_side=lst[i].split('=')[1].strip()    # Stores the actual expression
                expr = self._replaceVariables(r_hand_side)    # If the expression has variables that may have values, those variables are replaced with the values
                calcObj.setExpr((expr))                       
                self.states[l_hand_side]= calcObj.calculate 
                dict[lst[i]]= self.states.copy()              
            
            if ('return' in lst[i]):                       
                line=lst[i].replace('return ','')          # We do not want the keyword 'return' in our final dictioonary 
                line=self._replaceVariables(line)
                calcObj.setExpr(line)                         
                dict['_return_']=calcObj.calculate        # The final evaluation of the expression is stored as the value to the keyword '_return_'
        
        return dict


def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(AdvancedCalculator, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()



