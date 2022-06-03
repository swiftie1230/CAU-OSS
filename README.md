# WELCOME TO CAU_OSS repository for TEAM 3 !

## I. Simple Version(MVP) of Snake Game 🐍 : "SNAKE GAME"

### 👀 Details about our implementation

- **A programming language used to implement the game** : Python

- **A platform to run the game** : Pygame

- **Tools used for the collaborative development** : Notion & Discord & KaKaoTalk    
     

- **Introduction for our game**

    - i. If you successfully Load our game, you will see this Screen, “Main Menu”     

        <p align="center"><img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/170847237-dc793616-85dd-4378-a815-d3604d3298c3.png">   <img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/170847250-7e1dc046-ba99-430e-ab17-9b0ae2c37c85.png"></p>    

        - By clicking SINGLE PLAY, you can START a new SINGLE-PLAYER game

        - By clicking DUAL PLAY, you can START a new DUAL-PLAYER game

        - By clicking AUTO PLAY, you can START a new AUTO-PLAY game

        - By clicking LOAD, you can RELOAD the SAVED game

            - If there is **no saved game, button will not be clicked**, like right image. (nothing will happen)

        - By clicking START, you can START the game   

        <p align="center"><img width="174" alt="image" src="https://user-images.githubusercontent.com/63195670/166117798-d1bc9908-5034-4c73-aecc-c5a4deba1d1b.png">   <img width="169" alt="image" src="https://user-images.githubusercontent.com/63195670/166117800-afeb3ba1-eba3-4bc8-86c0-b20b0097cbdf.png"></p>    

        - By clicking RANKING, the top-10 ranked player’s name and score are DISPLAYED

            - If there is **no saved rank, It will display ‘There is No Rank’**, like the right image.

	        - If there are saved ranks, It will display them, like left image. (At most 10)

            - If you click QUIT here, you can go back to main menu.

        - By clicking QUIT, you can EXIT the game


    - ii. SINGLE-PLAYER GAME ! ( Game play screen looks like below )   

        <p align="center"><img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/170847303-9bcbab6c-a267-42a7-b38e-6ca4456bc3ab.png">   <img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/170847307-09bbd923-2541-4dd5-8931-e8dc7a012d3b.png"></p>    

        - If you want to **PAUSE** game during play, **PRESS “ESC”**

        - The game continues until the snake “dies”.

            - The snake dies by either

                - Running into the edge of the board,
                - Running into its own body

        - Once the snake dies, you will see this screen.    

            <p align="center"><img width="184" alt="image" src="https://user-images.githubusercontent.com/63195670/166118007-7f54f6a9-c2da-412f-8cc5-63fdf59f6221.png"></p>    

            - You can write your name by just typing it using the keyboard (Clicking the part is not necessary)

                - **USE “BACKSPACE” first to ERASE THE DEFAULT** displayed on middle of the screen, then write your name, and **press “ENTER” to SAVE in RANKING!** (Don’t Click GO MENU)

            - If you **don’t want to write any name, then just click GO Main menu.** 

                - It will **not store your data in RANKING** and just return to main menu! 

        - If you PAUSE the game, you will see this screen.   

            <p align="center"><img width="206" alt="image" src="https://user-images.githubusercontent.com/63195670/166118147-e5449f5a-2f57-4bc2-8255-f033c1301f4c.png"></p>      

            - By clicking RESUME, you can RESUME the game
            - By clicking RESTART, you can START a NEW game
            - By clicking SAVE, you can SAVE the current game status and return to the main menu
            - By clicking QUIT, you can return to the main menu without saving the current game status


    - iii. DUAL-PLAYER GAME ! ( Game play screen looks like below )   

        <p align="center"><img width="185" alt="image" src="https://user-images.githubusercontent.com/63195670/170847359-65a2a0cd-fddf-41c4-820d-4502d7a0d272.png"></p>    

        - Player 1 : LEFT UPPER snake, play with WSAD keyboard

        - Player 2 : RIGHT BOTTOM snake, play with direction key

        - If you want to PAUSE game during play, PRESS “ESC”

        - The game continues until the either one snake “dies”.

        - The snake dies by either

            - Running into the edge of the board,
            - Running into its own body, or each other.

        - Once a game is finished, you will see this screen.

            <p align="center"><img width="181" alt="image" src="https://user-images.githubusercontent.com/63195670/170848509-3e544302-8cc9-4e45-b397-d6b898d4b260.png"></p>    

            - You can see a simple pop-up message, which contains

                - THE WINNER 

            - If you want to go back to main menu, then just click GO Main menu. 


        - If you PAUSE the game, you will see this screen.   

            <p align="center"><img width="198" alt="image" src="https://user-images.githubusercontent.com/63195670/170848570-5d82d097-c303-4771-b2e7-60935f38abf8.png"></p>      

        - By clicking RESUME, you can RESUME the game
        - By clicking RESTART, you can START a NEW game
        - By clicking QUIT, you can return to the main menu without saving the current game status


    - iv. AUTO-MODE GAME ! ( Game play screen looks like below )    

        <p align="center"><img width="184" alt="image" src="https://user-images.githubusercontent.com/63195670/170848616-ef879d8a-d664-4c49-9b40-10c322e9412f.png"></p>    

        - Basic Algorithm

            - Find food x, y coordinate.
            - First, move snake head to food x and then move snake head to food y.
            - if snake meet wall or snake’s body, it find new direction.
            - Look for directions, if it can, go in that direction.

        - The ONLY way the game can be over is when the snake makes ring-shaped. (there is no way to go because of its too long body)

        - If you PAUSE the game, you will see this screen.   

            <p align="center"><img width="198" alt="image" src="https://user-images.githubusercontent.com/63195670/170848570-5d82d097-c303-4771-b2e7-60935f38abf8.png"></p>      

        - By clicking RESUME, you can RESUME the game
        - By clicking RESTART, you can START a NEW game
        - By clicking QUIT, you can return to the main menu without saving the current game status

* * *

### ☝🏻 Guidelines to install and run our game

- Our game is based on “pygame”! First, **Install pygame** on your computer.

- **Download zip file** from our  Public GitHub repository.

    <img width="317" alt="image" src="https://user-images.githubusercontent.com/63195670/166118275-75446fed-33f2-44aa-a17a-9e8b699a4c0c.png">        

- Go to the directory like below and run ‘simplified_snake_game.py’

    - Using cd, move to ***“CAU_OSS”*** directory in your own computer and **access, open the file using below commands.**

        <img width="468" alt="image" src="https://user-images.githubusercontent.com/63195670/166118352-240e3cfc-9307-47a1-8e2c-065b0f5de702.png">    

        - *If you use python instead of python3, use python as command! It depends on your computer develop environment.

            - Ex)  `\CAU_OSS> python .\snake_game\simplified_snake_game.py`
