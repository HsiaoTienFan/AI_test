# Document Classification tool

This documentation describes how to run the classification tool written for the purposes of the AI test for McCarthyFinch - Data Scientist position.



## Getting Started



#### Python Libraries
Please check *requirements.txt* file for the required libraries.

To install the above libraries in your environment, run the following command on Terminal/Command Prompt.

```
pip install -r requirements.txt
```

### Running the app
- The app can be run from the src directory using:

```
python main.py arg1 1arg2 arg3 arg4 arg5 arg6 arg7 arg8
```

Note that the arguments are pagesCount, wordCount, fileSize, priority, author, title, createdDate, lastEditedDate respectively.

- To retrain the model, run the following:

```
python main.py -r [-p arg1] [-s arg2]
```

Here -r activates the retraining, while -p and -s represents the testing data percentage and the seed value for the train test split.

- To perform model validation, run the following:

```
python main.py -v [-f arg1]
```

Where f is an optional input to the number of folds for cross-validation




### Report

The report for the test is stored in the docs folder
