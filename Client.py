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

import sys
error = False
error_message  = ""
# Try to get MAIL FROM from user prompt
from_whom = input("From:\n")
i = 0
user_input = "MAIL FROM: <" + from_whom[0:len(from_whom)] + ">" +'\n'
length = len(user_input)
check_MAIL_FROM()
while (error):
    print(error_message)
    error = False
    error_message = ""
    i = 0
    from_whom = input("From:\n")
    user_input = "MAIL FROM: <" + from_whom[0:len(from_whom)] + ">" +'\n'
    length = len(user_input)
    check_MAIL_FROM()
FROM_final = from_whom



# Try to get RCPT TO from user prompt
to_whom = input("To:\n")
TO_final_list = []
mylist = to_whom.split(',')
to_whom_list = [x.strip() for x in to_whom.split(',') if mylist != ""]

for k in range(0,len(to_whom_list)):
    i = 0
    to_whom_single = to_whom_list[k]
    user_input = "RCPT TO: <" + to_whom_single[0:len(to_whom_single)] + ">" +"\n"
    length = len(user_input)
    check_RCPT_TO()
    if(error):
        print(error_message)
        TO_final_list = []
        break
    else: 
        TO_final_list.append(to_whom_single)

while(error):
    to_whom = input("To:\n")
    mylist = to_whom.split(',')
    to_whom_list = [x.strip() for x in to_whom.split(',') if mylist != ""]
    for k in range(0,len(to_whom_list)):
        error = False
        error_message = ""
        i = 0
        to_whom_single = to_whom_list[k]
        user_input = "RCPT TO: <" + to_whom_single[0:len(to_whom_single)] + ">" +'\n'
        length = len(user_input)
        check_RCPT_TO()
        if(error):
            print(error_message)
            TO_final_list = []
            break
        else: 
            TO_final_list.append(to_whom_single)



# Try to get SUBJECT from user prompt
subject = input("Subject:\n")

# Try to get Message from user prompt:
Message = []
first = input("Message:\n")
Message.append(first)
while True:
    line = input()
    if(line == "."):
        break
    else:
        Message.append(line)



# put all the information together to form DATA
data = []
data.append('From: <' + FROM_final + '>')
TO_final_bracket = []
for i in range(0,len(TO_final_list)):
    TO_final_bracket.append("<" + TO_final_list[i] + ">")
joined_string = ", ".join(TO_final_bracket)
data.append('To: ' + joined_string)
data.append('Subject: ' + subject + '\n')
for i in Message:
    data.append(i)

from socket import *
transmit = False
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

greeting_message = clientSocket.recv(1024).decode()
if(greeting_message == "220 comp431fa21b.cs.unc.edu"):
    print("Got greeting message from the server!")
    greeting_message2 = "HELO comp431fa21.cs.unc.edu"
    clientSocket.send(greeting_message2.encode())
    print("Sent greeting message 2 to the server!")

greeting_message3 = clientSocket.recv(1024).decode()
if(greeting_message3 == "250 Hello comp431fa21.cs.unc.edu pleased to meet you"):
    print("Got greeting message3 from the server! Ready to transmit")
    transmit = True

#Begin to transmit: 
current_state = "START"
rcpt_index = 0
data.append(".")
k = 0
while (transmit):
    print("The current state is: " + current_state)
    if(current_state == "START"):
        sentence = "MAIL FROM: <" + FROM_final + ">"
        print("send this to the server:", sentence)
        clientSocket.send((sentence+'\n').encode())
        current_state = "MAIL"
    elif(current_state == "MAIL"):
        sentence = "RCPT TO: <" + TO_final_list[rcpt_index] + ">"
        print("send this to the server:", sentence)
        clientSocket.send((sentence+'\n').encode())
        rcpt_index+=1
        current_state = "RCPT"
    elif(current_state == "RCPT"):
        if(rcpt_index >= len(TO_final_list)):
            current_state = "DATA"
            continue
        else:
            sentence = "RCPT TO: <" + TO_final_list[rcpt_index] + ">"
            print("send this to the server:", sentence)
            clientSocket.send((sentence+'\n').encode())
            rcpt_index+=1
    elif(current_state == "DATA") :
        sentence = "DATA"
        print("send this to the server:", sentence)
        clientSocket.send((sentence+'\n').encode())
        current_state = "SENT DATA"
    elif(current_state == "Message"):
        if(k < len(data)):
             sentence = data[k]
             k += 1
             print("send this to the server:", sentence)
             clientSocket.send((sentence+'\n').encode())
             continue
    
    response = clientSocket.recv(1024).decode()
    if(response == "221 comp431fa21b.cs.unc.edu closing connection"):
        print('From Server:', response)
        break
    elif((response[0:3] == "250") & (current_state == "MAIL")):
        print('From Server:', response)
    elif((response[0:3] == "250") & (current_state == "RCPT")):
        print('From Server:', response)
    elif((response[0:3] == "354") & (current_state == "SENT DATA")):
        print('From Server:', response)
        current_state = "Message"
    elif((response[0:3] == "250") & (current_state == "Message")):
        print('From Server:', response)
        sentence = "QUIT"
        clientSocket.send(sentence.encode())
        current_state = "Finish"
    else:
        print('From Server:', response)
        sentence = "QUIT"
        clientSocket.send(sentence.encode())
        current_state = "Error"


clientSocket.close()
