import re
import pandas as pd
import email

emails = []

fh = open(r"test_emails.txt", "r").read()

contents = re.split(r"From r",fh)
contents.pop(0)

for item in contents:
 emails_dict = {}

 sender = re.search(r"From:.*", item)

 if sender is not None:
  s_email = re.search(r"\w\S*@.*\w", sender.group())
  s_name = re.search(r":.*<", sender.group())
 else:
  s_email = None
  s_name = None

 if s_email is not None:
  sender_email = s_email.group()
 else:
  sender_email = None

 emails_dict["sender_email"] = sender_email

 if s_name is not None:
  sender_name = re.sub("\s*<", "", re.sub(":\s*", "", s_name.group()))
 else:
  sender_name = None

 emails_dict["sender_name"] = sender_name

 recipient = re.search(r"To:.*", item)

 if recipient is not None:
  r_email = re.search(r"\w\S*@.*\w", recipient.group())
  r_name = re.search(r":.*<", recipient.group())
 else:
  r_email = None
  r_name = None

 if r_email is not None:
  recipient_email = r_email.group()
 else:
  recipient_email = None

 emails_dict["recipient_email"] = recipient_email

 if r_name is not None:
  recipient_name = re.sub("\s*<", "", re.sub(":\s*", "", r_name.group()))
 else:
  recipient_name = None

 emails_dict["recipient_name"] = recipient_name

 date_field = re.search(r"Date:.*", item)

 if date_field is not None:
  date = re.search(r"\d+\s\w+\s\d+", date_field.group())
 else:
  date = None

 if date is not None:
  date_sent = date.group()
 else:
  date_sent = None

 emails_dict["date_sent"] = date_sent

 subject_field = re.search(r"Subject: .*", item)

 if subject_field is not None:
  subject = re.sub(r"Subject: ", "", subject_field.group())
 else:
  subject = None

 emails_dict["subject"] = subject

 # "item" substituted with "email content here" so full email not displayed.

 full_email = email.message_from_string(item)
 body = full_email.get_payload()
 emails_dict["email_body"] = "email body here"

 emails.append(emails_dict)

# Print number of dictionaries, and hence, emails, in the list.
print("Number of emails: " + str(len(emails)))

print("\n")

# Print first item in the emails list to see how it looks.
for i in range(len(emails)):
 for key, value in emails[i].items():
  print(str(key) + ": " + str(value))
 print('\n')