API Endpoints
============

Questions API
-----------

GET /questions
~~~~~~~~~~~~
Retrieve questions based on criteria.

Parameters:
- category (string): Knowledge category
- difficulty (int): Difficulty level
- limit (int): Number of questions to return
- offset (int): Pagination offset

POST /questions
~~~~~~~~~~~~~
Add new questions to the database.

Required fields:
- question_text
- correct_answer
- category
- difficulty

Analysis API
----------

GET /analysis
~~~~~~~~~~~
Retrieve analysis results.

POST /analysis/run
~~~~~~~~~~~~~~~
Run analysis on specified questions.

Parameters:
- analysis_type
- question_ids
- parameters

Data Formats
----------
All endpoints accept and return JSON data.
