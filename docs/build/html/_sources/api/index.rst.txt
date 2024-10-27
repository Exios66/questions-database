API Documentation
================

This section provides comprehensive documentation for the MVT Nexus API.

.. toctree::
   :maxdepth: 2
   :caption: API Contents:

   overview
   authentication
   endpoints
   examples

API Overview
-----------
The MVT Nexus API provides programmatic access to psychological assessment data and analysis tools.

Authentication
-------------
Security and authentication protocols:

* API key authentication
* OAuth2 implementation
* Access token management
* Rate limiting

API Endpoints
-----------
Available API endpoints and their functionality:

Questions Database
~~~~~~~~~~~~~~~~
.. code-block:: none

   GET /api/v1/questions
   GET /api/v1/questions/{id}
   POST /api/v1/questions
   PUT /api/v1/questions/{id}

Analysis Tools
~~~~~~~~~~~~
.. code-block:: none

   POST /api/v1/analyze
   GET /api/v1/analysis/{id}
   GET /api/v1/statistics

Usage Examples
------------
Code examples and implementation guidelines:

.. code-block:: python

   import mvt_nexus_api
   
   # Initialize client
   client = mvt_nexus_api.Client(api_key='your_key')
   
   # Fetch questions
   questions = client.get_questions(category='personality_disorders')
   
   # Run analysis
   analysis = client.analyze(data=questions, method='correlation')
