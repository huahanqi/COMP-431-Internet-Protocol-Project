# COMP431 (Internet Protocol) Project

This is the final project for COMP 431 (Internet Protocol Project). 

In this final Project, I built a prototype of an email server from scratch using Python. This email server enables users to send/receive email under SMTP protocol from linux command lines. While in reality, both sides are able to send and receive emails; In this prototype, Server is the one to send email, and Client is the one to receive email. 

The system would automatically pop up to suggest users what information to type in (such as "From Whom", "To Whom", and "Message" etc.). If you type the contents in the wrong format(e.g. wrong format for email address), the system would complain and ask to type in again. At the end of content, user must to use "." to indicate the end of message. After this indication, the email server would send this message to the indicated destination server. 

All the sent and received emails are recorded in txt file and managed under the respective file folders.
