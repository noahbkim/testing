# Testing, testing...

This framework is intended for use as the USC Image Understanding Lab's integrated subject testing platform.
From here, we'll be able to automatically proctor and score image recognition tasks.

## To Do

To keep things manageable, I'm maintaining a linear to do list.

- [ ] Add archived image uploading into some merged asset directory
- [ ] Create a test model for persistence and runtime access
- [ ] Create the test framework in SQL
- [ ] Create API endpoints for single page clients to run tests
- [ ] Finish the testing suite
- [ ] Add separation layer to conform to HIPAA
- [ ] Write up that last bit

## How to Set Up

- Clone the repository with `git clone https://github.com/uscfacestudy/testing.git`
- Install the environment `pipenv install`
  - If you need pipenv, `python3 -m pip install pipenv`
  - Close this shell and open another
- Start a shell in the environment `pipenv shell`
- Run the server `python manage.py runserver`
  - The server will automatically reload when you edit any files
