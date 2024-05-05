# RSS Reader

# About
This was developed as a final project for Harvard University's CS50x Introduction to Computer Science.<br>
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
* This is main page that displays all currently added RSS feed entries, it features an accodion dropdown to view the articles content. <br>
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/6800db83-f421-4b50-9d2c-334f8bed9f00)

#### Manage Feeds
* This is the admin page of the application, which allows users to add valid RSS feeds, and remove unwanted RSS feeds. <br>
* Additionally displays all current RSS feeds that have been added in a table. <br>
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/04b9825c-4090-4a27-b5ae-8dde7b29b2f3)

#### Login Page
* This is the login page, where users may login after registering for an account. <br>
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/3136ffcc-626c-4507-a890-927b39e0ed5f)

#### Register Page
* This is the registration page that allows users to register for an account, and start using this application. <br>
![image](https://github.com/Kagura374/RSS-Reader/assets/126167792/d8dc3279-d45a-43be-9083-8af5d4f98f89)

# Installation
Install [pip](https://pip.pypa.io/en/stable/installation/)
```
git clone https://github.com/Kagura374/RSS-Reader.git
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
