# FlaskBlog
FlaskBlog is a full-featured blog web application built using Flask framework. It allows users to read, write, and comment on blog posts, as well as manage their own user profiles.

## Features
* User authentication (register, login, logout)
* User profile management (change username, email, password, profile picture)
* Blog post creation, modification, and deletion
* Pagination of blog posts and comments
* Search functionality to search for blog posts by title or content
* Responsive design for optimal viewing on different devices

## Installation
1. Clone this repository to your local machine
```
git clone https://github.com/chiefmatias/FlaskBlog.git
```

2. Change directory into the project root
```
cd FlaskBlog
```

3. Create a virtual environment and activate it
```
python3 -m venv env
source env/bin/activate
```

4. Install the required dependencies
```
pip install -r requirements.txt
```
5. Initialize the database and run the Flask application
```
python run.py
```

## Configuration
FlaskBlog comes with a config.py file that contains configuration settings for the application. You can modify these settings to suit your needs. For example, you can change the name of the database, the secret key used for encrypting session cookies, and the number of blog posts to display per page.

## Usage
Once you have installed and configured FlaskBlog, you can access the web application by visiting http://localhost:5000 in your web browser. From there, you can register a new user account, create blog posts, and interact with other users by commenting on their blog posts.







