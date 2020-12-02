# Surfs_Up Challenge

## Overview
This is analysis allowed us to explore the use of SqlLite and SqlAlchemy, and the use of Python for visualization with Flask. We explored 
technologies by analyzing weather data for a new business venture for a icecream and surf shop. As the final challange, the investor has specific
questions about the months of June and December. Specifically, he wanted to understand the temperatures in those months to see if the shop can remain open
all year long.  To perform this analysis, I used the analytical tools of SQlLite to analyze the temperature data for June and December.

# Results
## Overview of the Results:
The months of June and December were analyzed the data. Both months had sufficient data to come to valid conclusions-- June (n=1700) and December(n=1517). Rrom the analysis
of the data it looks that there is not significant differences in the median temperature.  June had an average temp of 74.9 (std 3.25) while December had an average temp of
71.05 (std 3.75). 

### June_temps                         
count 1700.000000                      
mean  74.944118                        
std	  3.257417                         
min	  64.000000                        
25%	  73.000000                        
50%	  75.000000                        
75%	  77.000000                        
max	  85.000000  


### December_temps
count	1517.000000

mean  71.041529

std	3.745920

min	56.000000

25%	69.000000

50%	71.000000

75%	74.000000

max	83.000000

# Summary
While December is a bit cooler I don't think its enough of a difference to close the shop.  Even at the lower 25% level the temperature is still around 69 
which is not significantly lower than the mean. Even at the lower 25% the temp in December is around 69--which isn't very different from the median temperature. Based on
this, I don't believe the temperature drops enough to close the shop.  
## Results
***The major differences between the two months are:***

      -There was a 3 degree in the mean temperature
      -The number of data points was approximately 200 fewer for December
      -The standard deviation is higher for December which demonstrates a bit more variation in the data
      
In Summary, one analysis I would have also run was the temperatures by date--particularly for the month of December. By doing so, I would be able to determine if the temp
drop significantly at a certain time of the month (such as later) which could be lowering the overall average. If so the shop may need to close later in the month for a few weeks instead of the entire month
      

