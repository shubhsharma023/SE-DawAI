**Software Requirements Specification**

**for**

**DawAI**

**Version 1.0 approved**

**10 October 2022**

**Table of Contents**

1. # Project Selection Base

1) 1) # Software Bid

**Software Bid/ Project Teams**

**UCT 305- Software Engineering Lab**


# 1.2 Project Overview

The purpose of this document is to provide a correct and complete description of the requirements for the software of DawAI. The requirements will be shown in a written description to explain various concepts and different types of functionalities with relevant information.

Main features of our website portal DawAI are:

- DawAI focuses on providing advice to the client to find their medicine in emergency cases on the basis of their symptoms (predictable) and help them to connect to the medical practitioner.

- DawAI advises the client about the yoga practices which they can perform to cure the uneasiness in the long run. DawAI also focuses on providing childcare advice for their initial development and helping clients to suggest and connect to pediatricians.

- DawAI also helps you to get lab tests in easy steps.

Every day many people suffer with many of the health problems or for better healthcare. The software of DawAI is responsible in making the people to take better healthcare decisions and health related issues. This will help the client in finding the better suggestions regarding health from the best doctors and also help the client to somewhat cure or reduce the uneasiness caused by the illness by suggesting them medicine based on their symptoms.

By this software DawAI, people start finding the help from the best doctors which can be managed by single health care account for the entire family. It also secures all the sensitive information regarding the healthcare data so as to make better healthcare decisions from past reports also. This software is looking to simplify healthcare access and help you to make healthcare decisions. With search, we help you to find and decide on the right healthcare providers across doctors, hospitals and diagnostics and provide easy steps lab tests. Every day billions of people struggle for better healthcare. We are on a mission to help mankind to live healthier and longer. This software also has scope in childcare facility which they all seek in their initial stages.

1. 3. # References

- **Net meds** **–**

_<https://www.netmeds.com/healthstore?source_attribution=ADW-CPC-Search-PY-Generic&utm_source=ADW-CPC-Search-PY-Generic&utm_medium=CPC&utm_campaign=ADW-CPC-Search-PY-Generic&gclid=Cj0KCQiAgribBhDkARIsAASA5buOSsHAbTUu2M3Fc4FsgP0QThlLfz7nzrFvo5R9aPmz5vfrHTv53ScaAp0LEALw_wcB>_

- **Apollo Pharmacy** **–**

_<https://www.apollopharmacy.in/?utm_source=google&utm_medium=srnb&campaignid=13448533801&adgroupid=127019844167&keyword=medicine%20websites&device=c&adtype=&product_id=&utm_campaign=Apollo_Pharmacy_Non-Brand_RestCities_New&utm_content=Medicine%20Online%20EM&gclid=Cj0KCQiAgribBhDkARIsAASA5bsPNBAzdpvkEIwhF-btLuJKjFqrChXSZSJjKLVQO-haBuw6GDdTN54aAqTSEALw_wcB>_

- **Pharmeasy –**

_<https://pharmeasy.in/>_

- **Truemeds –**

_<https://www.truemeds.in/>_

- **Baby Care Advice -**

_<https://www.babycareadvice.com/blogs/baby-care/swaddling-baby>_

2. # Project Requirements

2) 1) # Functional Requirements

- On the login screen, after the user types in their username and password and click submit, the user’s credentials are validated and if correct they are logged in, otherwise an error message is displayed.

* In the sign-up screen when a new user types in all of their information and clicks submit, the data is then validated. If there is an existing user then the user is asked to enter a new username. If there is no conflict then the user is registered.

- When the user selects a category and clicks on find button, the interface should redirect to a new page that displays the results.

* If the user selects any filter on search results page, only the search results that match the filter constraints, should be displayed.

- If the user clicks on details button on a result, the interface shows the detailed profile for that account on a new page.

* Booking details should be mailed to both the client and the Doctor

- The unique id created should match exactly with mobile number.

2. 2. # Non-Functional Requirements

