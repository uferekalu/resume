from django.shortcuts import render
from .forms import ContactForm


def contactview(request):
  form = ContactForm(request.POST or None)
  if form.is_valid():
    email = form.cleaned_data['email']
    print(email)
  context = {
    'form': form
  }
  return render(request, 'contact/contact_form.html', context )

# # import httplib2
# # import os

# # from apiclient import discovery
# # import oauth2client
# # from oauth2client import client
# # from oauth2client import tools

# # try:
# #     import argparse
# #     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# # except ImportError:
# #     flags = None

# # SCOPES = 'https://mail.google.com/'
# # CLIENT_SECRET_FILE = 'client_secret.json'
# # APPLICATION_NAME = 'Gmail API Quickstart'


# # def get_credentials():
# #     """Gets valid user credentials from storage.

# #     If nothing has been stored, or if the stored credentials are invalid,
# #     the OAuth2 flow is completed to obtain the new credentials.

# #     Returns:
# #         Credentials, the obtained credential.
# #     """
# #     home_dir = os.path.expanduser('~')
# #     credential_dir = os.path.join(home_dir, '.credentials')
# #     if not os.path.exists(credential_dir):
# #         os.makedirs(credential_dir)
# #     credential_path = os.path.join(credential_dir,
# #                                    'gmail-quickstart.json')

# #     store = oauth2client.file.Storage(credential_path)
# #     credentials = store.get()
# #     if not credentials or credentials.invalid:
# #         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
# #         flow.user_agent = APPLICATION_NAME
# #         if flags:
# #             credentials = tools.run_flow(flow, store, flags)
# #         else: # Needed only for compatability with Python 2.6
# #             credentials = tools.run(flow, store)
# #         print('Storing credentials to ' + credential_path)
# #     return (credentials)

# # import base64
# # from email.mime.audio import MIMEAudio
# # from email.mime.base import MIMEBase
# # from email.mime.image import MIMEImage
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # import mimetypes
# # from httplib2 import Http

# # from apiclient import errors

# # from apiclient.discovery import build
# # credentials = get_credentials()
# # service = build('gmail', 'v1', http=credentials.authorize(Http()))

# # def SendMessage(service, user_id, message):
# #   """Send an email message.

# #   Args:
# #     service: Authorized Gmail API service instance.
# #     user_id: User's email address. The special value "me"
# #     can be used to indicate the authenticated user.
# #     message: Message to be sent.

# #   Returns:
# #     Sent Message.
# #   """
# #   try:
# #     message = (service.users().messages().send(userId=user_id, body=message)
# #                .execute())
# #     print 'Message Id: %s' % message['id']
# #     return message
# #   except errors.HttpError, error:
# #     print 'An error occurred: %s' % error


# # def CreateMessage(sender, to, subject, message_text):
# #   """Create a message for an email.

# #   Args:
# #     sender: Email address of the sender.
# #     to: Email address of the receiver.
# #     subject: The subject of the email message.
# #     message_text: The text of the email message.

# #   Returns:
# #     An object containing a base64 encoded email object.
# #   """
# #   message = MIMEText(message_text)
# #   message['to'] = to
# #   message['from'] = sender
# #   message['subject'] = subject
# #   b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
# #   b64_string = b64_bytes.decode()
# #   body = {'raw': b64_string}

# # testMessage = CreateMessage(sender, to, subject, body)

# # testSend = SendMessage(service, 'me', testMessage)

# from django.shortcuts import render
# from .forms import ContactForm
# from django.core.mail import send_mail
# from email.mime.text import MIMEText
# import base64
# from django.http import HttpResponseRedirect

# def SendMessage(service, user_id, message):
#   """Send an email message.

#   Args:
#     service: Authorized Gmail API service instance.
#     user_id: User's email address. The special value "me"
#     can be used to indicate the authenticated user.
#     message: Message to be sent.

#   Returns:
#     Sent Message.
#   """
#   try:
#     message = (service.users().messages().send(userId=user_id, body=message)
#                .execute())
#     print ('Message Id: %s' % message['id'])
#     return message
#   except (errors.HttpError, error):
#     print ('An error occurred: %s' % error)

# def contactview(request):
#     name=''
#     email=''
#     comment=''


#     form= ContactForm(request.POST or None)
#     if form.is_valid():
#         name= form.cleaned_data.get("name")
#         email= form.cleaned_data.get("email")
#         comment=form.cleaned_data.get("comment")
#         to = 'dekalusha@gmail.com'

#         if request.user.is_authenticated:
#             subject= str(request.user) + "'s Comment"
#         else:
#             subject= "A Visitor's Comment"


#         comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
#         # send_mail(subject, comment, 'dekalusha@gmail.com', [email])
#         message = MIMEText(comment)
#         message['to'] = to
#         message['from'] = email
#         message['subject'] = subject
#         b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
#         b64_string = b64_bytes.decode()
#         body = {'raw': b64_string}


#         context= {'form': form}

#         return HttpResponseRedirect("/SendMessage")

#     else:
#         context= {'form': form}
#         return render(request, 'contact/contact_form.html', context)
