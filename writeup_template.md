# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/pipeline.png "Pipeline"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

1. I converted the image to a grayscale image. I tried converting to hsv and thresholding for yellow and white. The results were almost identical
2. I applied a gaussian blur with a kernel size of five
3. I applied a cannyu edgd detectior to get the edges 
4. I created a trapezoidal region of interest and masked the rest of the image with a black mask.
5. I used the hough lines function to find lines in the image. To find the longest lines 2 line equations were used.
    * y = m*x + b
    * m = y2-y1/x2-x1
    * set y_max and y_min to the height of the image
    *  I calculate slopes for both lines and found the intercepts. 
    * set y_min to the least value of y1,y2 and y_max
    * Negative slopes are for left lines and positive slopes are for lines on the right. 
    * I average all the slopes and intercepts.
    * I find x_max and x_min for left and right slopes using x = (y-b)/m where y is y_max and y_min respectively and b is the average slope.
    * x_min, x_max, y_min and y_max are the passed to the draw_lines funtion to draw the longest lines in the image
![alt text][image1]

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the lanes aren't straight lines 

Another shortcoming could be inclined roads going either uphill or downhill


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to making it able to handle curves and inclines using perspective transformation and poly fitting lane lines.

### References
1. https://github.com/upul/CarND-LaneLines-P1/blob/master/P1.ipynb
2. https://github.com/naokishibuya/car-finding-lane-lines