# Challenge 3 Solution #

The code for the challenge can be find [here!](https://github.com/agyimr/bigdata_challenge_3)

In the third challenge, our task was to create a unique hash algorithm for videos, and test the efficiency of the algorithm with the clustering of 9700 videos. These were made from an initial 970 videos, all of which was distorted with different methods in order to get 10 of each. The goal was to get the same videos into the same clusters.

Our approach to the problem was to first create an image of each video and then hash these images. We created this image with averaging all the frames in the video. We basically summed up each pixels red, green and blue values from each frame and in the end divided this matrix with the number of frames. This resulted in the images below (for two videos of the same content, but distorted):

![Averaged images](https://github.com/agyimr/bigdata_challenge_3/blob/master/averaged_images.jpg "Averaged images") 

As we can see the images are similar but it would be great if we could somehow normalize the brightness levels. This is exactly what we did as a next step. For this we first converted each image from RGB to HSV representation, and here set both the Saturation and Brightness levels to 128, which is a middle value. After this step, we converted the image back to RGB. The results can be seen below:

![Normalized images](https://github.com/agyimr/bigdata_challenge_3/blob/master/normalized_images.jpg "Normalized images")

The images are really similar now. The only problematic part is the border. We can easily get rid of it by only examining the inner 80% of the picture. Since each image is represented as a numpy array this can be done really easily using built in functionalities of python. 

Now we need to somehow hash these images. We wanted to use k-means to cluster the hashes. This method aligns really well with multi-dimensional values. Therefore what we did was we downscaled the images to a 10*10 pixel size. This way we ended up with 300 values for each image (since 10 * 10 = 100, but we still have the red, green and blue values for each pixels, which results in 300 values overall). This array of values is what we called hash. Of course picture worth more than a 1000 words...

![Hashed images](https://github.com/agyimr/bigdata_challenge_3/blob/master/hashed_images.jpg "Hashed images")

This information is stored in an array with the lengths of 300. The values with the same meaning are always at the same pace. This results in the following structure:
* The first element is the top left pixel's red value
* The second element is the top left pixel's green value
* The third element is the top left pixel's blue value
* the fourth element is is the top row's second element's red value
* ...

This way all the 300 dimensions have a meaning, as well as the distance between them. It is important to carry information with the difference for the k-means to work. In other words... The difference of the values in the same place represents the difference of the images (hence the videos). The closer they are, the more similar the videos are and vica versa.

With all that in mind applying k-means clustering (with k = 970 brackets) we get a clustering with a rand index of about **0.697 ~ 0.7**, which can be considered as a pretty good result especially if we take into account that the computational time was only **1 hour** in our 8 core machine. (The hashing part of the program is written in a way to utilise parallel computation to speed up the process)
