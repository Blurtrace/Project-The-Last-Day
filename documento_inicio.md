Development Process – Game Initialization Module

During the development of this module, the goal was to create the initial configuration of the game. The script asks the player for a username, validates that the username is not empty, and allows the player to select a difficulty level that determines the starting resources.

At the beginning, the first challenge was implementing a loop that ensured the user entered a valid username. Since I am still new to programming and Python, creating loops was difficult for me. After some attempts, I used a while loop to keep asking the player for a username until they entered a valid value.

Another challenge occurred when creating the function that allows the player to select the difficulty level. Initially, I had problems because the variables such as health, food, water, and energy were not being stored correctly in the game engine after the function executed. This happened because the values were defined inside the function but were not being returned.

To solve this problem, I implemented a return statement that sends the variables outside the function so they can be used by the rest of the program. This allowed the main script to correctly receive and store the game resources.

While working on the code, I also made some improvements to the game configuration. For example, I added a new variable called  bad_porcentage, which represents..................... I also adjusted the population values for each difficulty level to make the gameplay more balanced.

Even though creating loops and managing variables inside functions was challenging at first, solving these issues helped me better understand how functions, loops, and variable scope work in Python. This process improved my confidence when building logical structures in code.