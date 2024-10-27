Usage Examples
=============

Python Examples
-------------

Retrieving Questions
~~~~~~~~~~~~~~~~~~
.. code-block:: python

    import requests

    def get_questions(category, difficulty):
        url = "https://api.mvtnexus.com/v1/questions"
        params = {
            "category": category,
            "difficulty": difficulty
        }
        response = requests.get(url, params=params)
        return response.json()

Running Analysis
~~~~~~~~~~~~~~
.. code-block:: python

    def run_analysis(question_ids, analysis_type):
        url = "https://api.mvtnexus.com/v1/analysis/run"
        data = {
            "question_ids": question_ids,
            "analysis_type": analysis_type
        }
        response = requests.post(url, json=data)
        return response.json()

JavaScript Examples
----------------

Fetching Data
~~~~~~~~~~~
.. code-block:: javascript

    async function getQuestions(category, difficulty) {
        const url = `https://api.mvtnexus.com/v1/questions?category=${category}&difficulty=${difficulty}`;
        const response = await fetch(url);
        return response.json();
    }

Error Handling
~~~~~~~~~~~~
.. code-block:: javascript

    async function handleApiRequest(url, options) {
        try {
            const response = await fetch(url, options);
            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }
            return response.json();
        } catch (error) {
            console.error('API Request failed:', error);
            throw error;
        }
    }