- It must not contain duplicate accounts of the same doctor/laboratory.

* The contact details provided by a user should be valid.

- The contact details of each doctor should be easily accessible.

* There should be security of personal information provided by a doctor.

- The available information should be reliable.

* The system should be easy to use by any computer-literate person.

- The payment Gateway should be available 24x7

* The web portal should be accessible on any device (device friendly).

2. # Analysis Phase

2) 1) # Use-case

2. 1. # **Use-case I:**

1) (SR)The Portal asks for symptoms.

2. (AA) The user enters the symptoms.

3) (SR) The Portal searches the database for related symptoms and gives the recommendation of medicine accordingly.

4. (SR)The portal asks if doctor consultation is required?

5) (AA)user enters “yes”

6. (SR)The portal redirects to doctors and specialists’ page.

7) (AA)User selects the doctor for consultation and the time slot accordingly.

8. (SR)Portal Redirects to the payment gateway where the required fees for appointment can be submitted and then shows a confirmation message.

9) (SR)The portal also sends a confirmation email to the doctor and client and updates the database.

3. 1. 2. # **Use-case II:**

**As A user (Member)**

I WANT TO have login facility

SO THAT I can access the website and its contents

**+SCOPE+**

Member registration

Member Validation

Member should be able to change the password

It should work in all browsers

It should be device friendly

**PRE CONDITION**

User should have a credit/debit card

User should have booked and consulted the doctor earlier

**+Acceptance Criteria+**

**SCENARIO**: User can successfully login

Given I am on login page

And fill the login details

Then database is checked

And logged in if found entry

And Displayed Error if Entry not found

**SCENARIO**: Registration

Given I am on login page

And I click on “new user?”

Then I get redirected to registration page

And I fill in all the details

Then my details get verified and entry is made to Database

Scenario: Buy Membership

Given I am on home page /dashboard

And I click on buy membership button

Then I am shown all the different prices and plans

And I select the suitable plan

Then I am redirected to payment portal

And displayed message Welcome Aboard in case of successful payment

Then I can also check my membership status from profile.

3. 1. 2. # **Use-case III:**

**As a user (Member)**

I WANT TO have a doctor contact facility

SO THAT I can personally contact the doctor in case of emergency

**+SCOPE+**

Build a doctor contact database

Member Validation

Only consulted doctor contact should be shared

It should work in all browsers

It should be device friendly

**PRE-CONDITION**

User should be a member of DAWAI

User should have booked and consulted the doctor earlier.

2. 2. # Use-case Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_993f9d0f.jpg)

2. 1. # Use-case Template

|                         |                                                                                                                                                                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME                    | DAWAI WEB APP (Login and booking)                                                                                                                                                                                                                              |
| ID                      | 10211-DAW-09                                                                                                                                                                                                                                                   |
| DESCRIPTION             | CONNECTS DOCTORS AND PATIENTS ALONG WITH SUGGESTING THEM MEDS AND LAB TESTS                                                                                                                                                                                    |
| ACTORS                  | MEMBERS, DOCTOR, ADMIN                                                                                                                                                                                                                                         |
| ORGANISATIONAL BENEFITS | ANNUAL MEMBERSHIP CHARGES                                                                                                                                                                                                                                      |
| PRE-CONDITIONS          | USER SHOULD HAVE A GOOD INTERNET CONNECTION FREE FROM VPNS AND PROXY’SUSER SHOULD BE A REGISTERED MEMBER OF DAWAI LTD.USER SHOULD HAVE READ THE TERMS AND CONDITIONS PROPERLY                                                                                  |
| POST CONDITIONS         | THE USERNAME AND PASSWORD SHOULD NOT BE SHAREDUNIQUE ID SHOULD NOT BE SHARED PUBLICALLYPATIENT DATA SHOULD NOT BE PROVIDED TO ANY THIRD-PARTY APPS                                                                                                             |
| MAIN COURSE             | 1.LOGIN AND MEMBERSHIP FACILITY2.CONNECT DOCTORS AND PATIENTS3.SUGGEST LAB TESTS, SPECIALIST DOCTORS, MEDICINES4.HELP IN BOOKING APPOINTMENTS WITH DOCTORS5.PROVIDE YOGA AND FITNESS FACILITY6.HELP CENTRE7.CONTACT DOCTORS DIERECTLY                          |
| TASK SEQUENCE           | 1) USER ENTERS USERNAME AND PASSWORD

2) SYSTEM VALIDATES USERNAME AND PASSWORD, ALLOWS ENTRY IF MATCH, SHOWS ERROR IF NOT MATCHED

3) SYSTEM REDIRECTS TO THE HOME PAGE

4) USER CAN CHOOSE DOCTOR FOR APPOINTMENTS AND CAN ALSO BOOK LAB TESTS AND MEDICINES |
| FREQUENCY               | ONCE                                                                                                                                                                                                                                                           |
| CONSTRAINTS             | REQUIRES DOCTOR ACTIVE PARTICIPATION, MEDICINES SUGGESTED CAN’T BE ORDERED WITHOUT CONFIRMATION BY DOCTOR                                                                                                                                                      |
| SPECIAL REQUIREMENTS    | MEMBERSHIP PLANS PAYMENT GATEWAY                                                                                                                                                                                                                               |

2. 3. # Activity Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_2e01fd65.jpg)

2. 4. # Data Flow Diagrams

2) 1) # DFD Level 0

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_c9549de5.png)

2. 1. 2. # DFD Level 1

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_83a0650a.png)

2. 5. # Data Dictionary

|                    |                |               |                       |                               |               |
| ------------------ | -------------- | ------------- | --------------------- | ----------------------------- | ------------- |
| **Field Name**     | **Field size** | **Data Type** | **Data Format**       | **Description**               | **Required?** |
| First Name         | 30             | char          | -                     | First name of the User        | Yes           |
| Last Name          | 30             | Char          | -                     | Last name of the user         | yes           |
| Age                | 3              | int           | -                     | Age of user                   | yes           |
| Earlier disease    | 30             | char          | Disease1, disease2... | Disease diagnosed earlier     | No            |
| Mobile number      | 10             | int           | -                     | Phone number                  | yes           |
| Address            | 90             | char          | -                     | Address of user               | Yes           |
| Membership status  | 1              | Boolean       | -                     | Displays Member or not        | No            |
| Personal Id no.    | 10             | int           | mobile                | Unique number of Member       | Yes           |
| Gender             | 5              | char          | First5letters         | Gender of User                | Yes           |
| Aadhar card number | 16             | Str           | Abcd-1234-efgh-5678   | Aadhaar no. of user           | No            |
| Doctor Status      | 1              | Boolean       | -                     | Displays user a doctor or not | Yes           |
| Doctor contact     | 60             | str           | Mobile-email-address  | Contact of doctor             | No            |
| Disease            | 10             | str           | -                     | Disease                       | No            |
| Symptom            | 10             | Char          | -                     | Symptom of user               | No            |

2. # Design Phase

2) 1) # Class Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_d57dd826.png)

2. 2. # Sequence Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_d257f85a.jpg)

2. 3. # Collaboration Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_515d70c.jpg)

2. # Implementation

   1. # Component Diagram

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_30bd6ccf.jpg)

2. 2. # Screenshots

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_710c4780.jpg)

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_b91fe95a.jpg)

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_7df2a378.jpg)

