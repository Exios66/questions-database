Database Structure
=================

The MVT Nexus question database follows a structured organization that facilitates efficient data management and retrieval. This document outlines the core structural elements of the database.

File Organization
---------------
The database is organized into multiple CSV files:

* ``Expanded_Questions_Full_Columns.csv`` - Main comprehensive question database
* Subject-specific files:
    * ``Astronomy_Questions.csv``
    * ``General Knowledge_Questions.csv``
    * ``Geography_Questions.csv``
    * ``Literature_Questions.csv``
    * ``Science_Questions.csv``

Database Schema
-------------
Each question entry contains the following fields:

.. code-block:: text

    id                  - Unique identifier for each question
    question            - The actual question text
    correct_answer      - The correct answer to the question
    choice_1           - First alternative answer choice
    choice_2           - Second alternative answer choice
    choice_3           - Third alternative answer choice
    difficulty         - Difficulty level (0-2)
    Knowledge Category - Main category of knowledge
    Topic Focus        - Specific topic within the category

Field Descriptions
----------------

id
~~
* Unique numerical identifier
* Sequential numbering
* Used for reference and tracking

question
~~~~~~~~
* Clear, concise question text
* Formatted for multiple-choice responses
* Consistent grammatical structure

answer fields
~~~~~~~~~~~~
* correct_answer: The verified correct response
* choice_1-3: Carefully selected incorrect options
* All options are mutually exclusive
* Similar length and structure for fairness

difficulty
~~~~~~~~~
Three-level scale:

* 0: Basic/Elementary level
* 1: Intermediate level
* 2: Advanced/Complex level

Knowledge Category
~~~~~~~~~~~~~~~~
Main subject areas including:

* Astronomy
* Geography
* Literature
* Mathematics
* Science
* General Knowledge

Topic Focus
~~~~~~~~~~
Specific subtopics within each category:

* Capital Cities (Geography)
* Authors & Literature (Literature)
* Chemistry (Science)
* Planets (Astronomy)
* Arithmetic (Mathematics)
* Miscellaneous (General Knowledge)

Data Integrity
-------------
The database maintains several integrity measures:

* Unique IDs across all entries
* Consistent formatting across all fields
* Verified correct answers
* Cross-referenced categories and topics
* Standardized difficulty ratings

This structured approach ensures:

* Easy data retrieval and filtering
* Consistent question quality
* Reliable difficulty assessment
* Clear category organization
* Efficient database maintenance
