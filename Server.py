def check_MAIL():
   global i
   global error
   global error_message
   if((4<= length) &(user_input[i:4] == 'MAIL')):
       i = i + 4
   else: 
       error = True
       error_message = "ERROR -- mail-from-cmd"

# check white space
def check_white_space():
    global i
    global error
    global error_message
    if((i< length) & ((user_input[i] == " ") |(user_input[i] == "\t"))):
        i+=1
        check_space()
    else:
        error = True
        error_message = "ERROR -- whitespace-mail-from-cmd"

# check space
def check_space():
    global i
    global error
    global error_message
    if((i< length) & ((user_input[i] == " ") |(user_input[i] == "\t"))):
        i+=1
        check_space()
    elif((i< length) & user_input[i].isalpha()):
        return
    else:
        error = True
        error_message = "ERROR -- whitespace-mail-from-cmd"

# check from
def check_from():
    global i
    global error
    global error_message
    if((i+5 < length) & (user_input[i:i+5] == 'FROM:')): 
        i = i+5
    else:
        error = True
        error_message = "ERROR -- mail-from-cmd"

# check null space
def check_null_space_1():
    global i 
    global error
    global error_message
    if((i< length) &((user_input[i] == " ") | (user_input[i] == "\t"))):
        i += 1
        check_null_space_1()
    elif((i< length) &((user_input[i] == "<"))):
        return
    else:
        error = True
        error_message = "ERROR -- path"

#check reverse path
def check_reverse_path():
    check_path()

#check path
def check_path():
    global i
    global error
    global error_message
    if( (i< length) & (user_input[i] == '<')):
        i+=1
        check_mail_box()
        if(error_message != ""):
            return
        if((i< length) & (user_input[i] == '>')):
            return
        else:
            error = True
            error_message = "ERROR -- path"
    else:
        error = True
        error_message = "ERROR -- path"

#check_mail_box
def check_mail_box():
    check_local_part()
    check_domain()

#check_local_part
def check_local_part():
    global i
    global error
    global error_message
    if((i< length) & (user_input[i] == '@')):
        error = True
        error_message = "ERROR -- mailbox"
    else:
        check_string()

#check_string
def check_string():
    check_char()

#check char
def check_char():
    global i
    global error
    global error_message
    if((i< length) & (user_input[i] == '@')):
        i+=1
        return
    if((i< length) & ((user_input[i] == " ") | (user_input[i] == "\t"))):
        error = True
        error_message = "ERROR -- mailbox"
        return
    if((i< length) & (user_input[i].isprintable())):
        if(is_special(user_input[i])):
            error = True
            error_message = "ERROR -- mailbox"
        else:
            i+=1
            check_char()
    else:
        error = True
        error_message = "ERROR -- mailbox"

#check_domain
def check_domain():
     global i
     global error
     global error_message
     if((i< length) & (~user_input[i].isalpha())):
         error = True
         error_message = "ERROR -- mailbox"
         return
     else:
        check_element()
        if(error_message != ""):
            return
        if((i< length) & (user_input[i] == '>')):
            return
        else: 
            error = True
            error_message = "ERROR -- path"

     
#check_element
def check_element():
    global i
    global error
    global error_message
    if((i< length) & (user_input[i] == '.')):
         error = True
         error_message = "ERROR -- mailbox"
         return
    elif((i< length) & (user_input[i].isdigit())):
         error = True
         error_message = "ERROR -- mailbox"
         return
    else:
        check_letter()
        check_name()

#check_name
def check_name():
   check_letter()
   check_let_dig_str()

#check_letter
def check_letter():
   global i
   global error
   global error_message
   if(error_message != ""):
       return
   if((i< length) & (user_input[i] == ">")):
       return
   if((i< length) & (user_input[i] == "\n") or (user_input[i] == " ") or
        (user_input[i] == "\t")):
       return 
   if((i< length) & (~user_input[i].isalnum()) & (~(user_input[i] == '.'))):
       error = True
       error_message = "ERROR -- mailbox"
       return
   if((i< length) & (user_input[i].isalpha())):
       i+=1
       check_letter()
   elif((i< length) & (user_input[i].isalnum())):
       i+=1
       check_let_dig_str()
   elif((i< length) & (user_input[i] == ".")):
       i+=1
       check_domain()
   else:
       error = True
       error_message = "ERROR -- path"

