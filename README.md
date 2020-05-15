# Kickstarting Your Project

![ideas](images/ideas.jpg)

## Table of Contents
- [Background](#Background)
- [Project Goal](#project-goal)
- [Data](#the-data)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Analysis](#analysis)
- [Conclusion](#conclusion)

---

## Background 

Kickstarter is a crowdfunding platform with a stated mission to "bring creative projects to life". Since its launch in 20019, it has attracted artists, designers, musicians, and creative people from all over the world to pitch their project ideas to the public in hopes to make their vision a reality. According to [Kickstarter](https://www.kickstarter.com/charter?ref=how_it_works), there have been more than 17 million people pledging a total of more than $4 billion to fund 445,000 projects. These projects include films, music, stage shows, comics, video games, technology, design, food and arts and crafts. 

---

## Project Goal

One would wonder what makes a kickstarter campaign successful. Let's wonder no more. We are going to use machine learning models to predict whether a campaign will meet its funding goal within 90 days of launched date. Hence to answer the question, "what can you leverage to make your campaign successful?"

---

## The Data

There are downloadable Kickstarter datasets that are being scraped monthly. The datasets I use have a total of 55 csv files that contain campaigns starting from April of 2009 up until April of 2020. I started with 204,625 rows and 38 columns of data; after removing duplicate entries, cancelled and live campaigns, irrelevant features, and campaigns with a length of more than 90 days, I was left with 169,591 datapoints to work with. 

The columns that I kept are:
- Backers Count (number of backers per campaign)
- Blurb (Brief description of the campaign)
- Profile 
- Country
- Deadline
- Goal
- Launched at
- Name 
- Pledged (funds raised)
- Slug
- Staff Pick
- State (successful or failed)

From these features, I was able to perform featuring to extract the following features:
- Launch month
- Launch year
- Category Type
- Campaign length
- Blurb length

---

## Exploratory Data Analysis

**How are listing price distributed across San Francisco?**

As expected, listing price generally concentrate on the lower end, with a handful of expensive listing with over $500 per night.

![all_listings](images/list_all.png)

**How do price vary between neighborhoods?**

Graph below shows average listing price for the top 20 most expensive neighborhoods along with count of listings in the neighborhood. It does not seem to me that count of listings affect price. Now I am curious to see what affects pricing other than the location of listings.

![top_20](images/top_20.png)


I calculated the price per person rate for each listing by dividing listing price by number accommodated to get the average price per person. I plotted them using their latitudes and longitudes. Colors are by average price per neighborhood, circle sizes are by price per person for each listing. This image shows that listings in center of the city tend of have higher price, and then listings facing the Golden Gate Bridge (North) are the highest priced. 


![coords_plot](images/coords_plot.png)


**One would think that listing price would increase as number of guests increases. Is that the case for listings in San Francisco?**

As it turns out not so much. This tells me that neighborhood might be the only factor that is affecting listing price.

![accomomdates](images/accomoates.png)


---

# Analysis

## Mission vs. Noe Valley

- Mission 
    - Avg price: $225.95
    - Count: 730

- Noe Valley
    - Avg price: $234.12
    - Count: 325

Here is the distribution of listing price between the two neighborhoods.

![mission_noe_dist](images/mission_noe_dist.png)

One tail hypothesis test varialbes:
- **Null Hypothesis:** Noe Valley is more expensive than Mission by chance.
- **Alternative Hypothesis:** Noe Valley is truly more expensive than Mission. 
- **Alpha Level:** 0.05
- **Welch Test Statistics:** 2.34
- **Degrees of Freedom:** 514.41
- **p-value:** 0.0099

According to my findings, we can see that the Welch's t-test statistics is 2.34. The probability of having this result, or more extreme, given the null hypothesis is true is 0.0099. This is statistically signficiant enough for us to reject the null hypothesis. Airbnb listings in Noe Valley are generally more expensive than Mission.

![mission_noe_curve](images/mission_noe_curve.png)

### Mann-Whitney U-test
I also performend a Mann-Whitney U-test with  similar result with a p-value of 0.016. Noe Valley is clearly more expensive than Mission.

## Inner Sunset vs. Outer Sunset

- Inner Sunset 
    - Avg price: $230.24
    - Count: 161

- Outer Sunset
    - Avg price: $153.97
    - Count: 277

Here is the distribution of listing price between the two neighborhoods.

![sunset_dist](images/sunset_dist.png)

One tail hypothesis test varialbes:
- **Null Hypothesis:** Inner Sunset is more expensive than Outer Sunset by chance.
- **Alternative Hypothesis:** Inner Sunset is truly more expensive than Outer Sunset. 
- **Alpha Level:** 0.05
- **Welch Test Statistics:** 2.95
- **Degrees of Freedom:** 281.25
- **p-value:** 0.0017

According to my findings, we can see that the Welch's t-test statistics is 2.95. The probability of having this result, or more extreme, given the null hypothesis is true is 0.0017. This is statistically signficiant enough for us to reject the null hypothesis. Airbnb listings in Inner Sunset are generally more expensive than Outer Sunset.

![sunset_curve](images/sunset_curve.png)

### Mann-Whitney U-test
 The Mann-Whitney U-test with similar result with a p-value of 0.0000. Inner Sunset is clearly more expensive than Outer Sunset.

# Conclusion

When I ran my hypothesis testing, my Welch's t-tests were returning different results from my Mann-Whitney U-tests. Reason being there are a couple of outliers in the neighborhoods with prices listed for more than $2,000 a night. As Welch's t-tests are sensitive to standard deviations, I removed all listing prices of more than $2,000 and they gave me similar results to my Mann-Whitney U-test. 

In conlusion, both Welch's t-tests and Mann-Whitney U Tests return statistically significant results to indicate Airbnb listing prices do vary by neighborhoods in San Francisco, even if they are in close proximity. If an investor wants to purchase a property in San Francisco for listing in Airbnb, the location of the property is a good indicator of how much to charge for the listing. 

 












