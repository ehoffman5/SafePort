# SafePort

 This is the official repository of SafePort, the user-friendly port scanner.
 Code for the beta version of this project can be found at this repo: https://github.com/sharpnachos/comp330sp19p3

## What is SafePort?

SafePort is a sleek, modern, easy-to-use port scanner that provides an accessible way for the ordinary person to test the security of their own devices. As opposed to less user-friendly port scanners like ZenMap, SafePort makes it easy for users to scan their device with a single click. SafePort sends TCP connection requests to the device's ports (via the user's personal IP address) and determines whether or not the device is at risk.  Once a scan is completed, the user can view which of their ports are open and follow simple documentation for how to close those ports.

## Run and Build Instructions
Please follow the setps below to ensure this application runs as needed in a development environment:
 * Ensure Node.js is installed on your computer
      * To check if it is installed, open cmd and type 'node -v' for your Node.js version and 'npm -v' for NPM
      * To install Node.js, follow this link to the official web page: https://nodejs.org/en/
 * Clone this repository into Visual Studio Code or any other IDE of your choice
 * Open Git Bash and make sure you are in your local project directory
 * Run the following line of code in your terminal to ensure there are no permissions errors while running this application:
      * rm -rf node_modules && npm install
 * Type the command "npm start' in the terminal to start Electron
 * An Electron window should open up running the SafePort application

## Features
### Web Application using Bulma
We created our main interface using HTML and Bulma which is CSS Framework. We included a welcome page that give you the option of logging and signing up. The login button leads to the login page and the sign up button leads to the sign-up page.

### Login Verification
We implemented login verification as one of the main features. The login verification on the login page does not allow that user to move past that page if either field (username or password) is left empty. It creates an alert box that prompts the user to make sure no field is left empty. Once the requirements are met, they can move on to the Feed page. At the end of the log-in page ther is als the option for the user to switch over to the sign-in page. Login verification is also implemented on the sing up page which requires users to input a username, password, and password confirmation. The following criterias must be met by the users: 
  * Username field cannot be left blank  
  * Password must contain at least one number  
  * Password must contain at least one uppercase letter  
  * The inputs in the Password and Confirm password field must pass    
  
These requirements must be met in order to move on the Feed page, otherwise and error notification box pops up to nitify the user of what requirement they still need to meet (i.e. if the user is missing a number in the password, an error box with the follwing error will pop-up: "Error: password must contain at least one number (0-9).").  

### Twitter API
The search API was implemented to look for tweets froma  sepcific user. The API is hardcoded to access the most recent tweet from @LoyolaChicago. This is the feature that we ran in to issues with and is fruther discussed in the reflection below.

### Embedded Twitter Timeline
On the feed page, we implemented a feature where the tweets from Loyola Chicago twitter and the timeline is embedded on the page for the user to look at. This feed updates in realtime.

### Class Lecture Aspect
We utilized Scrum methodology as discussed in the lecture videos. We used "sprints" as one of our main methods of meetings and work. It allowed for us as a bigger team to be more effective whether it was in person or over Zoom call. We used Basecamp actively to schedule our meeting and to-dos, upload notes, and create benchmarks to meet in each meeting/worrk session.

### Additional Fun Features
#### World Map
We included a world map feature as fun interactive map that allows you to click on continent and learn a fun fact about it.

#### Words of Wisdom
We included a fun Words of Wisdom page which is a random quotes generator. And, it also allows you to click on a tweet button to share something on Twitter.

## Reflections
This project has been accompanied with many ups and downs and fixes. Through the process we learned many lessons about proper GitHub merging, project configurations, dependencies, team communication. We also learned the importance of contiued communication in order to end with a coherent project having that we decided to start with a new project in the second week of the process. This project went through a lot of changes and required us to adjust ot the circumstances. We originally started with an Android Studio app that changed to a web application, we also had a lot of issues getting the API up and running, but we still have a working API whose data can be accessed about the user that is hardcoded in. We even added two fun features; this project taught us a alot about adjusting to the circumstances. This project has taught us how to work with new technologies such as Node, server-side problems, JavaScript, and more. We also learned the importance of GitHub branching and how to avoid merging conflicts since that was a huge source of issues early on in the project. We also acknowledge the lack of testing since this was the first time using JavaScript for all of us and we spent most of the time ensuring the application was running and functional first. Overall, this project was a huge learning experience and has really better prepared us for the final semester project.
  
    
Software Requirements document can be found here: https://docs.google.com/document/d/1UbNAnlWFwyI88b9gsaV5jTWpR_EDOiLiTKiGmrd8sgo/edit?usp=sharing
