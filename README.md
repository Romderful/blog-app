# test-blog

This project has been built with :

    - Django rest framework for the backend
    - Nuxtjs for the frontend

📝 Content creation
- As a creator, I have access to a button that allows me to create an article.
- As a creator, in the creation page, I can create content and validate this creation.

📑 List and details
- As a user (creator or reader), I can view all the articles in the homepage
- As a user (creator or reader), I can view the article detail page

💓 Like the articles ( If you have some time left )
- As a reader, I can “like” an article by clicking on a heart icon in the detail page.
- As a user (creator or reader), I can see the likes in the detail page.

## Install

- backend :

    Set your location in the back folder with the following command :
    - cd back

    To install the dependencies :
    - pipenv install

    To make the database migrations :
    - ./manage.py migrate

    To create the superuser :
    - ./manage.py createsuperuser

- frontend :

    Set your location in the front folder with the following command :
    - cd front

    To install the dependencies :
    - yarn install

## Usage

- `(cd front && yarn dev)` run the frontend server.
- `(cd back && ./manage.py runserver)` run the backend server.

## License

[MIT](https://choosealicense.com/licenses/mit/)