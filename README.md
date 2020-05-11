# final_project
Each team creates a fork from this for their course project

<h2>Insights Dervied through Internet Usage Worldwide</h2>
<b>Created by : Gaganpreet Kaur Baansal, Welisa Lewis</b>

<b>Data Sources:</b>

1. https://www.kaggle.com/sudalairajkumar/undata-country-profiles#country_profile_variables.csv 
2. https://knoema.com/atlas/topics/Telecommunication/Telecomm-Services/Secure-Internet-servers 
3. https://knoema.com/atlas/topics/Telecommunication/Internet-Users/Share-of-the-Internet-users 
4. https://drive.google.com/file/d/0Bx1Nsg-bc9ovX0h4SnJ1SFc5Q2c/view <br>
   Obtained from HCR lab dataset :http://ocslab.hksecurity.net/Datasets/web-hacking-profiling 

<b>References:</b><br>
    1 https://stackoverflow.com/questions/49413005/replace-multiple -substrings-in-a-pandas-series-with-a-value <br>
    2 https://plotly.com/python/bubble-charts/ <br>
    3 https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d <br>
    4 https://plotly.com/python/bar-charts/
    5 https://stackoverflow.com/questions/28679930/how-to-drop-rows-from-pandas-data-frame-that-contains-a-particular-string-in-a-p <br>
    6 https://stackoverflow.com/questions/39141856/capitalize-first-letter-of-each-word-in-the-column-python<br>
    7 https://plotly.com/python/treemaps/ <br>
    8 https://plotly.com/python/line-and-scatter/ <br>
    9 https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php<br>

<b>Introduction:</b>

Internet is a very powerful tool today and it has been around for more than two decades now. In this project, we would like to explore some insights about countries and how they're related to internet usage. We have analyzed data to get correlations between internet usage and various other statistics of a country. Some of the insights we focused on is as follows:<br>
<b>1. Population of a country vs Internet Usage <br>
2. Internet usage vs Mental illness<br>
3. GDP per capita of a country vs Internet usage of a country<br>
4. Internet usage vs Security Breaches<br>
5. Secure Servers in a country vs No. of Data Breaches</b><br>

<b>Note:</b> Internet usage is defined as internet users as a percentage of the population

<b>Hypothesis 1 :</b><br>
<b>Hypothesis 1.1 : We assume that countries with larger populations have greater internet usage.</b><br>
Our general assumption is that countries that have a larger population have more resources compared to countries with a lower population, therefore countries with larger populations have easier access to the Internet. Thus we assume that countries with larger populations would have greater internet usage.

![](/Figures/1.PNG)

<b>Conclusion for Hypothesis 1.1 :</b><br>
From the trend seen above, we can conclude that internet usage of a country does not depend on the population. So our hypothesis that countries with larger populations have higher internet usage does not hold true. On the contrary it is seen that countries with comparatively lower population have higher internet usage

<b>World Map indicating Internet Usage Distribution worldwide.</b>

![](/Figures/2.PNG)

<b>Hypothesis 1.2 : There exists a trend between internet usage and mental illness (i.e the greater the number of internet users the higher the number of people having mental health disorders)</b><br>
The availability of Internet has caused a surge in socail media platforms over the last decade, although social media platforms have been a blessing, it certainly has a few drawbacks. One of the nagative aspects of social media platforms is it's affect on an individual's mental health. Excessive use of social media may tend to cause anxiety, depression, stress and other forms of mental illness. Therefore we assume that there is a relationship between internet usage and mental illness.

![](/Figures/3.PNG)

<b>Conclusion for Hypothesis 1.2:</b><br>
Through our analysis, we found that the no. of depressed people and the no. of internet users in a country are moderately correlated. From the visualization above, we can see that there are a few countries that have a larger no. of internet users compared to no. of depressed people and vice versa. Therefore our hypothesis that the greater the number of internet users in a country the greater the no. of individuals affected by mental illness does not hold true for the countries.

<b>Hypothesis 1.3 : There is a positive correlation between the GDP per capita of a country and internet users of that country.</b><br>
We assume that the countries which have higher GDP per capita values are categorized as developing countries, such devloped or dveloping countries have easier access to the Internet. Threfore therefore there would be a positive correlation between the GDP per capita of a country and it's internet usage.
![](/Figures/4.PNG)
<b>Conclusion for Hypothesis 1.3:</b><br>
From the visualization above we can conclude, that countries with higher GDP per capita values tend to have a higher average of internet users.

<b>Hypothesis 2 :We expect that countries with higher internet usage are more prone to security breaches.</b><br>
Countries that have higher internet usage will have higher volumes of personal data being collected. Therefore, we assume that these countries will be more prone to security breaches.

![](/Figures/5.PNG)

<b>Conclusion for Hypothesis 2:</b><br>
We can conclude that there isn't a strong linear relationship between data breaches and average internet usage over the years.Therefore our proposed hypothesis does not hold true.

<b>Suggestion for Hypothesis 2:</b><br>
Whether the population of a country plays a role in the no. of databreaches?<br>

![](/Figures/7.PNG)

We can see that countries with larger populations, generally have higher no. of data breaches. Therefore the population of a country is realted to the number of data breaches that occur.

<b>Hypothesis 3: We expect that countries with higher secure internet servers would have lesser cases of data breaches</b><br>
The countries that have higher no. of secure servers will be well prepared for data breaches. Therefore we assume that the countires with higher number of seccure servers would have lesser data breaches.

![](/Figures/6.PNG)

<b>Conclusion for Hypothesis 3:</b><br>
Through the treemap above we can see that the countries that have higher no. of secure servers are also prone to more data breaches.Therefore our hypothesis does not hold true.
