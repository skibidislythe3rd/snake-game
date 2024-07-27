from snake import Snake
import turtle
import time
from food import Food
from score import Score
import os
log_files = os.listdir('./Logs')
PLACEHOLDER = "[name]"

with open("./DraftingLetters-main/DraftingLetters-main/Contacts/names.txt", "r") as file:
    names = file.readlines()
    
    print(names)
with open("./DraftingLetters-main/DraftingLetters-main/Email/draft.txt", "r") as draft:
    draft_letter = draft.read()
    for name in names:
        name = name.strip() 
        letter = draft_letter.replace(PLACEHOLDER, name)
        with open(f"./Send/Letter_for_{name}.txt", "w") as new_file:
            new_file.write(letter)



ts = turtle.getscreen()
ts.screensize(600,600)
ts.bgcolor('black')
ts.title("Classic Snake Game")
ts.tracer(0)

snake = Snake()
food = Food()
score = Score()
score.update_score()

ts.listen()
ts.onkey(snake.up, "Up")
ts.onkey(snake.down, "Down")
ts.onkey(snake.left, "Left")
ts.onkey(snake.right, "Right")
        

while True:
    snake.move()
    ts.update()
    time.sleep(0.1)

   
    #Check if game over 
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()

    #Check if touches tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()     


    def quit():
        with open("highscore.txt")as file:
            prev_high_score = int(file.read())

        if (score.high_score > prev_high_score):
            with open("highscore.txt", "w") as file:
                file.write(str(score.high_score))
            

        turtle.bye()
            

              