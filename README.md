# RSS Reader

# About
This was developed as a final project for Harvard University's CS50x Introduction to Computer Science.<br>
Here's a quick video demo: [click me!](https://youtu.be/PshoiHSE_Bw).<br>
The main idea of this project came from my interest in RSS feeds. <br>
I've used many different feeds before, so I thought of taking a crack at making one.

# Features
* RSS feed reader and parser
* Simple and easy to use
* Allows for adding and removing of feeds
* Displays currently added feeds with a simple interface
* User login for safe access

# Layout
#### Main page
* The is the main page that displays all currently added RSS feed entries, it features an accodion dropdown to view the articles content. <br>
* It also displays the author of the feed and the source to the article.
* So the code behind this page stores the get_feeds function in a variable and then returns that along with the render template. <br>
* The get_feeds function is quite complex, so firstly it connects to the databse and pulls out the title, and url associated with the user_id currently logged in. <br>
* Then it gets passed to feedparser. Feedparser then parses the url and returns 3 items from the feed, the title, the link, and the summary. That information is then appended to a dictionary.
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/6800db83-f421-4b50-9d2c-334f8bed9f00)

#### Manage Feeds
* This is the admin page of the application, which allows users to add valid RSS feeds, and remove unwanted RSS feeds. <br>
* Additionally displays all current RSS feeds that have been added, in a table. <br>
* The code beind this page consists of a few parts. <br>
* Firstly it gets the form data submitted in the "Add Feeds" forms, and stores them in two variables. <br>
* Then it passes the received url to feedparser, and it checks if the feed is valid. <br>
* If not then it spits out an error, if it is, then it inputs the title and url values into the database. <br>
* Then lastly it returns a success message and redirects the user back to the page. <br>
* As for the remove feeds, it's passed off to a seperate function route. <br>
* It functions by again receiving the form data inputted into the "Remove Feed" form, then stores that in a variable. <br>
* It then checks if the feed submitted exists in the database, if it doesn't then it spits out an error. <br>
* If it does, then it deletes that entry from the database; flashes a success message, then redirects back to the page.
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/04b9825c-4090-4a27-b5ae-8dde7b29b2f3)

#### Login Page
* This is the login page, where users may login after registering for an account. <br>
* The code behind this page is quite simple. <br>
* Firstly it checks if the username supplied in the username form exists in the database, then cross checks the password supplied in the password form against the stored hash in the database. <br>
* If it doesn't match, then it spits an error. <br>
* If it does then it stores the session user_id and redirects them to the home page. <br>
* The flipside of this is the logout function, which simply just clears the session, and redirects.
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/3136ffcc-626c-4507-a890-927b39e0ed5f)

#### Register Page
* This is the registration page that allows users to register for an account, and start using this application. <br>
* Likewise this page's code is quite simple. <br>
* It takes both the username, and password supplied in the forms, and stores them in two variables. <br>
* It then check if the provided username is unique against the other entries in the database, if it isn't then it gives an error. <br>
* If it is then it proceeds to check if the password provided is of the adequate length; 8 characters. <br>
* If not then again an error, if it is more than 8 characters, then it stores both the username and password in the database; remembers the session user_id and redirects to the home page.
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/d8dc3279-d45a-43be-9083-8af5d4f98f89)

# Installation
Install [pip](https://pip.pypa.io/en/stable/installation/)
```
git clone
cd /project
pip install -r requirements.txt
flask run
```
# Usage
* Register an account
* Navigate to "manage feeds"
* Add a valid rss feed into the "URL" form
* Navigate back to "home"
* You should now be able to view the entries from the rss feed!

# Credits
* [CS50x](https://cs50.harvard.edu/x/2024/) <br>
* [Feedparser](https://github.com/kurtmckee/feedparser) <br>
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) <br>

# License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.
