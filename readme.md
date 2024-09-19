# Tebby Bear Corner: Where Every Teddy Has a Tale

## Table of Contents

[Description](#description) | [Features](#features) | [Result](#result) | [Technologies](#technologies) | [Installation](#instalation) | [Usage](#usage) | [Disclaimer](#discalimer)

## Description

This project was created using Python, Django and Tailwind to resemble a marketplace where users can put their old teddy bears up for sale. 

## Features

### Existing Features

- Sign up 
- Sign in
- Log out
- Dashboard displaying user items
- Add new item for sale, listing: price, image, description, name and category
- Update listing details: price, image, description, name and an option to select whether or not the item was sold
- Navbar showing site name, create new listing, browsing, inbox, dashboard and log out buttons
- Search page featuring search bar, categories and a clear search option
- Communication between users with inbox and conversation page


### Features to consider adding

- Email verification
- Image Galery
- Delete conversation
- Improve Design
- Add item to cart
- Remove Item from cart
- Add checkout page
- Add 'view' and 'add to cart' buttons on item card
- Add cookies
 
## Result
1. picture or giff


## Technologies

Here's an overview of the technologies used to build this template application:

### Python

[Python](https://www.python.org/) is a high-level programming language used for backend development.

### Django

[Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework for creating custom designs without having to leave your HTML.

I also used:

- [Black](https://black.readthedocs.io/en/stable/) for Python code formatting
- [Prettier](https://prettier.io/) for code formatting


## Instalation

1. Clone the repository.
2. Navigate to the project directory 

## Usage

1. Install python3. Note than Python3 is normally installed on macOS. If you need a newwer version, you can use homebrew:
   ```
   brew install python
   ```

3. Install django.
   ```
  pip install django
   ```

### Set up your project

Navigate to root/docs and follow these steps:

1. Apply the database migrations:

  ```
  python manage.py migrate
   ```

2. Create a superuser account to access the admin panel:
  ```
  python manage.py createsuperuser
   ```

3. Collect static files::
  ```
  python manage.py collectstatic
   ```

### Start

Navigate to root/docs and follow these steps:

1. Run:
```
 python manage.py runserver
 ```

2. As user

  - Visit `http://127.0.0.1:8000/`

3. As admin

- Visit `http://127.0.0.1:8000/admin/` to log in with the superuser account.
- Manage users, items, and conversations from the Django admin interface.

**Note:** The media files have been added to .gitignore so it is recommended to add your own listings.

### Testing

## Disclaimer

This project is a work in progress and is intended for educational purposes. Use at your own risk and contribute to improve its functionality.
