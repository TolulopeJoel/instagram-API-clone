# Instagram Clone API
This is a Django REST Framework API that provides Instagram-like functionality for users to create and share posts, comment on other users' posts, and like posts.

## Getting Started
To get started with this project, you can clone the repository from GitHub:


```git clone https://github.com/your-username/instagram-clone-api.git```

Once you've cloned the repository, you can install the required packages by running:

Copy code
pip install -r requirements.txt
Next, you'll need to run the database migrations to set up the database schema:

Copy code
python manage.py migrate
You can then start the development server by running:

Copy code
python manage.py runserver
The API will be available at http://localhost:8000/.

API Endpoints
The API provides the following endpoints:

/posts
GET /posts: Retrieve a list of all posts.
POST /posts: Create a new post.
/posts/{post_id}
GET /posts/{post_id}: Retrieve a specific post.
PUT /posts/{post_id}: Update a specific post.
DELETE /posts/{post_id}: Delete a specific post.
/posts/{post_id}/comments
GET /posts/{post_id}/comments: Retrieve a list of comments for a specific post.
POST /posts/{post_id}/comments: Create a new comment for a specific post.
/posts/{post_id}/comments/{comment_id}
GET /posts/{post_id}/comments/{comment_id}: Retrieve a specific comment for a specific post.
PUT /posts/{post_id}/comments/{comment_id}: Update a specific comment for a specific post.
DELETE /posts/{post_id}/comments/{comment_id}: Delete a specific comment for a specific post.
/posts/{post_id}/likes
GET /posts/{post_id}/likes: Retrieve a list of likes for a specific post.
POST /posts/{post_id}/likes: Like a specific post.
/posts/{post_id}/likes/{like_id}
GET /posts/{post_id}/likes/{like_id}: Retrieve a specific like for a specific post.
DELETE /posts/{post_id}/likes/{like_id}: Unlike a specific post.
Authentication
Authentication is required to access the API. You can obtain an access token by sending a POST request to the /api/token/ endpoint with valid credentials. The access token can then be used in the Authorization header for subsequent requests.

Filtering
You can filter the list of posts by the user who created the post by using the author query parameter. For example, to retrieve all posts created by the user with ID 1, you can send a GET request to /posts/?author=1.

Pagination
The API provides pagination for the list of posts. By default, the API returns 10 posts per page. You can customize the page size by setting the page_size query parameter. For example, to retrieve the first 20 posts, you can send a GET request to /posts/?page_size=20. You can navigate between pages using the next and previous links in the response metadata.

Contributing
If you'd like to contribute to this project, please submit a pull request on GitHub.


# Instagram API Clone

## Table of Contents

- [Instagram Clone API](#instagram-clone-api)
  - [Getting Started](#getting-started)
- [Instagram API Clone](#instagram-api-clone)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Filtering](#filtering)
  - [Pagination](#pagination)

## Description

This is a clone of the Instagram API built using Django REST framework. The API allows users to create posts, comment on posts, and like posts. The API also includes authentication, filtering, and pagination features.

## Installation

To use this API, you will need to have Python 3 and Django installed on your machine. Once you have these installed, you can follow these steps to get the API up and running:

1. Clone the repository to your local machine.
2. Create a virtual environment using `python3 -m venv env`.
3. Activate the virtual environment using `source env/bin/activate` (on Linux/Mac) or `env\Scripts\activate` (on Windows).
4. Install the required packages using `pip install -r requirements.txt`.
5. Run the migrations using `python manage.py migrate`.
6. Create a superuser account using `python manage.py createsuperuser`.
7. Start the development server using `python manage.py runserver`.

## Usage

Once the development server is running, you can use the API by sending HTTP requests to the endpoints listed below. You can use a tool like `curl` or a program like Postman to send requests.

## API Endpoints

The following endpoints are available in the API:

- `GET /api/posts/`: Get a list of all posts.
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/:id/`: Get a single post by ID.
- `PUT /api/posts/:id/`: Update a post by ID.
- `DELETE /api/posts/:id/`: Delete a post by ID.
- `GET /api/comments/`: Get a list of all comments.
- `POST /api/comments/`: Create a new comment.
- `GET /api/comments/:id/`: Get a single comment by ID.
- `PUT /api/comments/:id/`: Update a comment by ID.
- `DELETE /api/comments/:id/`: Delete a comment by ID.
- `POST /api/posts/:id/like/`: Like a post by ID.
- `POST /api/posts/:id/unlike/`: Unlike a post by ID.

## Authentication

The API includes authentication using JSON Web Tokens (JWT). To use the API, you will need to include a valid JWT in the `Authorization` header of your requests. You can obtain a JWT by sending a POST request to the `/api/token/` endpoint with your username and password.

## Filtering

You can filter the posts by user, date, or text using query parameters. Here are the available filters:

- `user`: Filter posts by the ID of the user who created them.
- `date_from`: Filter posts by the date they were created (after a certain date).
- `date_to`: Filter posts by the date they were created (before a certain date).
- `text`: Filter posts by the text in their caption.

To filter the posts, add the relevant query parameters to the `GET /api/posts/` endpoint.

## Pagination

The API includes pagination to limit the number of posts returned in each request. By default, the API returns 10 posts per page. You can change the number of posts returned
