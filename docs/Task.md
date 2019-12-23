# Scenario
You are an AI expert working for a Legal AI company. The company wants to create a product that automatically sorts legal documents into specific categories based on the documents' metadata. You are tasked with analysing the data and making a recommendation as to the best way to pre-process it for training a classifier.

The data set is attached to this email. It’s the exact same data in three different file formats. This is for your convenience. Choose whatever data format works best for you.

The test is broken down into tiers of increasing complexity. It is okay to submit a partial solution. It is favourable to submit a great implementation of fewer tiers than to sloppily solve all tiers. We care more about the analysis than building the classifier, though building a classifier is, of course, great, too. The expected time to complete the full test is 3-6 hours. Please work within this timeframe. We generally give candidates two weeks to complete the test, but with the holidays coming up we can relax that requirement a bit. If you can submit a test solution before Christmas, we will do our best to schedule interviews before the break. However, if you unable to do so, then just let me know and we can make a suitable alternative arrangement.


# Expectations
Please write a report and, if you are attempting higher tiers, create an app that can train a model from the provided data. The app should then be able to be called using the first eight fields as an input and predict the last field (category) as an output class. 

- Write the report in whatever format you think best communicates the information. We are looking for concise insights, not elaborate detail in the report
- Show you keep up-to-date with the platform by explaining your choices of libraries and machine-learning classifier 
- Provide your solution either as a zip file or as a git repository
- The solution must be entirely your own work

## Tier 1 ##
- Perform an analysis to find patterns, trends, and insights in the provided data. Explain the analytical methodologies you used to find them.

## Tier 2 ##
- Based on your analysis, suggest what specific additional data would enhance the classification accuracy
- Briefly explain your plan to curate the additional data you need.

## Tier 3 ##
- Write 1-2 paragraphs on how you would prevent a machine learning model from overfitting and underfitting on the training data 

## Tier 4 ##
- Create a list of all the ways the data could be transformed to improve the classification accuracy

## Tier 5 ##
- Rank all your suggested data transformation in priority order in terms of their likely impact on classification accuracy. Pick the top two transformations and write a paragraph on why you think they will offer the most benefit
- Provide a brief overview of your prioritisation method

## Tier 6 ##
- Implement your chosen top two data transformations in a Python application that pre-processes the data

## Tier 7 ##
- Create an app that reads the data and creates a classifier model, then takes eight command line inputs and outputs a prediction result. The app must be able to generate the model from the training data with the code submitted. It must work offline, and it must not take any inputs other than the data
- Explain how you validated your implementation
- Present the results using a metric that you think is best
- Provide some documentation in a readme file of how to install and run your app
- Explain why you believe you’ve picked the best classification algorithm for the job
