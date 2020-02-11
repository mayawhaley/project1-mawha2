# Project1

### What was the theme you chose?

The theme I chose for this project was pudding :)

### How did you pick your seraches to fit the theme?

I used the "complexSearch" endpoint which allowed me to add 3 seperate parameters to further specify my search for pudding recipes in Spoonacular. For the quotes,  
I initially chose to search a hashtag, but instead just searched two words because there were more theme specific tweets.

### What are at least 3 issues you encountered with your project? How did you fix them?

1.) I initially had most of my variables and code in my API files, but found that I couldn't access them in my main, so I had to figure out how to use Python modules to access the data in my API files.

2.) I had a hard time figuring out requests_oauthlib and os.getenv() for accessing my keys for the Twitter API. I tried testing in my local environment but I would only get "None" returned. I then realized python variables and environmental variable aren't the same thing. Through a lot of trial and error, I figured out that I should place the get call for the key's before the function and place them in variables. I then called the variables inside the function, which fixed my problem. 

3.) When trying to launch my app on Heroku, my app wouldn't run because the API keys needed to be regenerated. After regenerating the keys and updating the Config vars in Heroku, I was able to run the app.


### What are known problems, if any, with your project?

The quotes that I featured on my webpage include retweets as tweets.

### What would you do to improve your project in the future?

One of the points of improvement for this app would be to add a list of ingredients to go with the listed recipe. 
I would also have a more sophisticated design for the webpage.



