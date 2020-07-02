#!/usr/bin/env python
# coding: utf-8

# In[1]:


board=["1","2","3","4","5","6","7","8","9"]
def display(board):
    from IPython.display import clear_output
    clear_output()
    print(" -------------")
    print("| "+board[0]+" |""| "+board[1]+" |""| "+board[2]+" |")
    print(" -------------")
    print("| "+board[3]+" |""| "+board[4]+" |""| "+board[5]+" |")
    print(" -------------")
    print("| "+board[6]+" |""| "+board[7]+" |""| "+board[8]+" |")
    print(" -------------")

    


# In[2]:


def placeholders_choice():   
    placeholder=""
    while placeholder not in ["x","o"]:
        from IPython.display import clear_output
        clear_output()
        print("player 1 choose X or O")
        x=input()
        placeholder=x.lower()
        placeholder1=placeholder
        placeholder2=""
        if placeholder1=="x":
            print("player1 = x  player2=o")
            placeholder2="o"
        else:
            placeholder2="x"
            print("player1 = 0  player2=x")
    return (placeholder1,placeholder2)

    


# In[3]:



def allocation_of_first_input():
    (placeholder1, placeholder2)=placeholders_choice()
    import random
    x=random.randint(0, 1)
    if x==1:
        print("player 1 will enter first")
        return (placeholder1, placeholder2)
    else:
        print("player 2 will enter first")
        return (placeholder2, placeholder1)
    


# In[4]:


positions=["1","2","3","4","5","6","7","8","9"]
def comparison():
    if board[0]==board[1]==board[2]:
        print("{} is winner".format(board[0]))
        return 1
        
    elif board[3]==board[4]==board[5]:
        print("{} is winner".format(board[3]))
        return 1
    elif board[6]==board[7]==board[8]:
        print("{} is winner".format(board[6]))
        return 1 
    elif board[0]==board[3]==board[6]:
        print("{} is winner".format(board[0]))
        return 1 
    elif board[1]==board[4]==board[7]:
        print("{} is winner".format(board[1]))
        return 1 
    elif board[2]==board[5]==board[8]:
        print("{} is winner".format(board[2]))
        return 1 
    elif board[0]==board[4]==board[8]:
        print("{} is winner".format(board[0]))
        return 1 
    elif board[6]==board[4]==board[2]:
        print("{} is winner".format(board[6]))
        return 1 
    elif len(positions)==0:
        print("tie")
        return 0 
    else:
        return 0
        


# In[5]:



def input_position():
    condition=0
    while condition==0: 
        raw_input=""
        
        while raw_input not in positions:
            display(board)
            print("{} enter your position".format(first_placeholder))
            raw_input=input()
        position=int(raw_input)
        positions.remove(raw_input)
        board[position-1]=first_placeholder
        display(board)
        condition=comparison()
        if condition==1:
            break
        
        while raw_input not in positions:
            display(board)
            print("{} enter your position".format(second_placeholder))
            raw_input=input()
        position=int(raw_input)
        positions.remove(raw_input)    
        board[position-1]=second_placeholder
        display(board)
        condition=comparison()
        if condition==1:
            break
    
            
        
    


# In[6]:


flag=0
(first_placeholder, second_placeholder)=allocation_of_first_input()
y=[]
while y==[]:
        print("enter any key to continue")
        y=input()
display(board)
input_position()




# In[ ]:





# In[ ]:




