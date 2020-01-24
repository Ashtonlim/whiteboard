# WhiteBoard

**Introduction**

The core of what we want to accomplish is building a search engine for videos. Just like how google indexed and contextualized the web, our research found that are no serious offerings in in this space. The idea is simply to use advances in converting speech to text AI, converting sound into text information, that can be structured and searched. By no means does our application achieve that to any serious extent, but is a demonstration that the objective is possible. Although we honestly do not feel the current state of the application is very compelling, we do feel there are many use cases for this which will be discussed further below at **Applications.**

**Description**

In NTU, and many other schools, study materials are often accessed online. For example, the current BlackBoard system provides Learning Activity Management System (LAMS) provides videos as well as recorded lectures for students to watch. After doing some research, we found that people often have trouble finding videos that they want to watch when they are revising, especially during examination period. This is due some courses having too many short videos and/or being poorly organized. Hence, we developed an application that uses Google’s speech to text AI API to generate subtitles for a video, allowing it to be searched.

**Problem**

When doing tutorials or during exams, students may often refer to lecture videos for solutions. however, due to the amount of lecture videos and lack of timestamps (sadly we did not this implement this in our product), the time required to find the right video and at the correct point can be significant.

**Product Functions**

The proposed application, “WhiteBoard”, aims to aid students with understanding subjects in school. With the current advancements in artificial intelligence (AI), the team will leverage in speech to text algorithms to aid students with understanding subjects at school.

Firstly, through the use of speech to text algorithms, video information which are already on NTU’s servers can have subtitles generated and embedded into videos. We decided to adopt Google’s cloud speech-to-text API to aid with this. As a result, lecture videos can be supported by the application to support subtitling in over 120 languages and variants. The obtained subtitles are then embedded into the videos.

Secondly, in order to cut down the time students take to find the right supplementary video when facing doubts, the team has integrated a search engine which not only loops through titles of videos, but also subtitles and descriptions. Search words found in the videos are then returned and displayed.
Besides aiding students with learning, by establishing this application, this helps the school to stay ahead in the education industry, creating an up-to-date image, improving the reputation of the school. 

**Technical**

The application is built using Django and python. There’s no real reason we choose this other than that it was something some of us were familiar with. To build this framework on your own computer. Install Django, Django rest framework and python.

Simply run “python manage.py runserver” in the root directory to spin the server and use the application on localhost.

In its current state, the application is not very scalable. As we are manually using google’s API to produce subtitles, and did not built a bulk import tool to import into our database. We also wanted to build a scraper but decided it was not worth the time and wanted to focus on other aspects.

**Applications**

We believe that further developing this technology could be useful for a number of applications. In the current space, we could add features like 
-	Allowing students to record tutorials and labs so that those can be searched through as well, as students often do. 
-	Building a scrape tool to search relevant videos on platforms like Khan academy, YouTube, etc. to built an entire complimentary learning platform.


Even for Shopee, technology like this could be useful. By scraping the web, it would be possible to find videos discussing and reviewing products being sold. This data could be valuable to both Shopee and as for customers as they provide another source of reviews, especially in video format where it is likely to be considered as something more authentic.