#check_let_dig_str
def check_let_dig_str():
   global i
   global error
   global error_message
   if(error_message != ""):
       return
   if((i< length) & (user_input[i].isalnum())):
       i+=1
       check_let_dig_str()
   elif((i< length) & (user_input[i] == '.')):
        i+=1
        check_domain()
   elif((i< length) & (user_input[i] == ">")):
        return
   else:
        error = True
        error_message = "ERROR -- path"

#check_Null_space_2
def check_null_space_2():
    global i 
    global error
    global error_message
    if((i+1 < length) &((user_input[i+1] == " ") | (user_input[i+1] == "\t"))):
        i += 1
        check_null_space_2()
    elif((i+1 < length) &((user_input[i+1] == "\n"))):
        return
    else:
        error = True
        error_message = "ERROR -- nullspace"

# this function check if the character is special 
def is_special(x):
    if (x == "<" or x == ">" or x == "(" or 
    x == ")" or x == "[" or x == "]" or 
    x == "\\" or x == "." or x == "," or 
    x == ";" or x == ":" or x == "@" or x == '"'):
        return True
    else:
        return False



# check MAIL FROM
def check_MAIL_FROM():
    global i
    global error
    global error_message
    check_MAIL()
    if(error):
        return
    check_white_space()
    if(error):
        return
    check_from()
    if(error):
        return
    check_null_space_1()
    if(error):
        return
    check_reverse_path()
    if(error):
        return
    check_null_space_2()
    if(error):
        return


# check RCPT
def check_RCPT():
   global i
   global error
   global error_message
   if((4<= length) &(user_input[i:4] == 'RCPT')):
       i = i + 4
   else: 
       error = True
       error_message = "ERROR -- mail-from-cmd"


# check TO
def check_TO():
    global i
    global error
    global error_message
    if((i+3 < length) & (user_input[i:i+3] == 'TO:')): 
        i = i+3
    else:
        error = True
        error_message = "ERROR -- mail-from-cmd"


def check_forward_path():
    check_path()

# check RCPT TO command
def check_RCPT_TO():
    global i
    global error
    global error_message
    check_RCPT()
    if(error):
        return
    check_white_space()
    if(error):
        return
    check_TO()
    if(error):
        return
    check_null_space_1()
    if(error):
        return
    check_forward_path()
    if(error):
        return
    check_null_space_2()
    if(error):
        return

# check DATA command
def check_DATA():
    global user_input
    global error
    global error_message
    global i
    if(user_input[0:4] == 'DATA'):
        i = 3
        check_null_space_2()
    else: 
        error = True
        error_message = "ERROR -- mail-from-cmd"

