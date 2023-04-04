# classic-snake-game

-  Snake is a sub-genre of action video games where the player maneuvers the end of a growing line, often themed as a snake. The player must keep the snake from colliding with both other obstacles and itself, which gets harder as the snake lengthens. It originated in the 1976 two-player arcade video game Blockade from Gremlin Industries where the goal is to survive longer than the other player.

- The original game is actually Two-Players game but what i have built is a single player to jsut demonstetate the Pyhton Essentials what i have leant till now.
- The "head" of the snake continually moves forward, unable to stop, growing ever longer. It must be steered left, right, up, and down to avoid hitting walls and the body of either snake.snake gets longer with each piece of food which '#' in our case.

[Play the deployed version here!](https://classic-snake-game.herokuapp.com/)

## Flowchart

- The Flowchart explains the functionality of the game to help understand the mechanism of the code. 

- The Flowchart was really helpful in the initial process of building the app.

- Firstly it was hard to figure out where to start but with the Flowchart it was almost drawing the game on a paper. 

![Flowchart](/documents/flowchart/snake%20flowchart.jpg)

## User Stories

  -   #### First Time Visitor Goals

      1. As a first time use i want to understand the manuevers of the snake. 
      2. As a first time visitor I want to understand how to play the Classic Snake Game. 
      3. As a first time user I want to understand how to start the game, check the instructions.
      4. As a first time visitor i want to feed as much as the food it can.

  -   #### Returning Visitor Goals

      1. As a returning visitor I want to Finish the game quicker then before with highest scores. 
      2. As a returning visitor I want to try make the snake as long as possible. 

  -   #### Frequent User Goals
      1. As a frequent user I want to be beat my last score. 
      2. As a frequent user I want not to hit the walls or the snake body. 

## Features

### Existing Features

- __Start__

    - When the program starts snake is already moving in Right direction.
    - Food is presented as '#,.

- __Controls__
     - User has a full control of game with Right, left, Up , and Down key.
     - Food is presented and regenrated as '#'.

- __End Game__

    - Anytime snake hits the wall Game ends.
    - Anytime snake hits his own body Game ends.


- __Features left to implement__

    - I would add the Code , so whenever snake take the 180 degrees turn, Game doesnt End .
    - I would use Pygame module and make snake colorful fonts and food too. Due to the cutial time management i could only come up with this simplicity. 
    - I would add play again button to be more user friendly. 
    - I would love to make a proper action game as a clone of classic snake game. 

## Testing 

- Testing was done using Pylint and PEP8 syntax chekcer.


 | Tests  |      Expectations      | Pass/Fail |
|----------|:-------------:|------:|
|__Testing the syntax by PEP8 online linter__ | There shoudnt be any syntax errors| **PASS** |
| __Testing the keys functioning in order__ | All the keys , Right, Left, Up, and Down should work perfectly as user input|   **PASS** |
| __Testing the snake eats food and increase in length__ | Whenever food was eaten by the snake Game ended. due to the **curses.curs_set()** and then i had ot delete that code of line|   **PASS** |
|  __Testing if the Game is over at specific rules__| By hitting the wall game should end and by hitting the snake its own body game should end   |   **PASS** |
| __Testing the code works again and again__ | When game ends and user clicks the RUN PROGRAM game starts as normal  |    **PASS** |
__Testing the Score increases__ | Whenever snake eats food the Score goes up by 1  |    **PASS** |
|
​
### Heroku Deployment
​
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
​
Deployment steps are as follows, after account setup:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Enter a name for your app. The app name must be unique, so you need to adjust the name until you find a name that hasn't been used.
- From the dropdown, choose the region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add buildpack*.
- The order of the buildpacks is important. Select `Python` first, then *Save changes*. Click *Add buildpack* again, and select `Node.js`, then *Save changes*. If they are not in this order, you can drag them to rearrange them

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- At the top of the screen on Heroku, select *Deploy*.
- Next to *Deployment method* select *GitHub*, then scroll down and click *Connect to GitHub* to confirm you want to connect.
- In the *repo-name* field, search for the name of the GitHub repository to deploy, and click *Search*.
- Click *Connect* to link the GitHub repository with Heroku. 
- Scroll down to the *Manual deploy* section, and click *Deploy Branch*.
- If you like, click *Enable Automatic Deploys* in the *Automatic deploys* section to have Heroku rebuild your app every time you push a new change to GitHub.

The frontend terminal should now be connected and deployed to Heroku.

## Credits


### Content
- I used Code Institute's Love Sandwiches Lesson ([repo here](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)) for the idea and the process of Heroku Deployment.
- For slower printing to the terminal I used Stackoverflow. The page is [here](https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay)

- To figure out deployment issues i used [Stack overflow](https://stackoverflow.com/)

- For the coding and the guidance i researhced few Youtube Channels and some web articles


## Acknowledgements

- Big Thanks to Ronan McClelland as a mentor to help me out addressing problems with my first BeautifulSoup app as a project.
