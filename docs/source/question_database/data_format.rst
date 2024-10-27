Data Format Specification
=====================

The MVT Nexus question database uses a standardized CSV (Comma-Separated Values) format for data storage and management. This document provides detailed specifications for the data format and field requirements.

CSV Format
---------

File Format
~~~~~~~~~~
* Encoding: UTF-8
* Delimiter: Comma (,)
* Quote Character: Double quote (")
* Line Ending: Unix-style (\\n)
* Header Row: Required
* File Extension: .csv

Field Specifications
------------------

1. id
~~~~
* Type: Integer
* Format: Sequential number
* Required: Yes
* Unique: Yes
* Example: "1", "2", "3"

2. question
~~~~~~~~~
* Type: String
* Format: Complete sentence ending with question mark
* Required: Yes
* Max Length: 255 characters
* Example: "What is the capital of France?"

3. correct_answer
~~~~~~~~~~~~~~~
* Type: String
* Format: Precise answer text
* Required: Yes
* Max Length: 100 characters
* Example: "Paris"

4. choice_1, choice_2, choice_3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Type: String
* Format: Alternative answer options
* Required: Yes
* Max Length: 100 characters each
* Example: "London", "Berlin", "Madrid"

5. difficulty
~~~~~~~~~~~
* Type: Integer
* Format: 0, 1, or 2
* Required: Yes
* Valid Values:
    * 0: Basic
    * 1: Intermediate
    * 2: Advanced

6. Knowledge Category
~~~~~~~~~~~~~~~~~~
* Type: String
* Format: Main category name
* Required: Yes
* Valid Values:
    * "Astronomy"
    * "Geography"
    * "Literature"
    * "Mathematics"
    * "Science"
    * "General Knowledge"

7. Topic Focus
~~~~~~~~~~~~
* Type: String
* Format: Specific topic within category
* Required: Yes
* Example: "Capital Cities", "Authors & Literature"

Sample CSV Row
------------
.. code-block:: text

    id,question,correct_answer,choice_1,choice_2,choice_3,difficulty,Knowledge Category,Topic Focus
    1,"What is the capital of France?","Paris","London","Berlin","Madrid",0,"Geography","Capital Cities"

Data Validation Rules
------------------

Required Fields
~~~~~~~~~~~~~
All fields are required and must not be empty.

Uniqueness Constraints
~~~~~~~~~~~~~~~~~~~
* id must be unique across the entire database
* question text should be unique
* correct_answer and choices must be different within each question

Value Constraints
~~~~~~~~~~~~~~
1. difficulty must be 0, 1, or 2
2. Knowledge Category must match defined categories
3. Topic Focus must be relevant to the Knowledge Category

Format Validation
~~~~~~~~~~~~~~~
1. question must end with a question mark
2. No trailing/leading whitespace in any field
3. No empty or NULL values allowed
4. Proper capitalization in all text fields

Best Practices
------------

Data Entry
~~~~~~~~~
1. Maintain consistent capitalization
2. Use clear, concise language
3. Verify all answers before entry
4. Check for duplicate questions
5. Ensure logical answer choices

File Management
~~~~~~~~~~~~~
1. Regular backups
2. Version control
3. Validation before import
4. Regular format compliance checks
5. Automated error checking

Quality Control
~~~~~~~~~~~~~
1. Peer review of new entries
2. Regular data audits
3. Automated format validation
4. Category consistency checks
5. Difficulty level verification

Tools and Scripts
---------------
Common tools for working with the database:

.. code-block:: python

    import pandas as pd
    
    # Read CSV file
    df = pd.read_csv('questions.csv')
    
    # Basic validation
    assert df['difficulty'].isin([0, 1, 2]).all()
    assert df['id'].is_unique
    
    # Check for required fields
    assert not df.isnull().any().any()

Error Handling
------------
Common error types and resolution:

1. Format Errors
    * Invalid CSV formatting
    * Missing fields
    * Incorrect delimiters

2. Data Errors
    * Duplicate IDs
    * Invalid difficulty levels
    * Inconsistent categories

3. Content Errors
    * Duplicate questions
    * Invalid answer choices
    * Incorrect categorization
