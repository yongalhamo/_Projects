Fall of 2021,I took part in a data science bootcamp *METIS*, where I was challenged to utilize my analytical skills to dive into the MTA turnstile dataset and help an organization find spots around the city that would be optimal for volunteer placements.

**Background**

*WomenTechWomenYes* (WTWY) is a new  and growing non profit organization, that focuses on increasing the participation of women in the technological space. They have an annual summer gala in New York City, to widen their reach and gather donations for the cause from passionate attendees. This year , for the upcoming gala, they are interested in harnessing the power of data and analytics, to optimize the effectiveness of their street volunteer team who would be signing on people for the event and for newsletter.To be precise, WTWY is requesting for my engagement in finding optimal spots around the city, where they can gather the most signatures, attendees, and donors for the gala.

**Dataset**

 The Primary data for this analysis was  [MTA turnstile data](http://web.mta.info/developers/turnstile.html),which contains data on the entries and exits at each turnstile. A subset of the dataset(ranging from March -July 2019), was used for this analysis. These months fall right before the gala and taking a year prior to covid would most closely depict the subway foot traffic patterns for the upcoming summer. (assuming that  things will normalize by summer 2022)

 To supplement the MTA turnstile dataset, a dataset of zip codes for corresponding turnstiles were extracted using the Google API.

 Additionally, a dataset on corresponding neighborhoods, were used to filter the remaining locations, based on whether it was a tech hub or otherwise.(Since foot traffic related to tech are more likely to be interested in the topic at hand.)
  
  
### Tools

*  ingesting the raw data into a SQL database
*  pandas for data exploration
*  seaborn for further exploration though visualization
*  Tableau for visualization

Elaboration on analysis can be found [here](https://yongalhamo.github.io/porto/post/project-1/)



