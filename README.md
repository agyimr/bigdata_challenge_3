# Challenge 3 Solution #

In the third challenge, our task was to create a unique hash algorithm for videos, and test the efficiency of the algorithm with the clustering of 9700 videos. These were made from an initial 970 videos, all of which was distorted with different methods in order to get 10 of each. The goal was to get the same videos into the same clusters.

Our approach to the problem was to first create an image of each video and then hash these images. We created this image with averaging all the frames in the video. We basically summed up each pixels red, green and blue values from each frame and in the end divided this matrix with the number of frames. This results in the images below:

![Averaged image 1](https://github.com/agyimr/bigdata_challenge_3/blob/master/test1.jpg "Averaged image 1") ![Averaged image 2](https://github.com/agyimr/bigdata_challenge_3/blob/master/test2.jpg "Averaged image 2")

As we can see the images are similar but it would be great if we could somehow normalize the brightness levels. This is exactly what we did as a next step. For this we first converted each image from RGB to HSV representation, and here set both the Saturation and Brightness to 128. Which is a middle value. After this step, we converted the image back to RGB. The results can be seen below:

![Normalised image 1](https://github.com/agyimr/bigdata_challenge_3/blob/master/test1_normalised.jpg "Normalised image 1") ![Normalised image 2](https://github.com/agyimr/bigdata_challenge_3/blob/master/test2_normalised.jpg "Normalised image 2")

The images are really similar now. The only problematic part is the border. We can easily get rid of it by only examining the inner 80% of the picture. Since each image is represented as a numpy array this can be done really easily using built in functionalities of python. 