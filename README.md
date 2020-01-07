# Python-Outlook-app.
An django based API mainly concerned with displaying mails, contacts and calendar events by calling Microsoft Outllook API 

## Register the app
  - Open a browser and navigate to the Azure Active Directory admin center. Login using a personal account (aka: Microsoft Account) or Work or School Account.

  - Select Azure Active Directory in the left-hand navigation, then select App registrations under Manage.

  - Select New registration. On the Register an application page, set the values as follows.

  - Set Name to Python Outlook Tutorial.
  - Set Supported account types to Accounts in any organizational directory and personal Microsoft accounts.
  Under Redirect URI, set the first drop-down to Web and set the value to http://localhost:8000/tutorial/gettoken/.
  Choose Register. On the Python Outlook Tutorial page, copy the value of the Application (client) ID and save it, you will need it in the next step.

  - Select Authentication under Manage. Locate the Implicit grant section and enable ID tokens. Choose Save.

  - Select Certificates & secrets under Manage. Select the New client secret button. Enter a value in Description and select one of the options for Expires and choose Add.

  - Copy the client secret value before you leave this page. You will need it in the next step.
  
  ## Setup app
  
  Replace the YOUR APP ID HERE and YOUR APP PASSWORD in authhelper.py placeholders with the values you generated in step 3 and save your     changes.
  
  ### YOUR APP IS READY TO US :+1:
