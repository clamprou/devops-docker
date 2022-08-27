# Django Student Management System
This is a Simple Student Management System where students can register and make their apply for a course at the same time and after that Secretary can aprove or disaprove their applies.

## Features of this Project

### A. Admin Users Can
1. Manage all Entities from the admin site

### C. Students Can
1. Register an account.
2. Apply for a Course

### B. Secretary Can
1. See Applies from all Students.
2. Approve Applies
3. Not Register an account (needs admin to create one)


## How to Install and Run this project Manualy?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

```
$  python3 -m venv venv
```

Activate Virtual Environment

```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/vijaythapa333/django-student-management-system.git
```

Then, Enter the project
```
$  cd django-student-management-system
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```

**6. Add the hosts**

- Got to settings.py file 
- Then, put your email credentials to the variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
```python
EMAIL_HOST_USER = email@email.com
EMAIL_HOST_PASSWORD = password
```

**7. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```


**7. Login Credentials**

Create Super User (HOD)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**8. Add initial data**
Command for PC:
```
$  python manage.py loaddata initial_data.json
```


## How to Install and Run this project automated on a remote server with Jenkins and Ansible?

### Pre-Requisites:
**1. Setup a Jenkins server on cloud**

**2. Setup a Deployment server on cloud**

**3.Make sure ssh connection can be established between two servers**  
  1. Connect to Jenkins server
  2. Run: ```$ sudo su jenkins```
  3. Create an id_rsa ssh Key
  4. Copy the id_rsa.pub
  5. Connect to Deployment server and paste it on the .ssh/authorized_keys file
  6. Edit .ssh/config file and add this HostName and User changed to yours
```
Host db01
    HostName 0.0.0.0
    User username
    IdentityFile ~/.ssh/id_rsa
Host app01
    HostName 0.0.0.0
    User username
    IdentityFile ~/.ssh/id_rsa
```
**4.Create a pipeline on jenkins site to clone ansible project**  
  1. Repository url: ```https://github.com/clamprou/ansible-example.git```
  2. Branch name ```*/master```

**5.Create a pipeline on jenkins site to clone the django project**
  1. Repository url: ```git@github.com:clamprou/devops1.git```
  2. Branch name ```*/main```
  3. Script path ```Jenkinsfile```
