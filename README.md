**Backend Assignment**

**Tech Stack you can use: [Any of the mentioned below]**

1. **Node.js / Nest.js**
2. **Python [Flask / Django]**
3. **Java Spring Boot**
4. **Go**

**Project Description:**

You will be building an application that allows users to create and participate in timed quizzes. The application should have a RESTful API that provides functionalities for creating and retrieving quizzes.

**Functionalities:**

- **Create a Quiz:** Users should be able to create a quiz by sending a POST request to the API with the following fields:
  - `POST /quizzes`
    - question: the text of the question
    - options: an array of the answer options for the question
    - rightAnswer: the index of the correct answer in the options array
    - startDate: the date and time when the quiz should start
    - endDate: the date and time when the quiz should end

- **Get Active Quiz:** Users should be able to retrieve the active quiz (the quiz that is currently within its start and end time).
  - `GET /quizzes/active`

- **Get Quiz Result:** After 5 minutes of the end time of a quiz, users should be able to retrieve the result of the quiz. The result is basically the right answer.
  - `GET /quizzes/:id/result` (where `:id` is the ID of the quiz)

**Requirements:**

The application should be built using Node.js, Java, Python, and any relevant frameworks.

The quizzes created by users should be stored in a database of your choice (e.g., MongoDB, MySQL, etc.).

The API should have the following endpoints:

- `POST /quizzes` - to create a new quiz
- `GET /quizzes/active` - to retrieve the active quiz (the quiz that is currently within its start and end time)
- `GET /quizzes/:id/result` - to retrieve the result of a quiz by its ID
- `GET /quizzes/all` - to retrieve all quizzes

The API should be well-documented, and the code should be well-organized and easy to read.

The API should implement error handling for all endpoints and return appropriate error responses.

**The API should have a status field for each quiz:**

- inactive: before the start time of the quiz
- active: during the time when the quiz is available
- finished: after the end time of the quiz

The status field should be updated automatically by the application based on the start and end time of each quiz.

**Bonus Points:**

- Implement rate-limiting to prevent abuse of the API.
- Implement caching to reduce the response time of frequently accessed data.

**Submission**: You will be required to submit the following:

- A link to the Github repository containing your application code.
- A link to the hosted API.
- Video for API or Postman collection with a deployed link.

**IMPORTANT NOTE: Use Cron Job for changing the status of the quiz based on its start time**

For any concerns email [amandeep@heliverse.com](mailto:amandeep@heliverse.com)
**Backend Assignment**

**Tech Stack you can use: [Any of the mentioned below]**

1. **Node.js / Nest.js**
2. **Python [Flask / Django]**
3. **Java Spring Boot**
4. **Go**

**Project Description:**

You will be building an application that allows users to create and participate in timed quizzes. The application should have a RESTful API that provides functionalities for creating and retrieving quizzes.

**Functionalities:**

- **Create a Quiz:** Users should be able to create a quiz by sending a POST request to the API with the following fields:
  - `POST /quizzes`
    - question: the text of the question
    - options: an array of the answer options for the question
    - rightAnswer: the index of the correct answer in the options array
    - startDate: the date and time when the quiz should start
    - endDate: the date and time when the quiz should end

- **Get Active Quiz:** Users should be able to retrieve the active quiz (the quiz that is currently within its start and end time).
  - `GET /quizzes/active`

- **Get Quiz Result:** After 5 minutes of the end time of a quiz, users should be able to retrieve the result of the quiz. The result is basically the right answer.
  - `GET /quizzes/:id/result` (where `:id` is the ID of the quiz)

**Requirements:**

The application should be built using Node.js, Java, Python, and any relevant frameworks.

The quizzes created by users should be stored in a database of your choice (e.g., MongoDB, MySQL, etc.).

The API should have the following endpoints:

- `POST /quizzes` - to create a new quiz
- `GET /quizzes/active` - to retrieve the active quiz (the quiz that is currently within its start and end time)
- `GET /quizzes/:id/result` - to retrieve the result of a quiz by its ID
- `GET /quizzes/all` - to retrieve all quizzes

The API should be well-documented, and the code should be well-organized and easy to read.

The API should implement error handling for all endpoints and return appropriate error responses.

**The API should have a status field for each quiz:**

- inactive: before the start time of the quiz
- active: during the time when the quiz is available
- finished: after the end time of the quiz

The status field should be updated automatically by the application based on the start and end time of each quiz.

**Bonus Points:**

- Implement rate-limiting to prevent abuse of the API.
- Implement caching to reduce the response time of frequently accessed data.

**Submission**: You will be required to submit the following:

- A link to the Github repository containing your application code.
- A link to the hosted API.
- Video for API or Postman collection with a deployed link.

**IMPORTANT NOTE: Use Cron Job for changing the status of the quiz based on its start time**