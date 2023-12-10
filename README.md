# comp_1510_term_project
<a href="https://github.com/TommyJu/comp_1510_term_project">Github Repository</a>

<marquee direction="right">BCIT CST - Autumn 2023</marquee>


<h3>Student names</h3>
<ul>
    <li>Tommy Ju</li>
    <li>Matthew Yoon</li>
</ul>

<h3>Student numbers</h3>
<ul>
    <li>A01347715 (Tommy)</li>
    <li>A01373290 (Matthew)</li>
</ul>

<h3>Student GitHub accounts</h3>
<ul>
    <li><a href="https://github.com/TommyJu">TommyJu</a></li>
    <li><a href="https://github.com/matthewy0987">matthewy0987</a></li>
</ul>

| Requirments                           | Where in Code                      |
|---------------------------------------|------------------------------------|
| 1. main func game                     | game.py in /comp_1510_term_project |
| 2. flowchart                          | flowchart.pdf                      |
| 3. b)  10 x 10 grid-based environment | game.py / make_board.py in /map    |
| 3. c)  character attributes           | make_character in /character       |
| 3. d) character movement              | all of /movement                   |
| 3. e) encounter some sort of obstacle | enemy_detection.py in /enemy       |
| 3. f)to overcome                      | /combat                            |
| 3. g) endpoint                        | /map endpoint reached              |
| 4. level up                           | level_up.py in /character          |
| 6. dying                              | in game.py or is alive             |
| 7. a)                                 | game.py in /comp_1510_term_project |

# Game Instructions

## The Objective
You're a ninja who is on a top secret mission.

You must reach the objective on the opposite corner of the game board.
Sneak past the enemies to complete the level swiftly or battle every enemy in an epic rock-paper-scissors duel, 
the choice is yours.

Beware of the boss, he's really strong.

## How Input Works
Once you run the program, there will be a text input box right under "GAME INPUT BELOW:" 
Click on it and then press enter to begin.
You can submit what you've typed by clicking on the enter button, or pressing enter on your keyboard.

## Movement
There are three ways to move in a direction:
- Type a number [1-4]
- Type the name of the direction Ex: "north"
- Type W, A, S, D (UP LEFT DOWN RIGHT)

## Enemies
Enemies will move in a random valid direction.
Each enemy can see the block in front of them, unless their vision is outside of the board or on the objective.
You will engage in combat if you are on the enemy's vision block, or on top of the enemy.
Being spotted by multiple enemies at once will lead to back-to-back combat.

## Combat
It's rock-paper-scissors but with a twist.
Player action and enemy action are dice rolls on top of the selection of rock, paper, or scissors.
It does two things:
1. Determines who wins or loses in a draw.
2. Decides how much damage you take from the enemy in a draw or a loss.

## Leveling
Upgrading your character's attack will increase your odds of generating a higher player action roll.
Upgrading defense will increase your max HP.
You regenerate health on level up.


>Thank you Chris for always going the extra mile. Comp 1510 is an amazing course, and I'm glad that I got to be a part of it.
-Tommy



