# Could housing prices have an effect in South Korea's aging society?

Medium Link : https://medium.com/@sahn1998/could-housing-prices-have-an-effect-in-south-koreas-aging-society-b3d5f7b76dd0

### Methodology
To proceed with this project, I used apartment transaction API data provided by the South Korean Government. There are thousands of data about South Korea that you can access on this site : https://www.data.go.kr/index.do. This data was the most important piece that I needed to start my analysis of Seouls housing prices.

In order to gather data about Seoul's demographics, I extracted data that is also provided by the South Korean Goverment on this site : https://jumin.mois.go.kr/ageStatMonth.do.

Additionally, GIS data of South Korea's submuniciaplities were gathered from this site http://www.gisdeveloper.co.kr/?p=2332. This data allowed me to create a geodataframe for choropleth map visualization of Seoul's housing prices and population by demographic.

### Limitations
There were few limitations that could introduce some bias when it comes to the analysis.

1) Data Availability and Quality: The availability of relevant and reliable data was limited. Although most apartment transactions are required by law to be reported to the Government, it is likely that a lot of the smaller transactions were left out (smaller transactions meaning relatively cheap and broken down houses in certain areas of Seoul). Additionally, the population / demographic count that was provided by the South Korean Government does seem relatively inaccurate because the total population does not seem to accumulate to the statements that have been released by Republic of Korea.

2) External Factors : South Korea were among the strictest countries when it came to COVID-19 for the past four years. Due to this factor, South Korea has been impacted economically (like many other countries) which meant more conservative spending by the overall population, job losses, and financial market volatility leading to lower circulation of currency in the country. Thus, the South Korean Government implemented various measures to support the housing market during the pandemic. It is reasonable that these measures may have harshly impacted the housing market and thus it may seem like there is some correlation between the housing prices and the demographic shift when there is not. 
