WIP still under construction - pardon the mess

`　　　　　　　　ｒ＠      ESS | MESS | MESS | MESS | MESS | ME
ニニニニヽ　　./ /|｜      | MESS | MESS | MESS | MESS | MESS |
　　　　∥   ./ /.|｜      ESS | MESS | MESS | MESS | MESS | ME
0( ｡ дﾟ)∥ 　/ / 　|｜      | MESS | MESS | MESS | MESS | MESS |
]( つ¶つ¶　/ / 　 r ―､     ESS | MESS | MESS | MESS | MESS | ME
ﾄ┳ヽ厂￣`/ /　　　| 　|    | MESS | MESS | MESS | MESS | MESS |
｢￣￣￣L/_/　　　　jjjjj　　ESS | MESS | MESS | MESS | MESS | ME
(◎￣◎)三)=)三)  | MESS |  | MESS | MESS | MESS | MESS | MESS |
_______________________________________________________________

-=-=-=-=-=-=--=- INTRODUCTION -=-=-=-=-=-=--=-
HelloWorld, I am a security researcher and practitioner and working on python projects to gain a firmer grasp on automation and build a portfolio of small useful tools that I can leverage. I have little experience with script writing so take the contents of this project with a grain of salt. Furthermore I have leveraged LLMs to help generate and test this code, and to my eyes it looks good. Take another pinch of salt for that one.

-=-=-=-=-=-=--=- This Project -=-=-=-=-=-=--=-
This project is meant to scrape sites for security headlines and catalogue them into a weekly digest. The contents are scraped, the titles and urls are stored in CSVs dated for the scrape, then the weekly digest will dedup headlines and combine the CSVs from the last 7 days and the previous digest. From there the digest can be sent via email message, or imported to a website for tabling.
________________________________________________________________
               Current Stage and Next Steps
________________________________________________________________
Current: I have the scraper in production, and am staging out the weekly digest. 
    1. crontab is running a shell script daily at 8am local time
Next Up: Digest creation, and cleanup routines. Then making things better.
    1. Deduping and combing the recent headlines into a top 10 list
        a. will need to dedup headlines between digests too
    2. Cron job to remove old files and artifacts
        a. maybe databasing the results and wrapping CSV cleanup into the scraper routine
    3. Incorporate keyword filtering and weighting for better digests.
    4. Incorporate other news sources:
        * security week
        * krebs on security
        * hackernews
        * ars technica
        * local news