# check which command to check
def check_command():
    global user_input
    global error
    global error_message
    global next
    global file_name
    global begin_append
    global forward
    global from_whom
    global data_input
    global response

    if(user_input[0:4] == "MAIL"):
        check_MAIL_FROM()
        if((error_message == "ERROR -- mail-from-cmd") | 
        (error_message == "ERROR -- whitespace-mail-from-cmd")):
            response = "500 Syntax error: command unrecognized"
        elif(next != "MAIL"):
            response = "503 Bad sequence of commands"
        elif(error_message != ""):
            response = "501 Syntax error in parameters or arguments"
        elif(error_message == ""):
            next = "RCPT"
            from_whom = truncate(user_input[0:len(user_input)-1])
            response = "250 OK"
        else:
            response = "501 Syntax error in parameters or arguments"
    elif(user_input[0:4] == "RCPT"):
        check_RCPT_TO()
        if((error_message == "ERROR -- mail-from-cmd") | 
        (error_message == "ERROR -- whitespace-mail-from-cmd")):
            response = "500 Syntax error: command unrecognized"
        elif((next != "RCPT") & (next != "RCPT or DATA")):
            response = "503 Bad sequence of commands"
        elif(((next == "RCPT") | (next == "RCPT or DATA")) & (error_message != "")):
            response = "501 Syntax error in parameters or arguments"
        elif((next == "RCPT") & (error_message == "")):
            next = "RCPT or DATA"
            forward_name = truncate(user_input[0:len(user_input)-1])
            forward.append(forward_name)
            name = "forward/" + truncate_domain_name(user_input[0:len(user_input)-1])
            if(not (name in file_name)):
                file_name.append(name)
            response = "250 OK"
        elif((next == "RCPT or DATA") & (error_message == "")):
            forward_name = truncate(user_input[0:len(user_input)-1])
            forward.append(forward_name)
            name = "forward/" + truncate_domain_name(user_input[0:len(user_input)-1])
            if(not (name in file_name)):
                 file_name.append(name)
            response = "250 OK"
        else:
            response = "501 Syntax error in parameters or arguments"
    elif(user_input[0:4] == "DATA"):
        check_DATA()
        if((error_message == "ERROR -- mail-from-cmd") |
        (error_message == "ERROR -- nullspace")):
            response = "500 Syntax error: command unrecognized"
        elif(next != "RCPT or DATA"):
            response = "503 Bad sequence of commands"
        elif(error_message!= ""):
            response = "501 Syntax error in parameters or arguments"
        else:
            data_input = True
            next = "MAIL"
            response = "354 Start mail input; end with <CRLF>.<CRLF>"
    elif(((len(user_input)==2) & (user_input[0:2]== ".\n")) |
    ((len(user_input)>2) & (user_input[(len(user_input)-2):len(user_input)] == ".\n") &
    (user_input[len(user_input)-3] == "\n"))):
        return
    else:
        response = "500 Syntax error: command unrecognized"

def truncate(string):
    output = ""
    for i in range(len(string)):
        if(string[i] == "<"):
            for j in range(i+1,len(string)):
                if(string[j] != ">"):
                    output += string[j]
                else:
                    break
    return(output)

def truncate_domain_name(string):
    output = ""
    for i in range(len(string)):
        if(string[i] == "@"):
            for j in range(i+1,len(string)):
                if(string[j] != ">"):
                    output += string[j]
                else:
                    break
    return(output)

def check_finish():
    global user_input
    global data_input
    global forward
    global from_whom
    global file_name
    global begin_append
    global data_list
    global response
    
    if (((data_input == True) & (len(user_input)==2) & (user_input[0:2]== ".\n")) | 
    ((data_input == True) & (len(user_input)>2) & (user_input[(len(user_input)-2):len(user_input)] == ".\n") & 
    (user_input[len(user_input)-3] == "\n"))):
        data_input = False
        response = "250 OK"
        for n in file_name:
                    f = open(n, "a")
                    for data in data_list:
                        f.write(data)
                    f.close()
        forward = []
        from_whom = ""
        file_name = []
        data_list = []
    elif((data_input != True) & (user_input[0:2] == ".\n")):
        response = "500 Syntax error: command unrecognized"


import sys
from socket import *
next = "MAIL"
data_input = False
from_whom = ""
forward = []
begin_append = False
file_name = []
data_list = []
response = ""

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is listening for connection!')
while True:
    connectionSocket, addr = serverSocket.accept()
    print ('Got connection from', addr)
    greeting_message = "220 comp431fa21b.cs.unc.edu"
    connectionSocket.send(greeting_message.encode())
    print("Sent greeting_message 1 to the client!")
    greeting_message2 = connectionSocket.recv(1024).decode()
    if(greeting_message2 == "HELO comp431fa21.cs.unc.edu"):
        print(greeting_message2)
        greeting_message3 = "250 Hello comp431fa21.cs.unc.edu pleased to meet you"
        connectionSocket.send(greeting_message3.encode())
    
    while True:
        sentence = connectionSocket.recv(1024).decode()

        if sentence == "QUIT":
            print("got QUIT from the client!")
            end_message = "221 comp431fa21b.cs.unc.edu closing connection"
            connectionSocket.send(end_message.encode())
            break
        else:
            user_input = sentence
            print(user_input[0:len(user_input)-1])
            i = 0
            error = False
            error_message = ""
            length = len(user_input)
            check_finish()
            print(data_input)
            if(data_input):
                data_list.append(user_input)
            else:
                check_command()
                print("send this to the client:", response)
                connectionSocket.send(response.encode())
    data_input = False
    connectionSocket.close()