![](file:///run/user/1000/snap.libreoffice/lu9583r9f2.tmp/lu9583r9h0_tmp_6746787.png)

6. # **Testing**

   1. # Test Cases

      1. # Test Case I:

**Pre-Conditions:**

- Patient must be logged in and registered.

\


- |      |                                  |                                                                                                                                                   |           |          |
  | ---- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | -------- |
  | Step | Action                           | Expected System Response                                                                                                                          | Pass/Fail | Comments |
  | 1.   | Book appointment                 | System displays a search bar alongwith a list of categories such as ENT, dentist etc.                                                             | pass      |          |
  | 2.   | Selection of a category          | System displays list of doctorsavailable for the category and the recommended doctor which the site has recommended according to patient symptoms | pass      |          |
  | 3.   | Selects of a doctor              | System sends patient details to respective clinic.                                                                                                | pass      |          |
  | 4.   | Clinic approves patient request. | Patient receives confirmation from system along with necessary details.Such as contact information, address etc. Patient redirected to home page. | pass      |          |

**Post-Conditions:**

- Patient redirected to home page.

\


6. 1. 2. # |          |                                              |                                                                                                          |                  |             |
         | -------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- | ----------- |
         | **Step** | **Action**                                   | ******Expected****** ******System****** Response********                                                 | **Pass/Fail**    | **Comment** |
         | **1**    | ****Navigate ****on ****login **Button****** | ****Able ****to ****see ****login **page******                                                           | **pass**         |             |
         | **2**    | ****Enter **username******                   | ******The** **username** **entered in**********username **field******                                    | **pass**         |             |
         | **3**    | ****Enter **password******                   | ******The** **password** **entered in**********password **field******                                    | ******pass****** |             |
         | **4**    | ****Click ****login **button******           | ****The ****user ****is ****logged ****into **system**********and ****form ****will be **displayed****** | **pass**         |             |
         | **5**    | ****Enter ****invalid **password******       | ****The ****message ****“invalid **username**********or ****invalid ****password” ****is **shown******   |                  |             |Test Case II:

**Pre-conditions:**

The user has a valid user account and password The system displays main page

\


**Post condition:**

User is validated with Database and successfully log in to account. The details of user will be displayed if it is available.

\


6. 1. 3. # Test Case III(a):

**Pre-conditions:**

The user has a unique UID and valid phone number or email ID

The system displays main page

\


|          |                           |                                                                                   |               |             |
| -------- | ------------------------- | --------------------------------------------------------------------------------- | ------------- | ----------- |
| **Step** | **Action**                | **Expected System Response**                                                      | **Pass/Fail** | **Comment** |
| 1        | Navigate on Signup Button | Able to see login page                                                            | pass          |             |
| 2        | Enter username            | The username entered in username field                                            | pass          |             |
| 3        | Enter password            | The password entered inpassword field                                             | pass          |             |
| 4        | Enter password again      | The password entered intoconfirm password field                                   | pass          |             |
| 5        | Enter age                 | The age entered inage field                                                       | pass          |             |
| 6        | Enter phone no.           | The mobile no. entered intocontact field                                          | pass          |             |
| 7        | Click signup button       | The message will come to your phone that you have registeredyourself successfully | pass          |             |
|          |                           |                                                                                   |               |             |

**Post condition:**

The record of user is stored in database after successful signup.

\


6. 1. 4. # Test Case III(b):

**Pre-conditions:**

The user has a Gmail ID.

The system displays main page

\


|          |                                      |                                                                                                      |               |             |
| -------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| **Step** | **Action**                           | **Expected System Response**                                                                         | **Pass/Fail** | **Comment** |
| 1        | Navigate on Signup with Gmail Button | Pop-ups to new window where it asks user to give access and permission of its Gmail account to DawAI | pass          |             |
| 2        | Navigate to allow access             | The user after reading the terms and condition clicks on the allow access button                     | pass          |             |
| 3        | Click signup button                  | The message will come to your Gmail that you have registered yourself successfully                   | pass          |             |
|          |                                      |                                                                                                      |               |             |

**Post condition:**

The record of user is stored in database after successful signup.





# SE-DawAI

This is a flask based website.
## Credentials

- username - shubh<br>
  password - passkey

# Working Process

To make this app completely working kindly download the zip of the repository and run app.py. A link will get generated which runs this website on your local system.

# Documentation

Kindly go through the DawAI SRS Doc in the given repository.

# Symptoms to make predictions

# medical-project

Please enter these symptoms in the medicine advisor column to predict the medicine for the disease you are suffering from :<br>
Itching <br>
Skin Rash <br>
Nodal Skin Eruptions <br>
Continuous Sneezing <br>
Shivering <br>
Chills <br>
Joint Pain <br>
Stomach Pain <br>
Acidity <br>
Ulcers On Tongue <br>
Muscle Wasting <br>
Vomiting <br>
Burning Micturition <br>
Spotting urination <br>
Fatigue <br>
Weight Gain <br>
Anxiety <br>
Cold Hands And Feets <br>
Mood Swings <br>
Weight Loss <br>
Restlessness <br>
Lethargy <br>
Patches In Throat <br>
Irregular Sugar Level <br>
Cough <br>
High Fever <br>
Sunken Eyes <br>
Breathlessness <br>
Sweating <br>
Dehydration <br>
Indigestion <br>
Headache <br>
Yellowish Skin <br>
Dark Urine <br>
Nausea <br>
Loss Of Appetite <br>
Pain Behind The Eyes <br>
Back Pain <br>
Constipation <br>
Abdominal Pain <br>
Diarrhoea <br>
Mild Fever <br>
Yellow Urine <br>
Yellowing Of Eyes <br>
Acute Liver Failure <br>
Fluid Overload <br>
Swelling Of Stomach <br>
Swelled Lymph Nodes <br>
Malaise <br>
Blurred And Distorted Vision <br>
Phlegm <br>
Throat Irritation <br>
Redness Of Eyes <br>
Sinus Pressure <br>
Runny Nose <br>
Congestion <br>
Chest Pain <br>
Weakness In Limbs <br>
Fast Heart Rate <br>
Pain During Bowel Movements <br>
Pain In Anal Region <br>
Bloody Stool <br>
Irritation In Anus <br>
Neck Pain <br>
Dizziness <br>
Cramps <br>
Bruising <br>
Obesity <br>
Swollen Legs <br>
Swollen Blood Vessels <br>
Puffy Face And Eyes <br>
Enlarged Thyroid <br>
Brittle Nails <br>
Swollen Extremeties <br>
Excessive Hunger <br>
Extra Marital Contacts <br>
Drying And Tingling Lips <br>
Slurred Speech <br>
Knee Pain <br>
Hip Joint Pain <br>
Muscle Weakness <br>
Stiff Neck <br>
Swelling Joints <br>
Movement Stiffness <br>
Spinning Movements <br>
Loss Of Balance <br>
Unsteadiness <br>
Weakness Of One Body Side <br>
Loss Of Smell <br>
Bladder Discomfort <br>
Foul Smell Of urine <br>
Continuous Feel Of Urine <br>
Passage Of Gases <br>
Internal Itching <br>
Toxic Look (typhos) <br>
Depression <br>
Irritability <br>
Muscle Pain <br>
Altered Sensorium <br>
Red Spots Over Body <br>
Belly Pain <br>
Abnormal Menstruation <br>
Dischromic Patches <br>
Watering From Eyes <br>
Increased Appetite <br>
Polyuria <br>
Family History <br>
Mucoid Sputum <br>
Rusty Sputum <br>
Lack Of Concentration <br>
Visual Disturbances <br>
Receiving Blood Transfusion <br>
Receiving Unsterile Injections <br>
Coma <br>
Stomach Bleeding <br>
Distention Of Abdomen <br>
History Of Alcohol Consumption <br>
Fluid Overload. <br>
Blood In Sputum <br>
Prominent Veins On Calf <br>
Palpitations <br>
Painful Walking <br>
Pus Filled Pimples <br>
Blackheads <br>
Scurring <br>
Skin Peeling <br>
Silver Like Dusting <br>
Small Dents In Nails <br>
Inflammatory Nails <br>
Blister <br>
Red Sore Around Nose <br>
YellowÂ CrustÂ Ooze <br>
