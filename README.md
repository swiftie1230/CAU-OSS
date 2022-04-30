# WELCOME TO CAU_OSS repository for TEAM 3 !

## I. Simple Version(MVP) of Snake Game 🐍 : "SANKE GAME"

### 👀 Details about our implementation

- **A programming language used to implement the game** : Python

- **A platform to run the game** : Pygame

- **Tools used for the collaborative development** : Notion & Discord & KaKaoTalk    
     
    <img width="116" alt="image" src="https://user-images.githubusercontent.com/63195670/166117642-1abb283b-d4e7-4656-b12b-f19efd71e190.png">    

    <img width="199" alt="image" src="https://user-images.githubusercontent.com/63195670/166117644-90ad989b-c190-4d5d-be4e-f80d93016f23.png">      
  
    <img width="45" alt="image" src="https://user-images.githubusercontent.com/63195670/166117648-c52c5299-2da4-4c31-a308-5be7d4f7d57e.png">       

- **Introduction for our game**

    - i. If you successfully Load our game, you will see this Screen, “Main Menu”     

        <img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/166117713-d735829a-2488-465c-b75a-c6c6addff9b9.png">   <img width="168" alt="image" src="https://user-images.githubusercontent.com/63195670/166117716-e7d1e005-f35a-4d13-8bfa-5083d63f2aab.png">    

        - By clicking LOAD, you can RELOAD the SAVED game

            - If there is **no saved game, button will not be clicked**, like right image. (nothing will happen)

        - By clicking START, you can START the game   

        <img width="174" alt="image" src="https://user-images.githubusercontent.com/63195670/166117798-d1bc9908-5034-4c73-aecc-c5a4deba1d1b.png">   <img width="169" alt="image" src="https://user-images.githubusercontent.com/63195670/166117800-afeb3ba1-eba3-4bc8-86c0-b20b0097cbdf.png">    

        - By clicking RANKING, the top-10 ranked player’s name and score are DISPLAYED

            - If there is **no saved rank, It will display ‘There is No Rank’**, like the right image.

	        - If there are saved ranks, It will display them, like left image. (At most 10)

            - If you click QUIT here, you can go back to main menu.

        - By clicking QUIT, you can EXIT the game

    - ii. Play game ! ( Game play screen looks like below )   

        <img width="162" alt="image" src="https://user-images.githubusercontent.com/63195670/166117957-35233331-f2f2-4c92-997a-2e136c61d872.png">   <img width="156" alt="image" src="https://user-images.githubusercontent.com/63195670/166117953-a868c396-83f9-44e6-9ea4-c9a2a02eba79.png">    

        - If you want to **PAUSE** game during play, **PRESS “ESC”**

        - The game continues until the snake “dies”.

            - The snake dies by either

                - Running into the edge of the board,
                - Running into its own body

        - Once the snake dies, you will see this screen.    

            <p align="center"><img width="184" alt="image" src="https://user-images.githubusercontent.com/63195670/166118007-7f54f6a9-c2da-412f-8cc5-63fdf59f6221.png"></p>    

            - You can write your name by just typing it using the keyboard (Clicking the part is not necessary)

                - **USE “BACKSPACE” first to ERASE THE DEFAULT** displayed on right-top of the screen, then write your name, and **press “ENTER” to SAVE in RANKING!** (Don’t Click GO MENU)

            - If you **don’t want to write any name, then just click GO Main menu.** 

                - It will **not store your data in RANKING** and just return to main menu! 

    - iii. If you PAUSE the game, you will see this screen.   

        <p align="center"><img width="206" alt="image" src="https://user-images.githubusercontent.com/63195670/166118147-e5449f5a-2f57-4bc2-8255-f033c1301f4c.png"></p>      

        - By clicking RESUME, you can RESUME the game
        - By clicking RESTART, you can START a NEW game
        - By clicking SAVE, you can SAVE the current game status and return to the main menu
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
