# Quiz Application

## Tech Stack

The application is built using **Python** and the **Django** framework, specifically the **Django REST Framework**.

## Functionalities

### Create a Quiz

Users can create a quiz by sending a POST request to the API with the following fields: ✅

- `question`: The text of the question.
- `options`: An array of answer options for the question.
- `rightAnswer`: The index of the correct answer in the options array.
- `startDate`: The date and time when the quiz should start.
- `endDate`: The date and time when the quiz should end.

### Get Active Quiz

Users can retrieve the active quiz, which is the quiz currently within its start and end time.

### Get Quiz Result

After 5 minutes from the end time of a quiz, users can retrieve the result of the quiz, which is the right answer.

### Additional Requirements

- The quizzes created by users are stored in a **database of your choice** (e.g., MongoDB, MySQL, etc.).
- The API has the following endpoints:
  - `POST /quizzes` - Create a new quiz. ✅
  - `GET /quizzes/active` - Retrieve the active quiz. ✅
  - `GET /quizzes/{id}/result` - Retrieve the result of a quiz by its ID. ✅
  - `GET /quizzes/all` - Retrieve all quizzes. ✅
- The API is well-documented, and the code is well-organized and easy to read.
- The API implements error handling for all endpoints and returns appropriate error responses.
- Each quiz has a status field: ✅
  - `inactive`: Before the start time of the quiz.
  - `active`: During the time when the quiz is available.
  - `finished`: After the end time of the quiz.
- The status field is automatically updated by the application based on the start and end time of each quiz.

## Bonus Points

- Implemented rate-limiting to prevent abuse of the API. ✅
- Implemented caching to reduce the response time of frequently accessed data.❌