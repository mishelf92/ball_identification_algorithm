# ball identification algorithm in a simulated robotic football game

Explanation of the files:

1.clickMouse - The code lets you know the pixels of a particular point in image

2.Simulation.ttt - the Simulation in CoppeliaSim. From here you can create data of images the steps that need to be done for this are:
First in coppeliasim enter to cam script and there make the notes into code like in the image
![צילום מסך מ־2021-07-02 15-25-35](https://user-images.githubusercontent.com/73639866/124274556-15848000-db4a-11eb-923e-ceb7f90f1e67.png)

this will create images, the images are in your coppeliasim folder. For example  in /home/mishel/CoppeliaSim

3.ball_identification_algorithm - This code runs the file "Simulation.ttt" and returns the position of the ball at each simulation step i.e. every 0.05 seconds this the final code of the algorithm for the project.

4.not_In_real_Time - Code that runs on any images that in the folder in your pycharm and saves algorithm results in an excel file. (Works with an image in horizontal mode compared to the final algorithm  code).
 
