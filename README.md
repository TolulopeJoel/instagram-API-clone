# Instagram API Clone

This is a clone of the Instagram API built using Django REST framework. The API allows users to create posts, comment on posts, and like posts. The API also includes authentication, filtering, and pagination features.


## Usage

Once the development server is running, you can use the API by sending HTTP requests to the endpoints listed below. You can use a tool like `curl` or a program like Postman to send requests.


## Features

- User registration and authentication
- Create, update, and delete posts
- Create, update, and delete comments
- Like and unlike posts
- Filter and search posts by username and caption
- Paginate posts

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/instagram-clone-api.git
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Run the migrations:
```
python manage.py migrate
```

4. Create a superuser:
```
python manage.py createsuperuser
```

5. Start the development server:
```
python manage.py runserver
```


## API Endpoints

### Authentication

- `POST /api/token/` - Obtain a token for authentication
- `POST /api/token/refresh/` - Refresh an expired token

### Users

- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Retrieve a user by ID

### Posts

- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{id}/` - Retrieve a post by ID
- `PUT /api/posts/{id}/` - Update a post by ID
- `DELETE /api/posts/{id}/` - Delete a post by ID

### Comments

- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create a new comment
- `GET /api/comments/{id}/` - Retrieve a comment by ID
- `PUT /api/comments/{id}/` - Update a comment by ID
- `DELETE /api/comments/{id}/` - Delete a comment by ID

### Likes

- `POST /api/posts/{id}/like/` - Like a post
- `POST /api/posts/{id}/unlike/` - Unlike a post

### Filtering and Pagination

- `GET /api/posts/?username={username}` - Filter posts by username
- `GET /api/posts/?caption={caption}` - Filter posts by caption
- `GET /api/posts/?search={search_term}` - Search posts by username or caption
- `GET /api/posts/?page={page_number}` - Paginate posts

## Contributing

If you'd like to contribute to this project, please submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
