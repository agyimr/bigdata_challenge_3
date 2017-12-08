# Challenge 3 Solution #
---
In the third challenge, our task was to create a unique hash algorithm for videos, and test the efficiency of the algorithm with the clustering of 9700 videos. These were made from an initial 970 videos, all of which was distorted with different methods in order to get 10 of each. The goal was to get the same videos into the same clusters.

Our approach to the problem was to first create an image of each video and then hash these images. We created this image with averaging all the frames in the video. We basically summed up each pixels red, green and blue values from each frame and in the end divided this matrix with the number of frames. This results in the images below:

![Averaged image](https://github.com/agyimr/bigdata_challenge_3/blob/master/test1.jpg "Averaged image")