---
layout: default
---

In this tutorial, we are going to deploy our Python Project to Heroku cloud. 

### Deploy to Heroku

<dl>
<dt>STEP-1: Create a Heroku account</dt>
<dd>Login or Signup to Heroku account online. It is totally free. <br> 
Login link here: <a href="https://heroku.com"> Heoku Home Page </a>
</dd>

<dt>STEP-2: Install Heorku toolbelt in your computer</dt>
<dd> This step is installing Heorku CLI toolbelt in computer. <br> 
- MacOS: `$ brew install heroku/brew/heroku` <br>
- Windows: [Download installer](https://cli-assets.heroku.com/heroku-x64.exe) <br>
- Ubuntu: $ sudo snap install heroku — classic <br>
More info here: <a href="https://devcenter.heroku.com/articles/getting-started-with-python#set-up"> Heroku Installer Page </a>
</dd>

<dt>STEP-3: Download the zip from canvas</dt>
<dd> Download the project zip file from canvas.</dd>

<dt>STEP-4: Deploy to Heroku</dt>
<dd> 1) open the command-line/terminal. <br>
2) Go to the root directory of project in your terminal with `cd` command.<br>
3) Run setup file with root permission. `$ python setup.py develop` <br>
4) Install required dependencies for the project with root permission. `$ pip3 install -r requirements.txt`. <br> <b> Note </b>, If it gives an error pip not found that means, you do not have pip installed. 
Install pip from here: <a href="https://pip.pypa.io/en/stable/installing/"> Install Pip </a> <br>
5) Create Heroku app in your terminal, It will ask about your login credentials. `$ heroku create`.
6) After successfully creation of an app locally, Go to Heroku Dashboard online and follow the steps for deploy. Link here: <a href="https://dashboard.heroku.com/apps"> Heroku Dashboard </a>
</dd> 
<center>
<img src="http://salemount.com/project-4/heroku-deploy.jpeg" alt="heroku Dashboard" style="width:500px;height:300px;">
<br>
Fig - Heroku dashboard for newly created app after Login.
</center>


</dl>


[back](./)
