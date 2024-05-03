
# Cake Personality Test
## CS110 Final Project  Spring Semester, 2024

## Team Members

Samiha Kazi

***

## Project Description

The Cake Personality Test was born out of my love for understanding what makes people, as well as my undeniable passion for cakes. I've always been fascinated by personality types and how they shape who we are, much like the layers of a cake come together to create something unique and delicious. This project is a whimsical yet insightful journey into self-discovery, blending the structured approach of personality assessment with the pure indulgence of choosing a favorite cake. As someone who enjoys both deep conversations about personality traits and the simple pleasure of savoring a sweet treat, I wanted to create a fun and interactive way for others to explore their own personalities while satisfying their cravings for both insight and dessert. Through the Cake Personality Test, users can embark on a delightful adventure of self-discovery, all while enjoying the delicious metaphor of personality as a piece of cake.

***    

## GUI Design

### Initial Design

![initial gui](assets/intialscreen.png)

### Final Design

![final screen] (assets/finalscreen.png)




## Program Design

### Features

Features
1) Personality Test: Allows users to answer a series of questions to determine their cake personality type.
2) Interactive Interface: Provides an interactive graphical user interface for users to navigate through the personality test.
3) Result Display: Displays the user's cake personality type along with a description of their result after completing the test.
4) Image Integration: Includes images of cakes corresponding to the user's personality type to enhance the visual experience.
5) External Data Handling: Utilizes external data in the form of cake descriptions to provide personalized results.

### Classes
1) PersonalityTestView: Manages the graphical user interface, including displaying questions,  options, and results, and handling user interactions.
2) PersonalityTest: Represents the personality test model, including questions, options, and logic for determining the user's cake personality type based on their answers.
3) CakeDescription: Stores and provides descriptions of different cake personality types to be displayed to the user upon completing the test.
4) ImageLoader: Handles the loading and display of images, such as cake images, within the application to enhance the visual presentation.

## ATP

| Step                 | Procedure            | Expected Results                    |
|----------------------|:---------------------|------------------------------------:|
|  1                   | Run Counter Program  | GUI window appears with count = 0   |
|  2                   | Click count button   | Display changes to count = 1        |
|  3                   | Click reset button   | Display changes back to count = 0   |
|  4                   | Enter text in input  | Text appears in display area        |
|  5                   | Click save button    | Text is saved to file               |
|  6                   | Close program        | Program window closes               |
