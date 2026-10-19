# Exercise 9: Jenkins Multi-Stage Pipeline

## 1. Objective

To create and execute a multi-stage Jenkins Pipeline for a Python Flask application, demonstrating source code checkout, application file verification, test-file verification, and deployment preparation.

## 2. Tools and Technologies Used

- **Jenkins** – Pipeline automation
- **Docker** – Running Jenkins in a container
- **Git and GitHub** – Source code management
- **Python** – Application programming language
- **Flask** – Python web framework
- **Groovy** – Jenkins Pipeline scripting language

## 3. Project Structure

```text
9-Jenkins-Multi-Stage-Pipeline/
├── app.py
├── requirements.txt
├── test_app.py
├── Jenkinsfile
├── pipeline-stages.png
├── console-output.png
└── README.md
```

## 4. Application Files

### app.py

A simple Flask application that returns a greeting when the home route is accessed.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline!"

if __name__ == "__main__":
    app.run(debug=True)
```

### requirements.txt

Specifies the Flask dependency required by the application.

```text
flask==2.1.2
```

### test_app.py

Contains a unit test that checks the home route's response status and message. In this exercise, the pipeline verifies that the test file exists; it does not execute the unit test.

## 5. Pipeline Stages

The Jenkins pipeline consists of the following four stages:

1. **Checkout:** Retrieves the source code from the GitHub repository's `main` branch.
2. **Build:** Verifies that `app.py` and `requirements.txt` exist.
3. **Test:** Verifies that `test_app.py` exists.
4. **Deploy:** Creates a `python-app-deploy` directory and copies `app.py` and `requirements.txt` into it.

## 6. Execution Procedure

1. Created the Python Flask application and its supporting files.
2. Pushed the project files to the GitHub repository.
3. Opened Jenkins at `http://localhost:8080`.
4. Created a Pipeline job named `Python-MultiStage-Pipeline`.
5. Configured the pipeline to check out the source code from GitHub.
6. Defined the Checkout, Build, Test, and Deploy stages.
7. Saved the configuration and clicked **Build Now**.
8. Viewed the Console Output and verified that the pipeline completed successfully.

## 7. Screenshots

### Pipeline Stage View

The following screenshot shows the stages of the Jenkins pipeline and their execution status.

![Jenkins Pipeline Stage View](./Screenshots/pipeline-stages.png)

### Console Output

The console output confirms successful pipeline execution.

![Jenkins Pipeline Console Output](./Screenshots/console-output.png)

## 8. Expected Output

```text
Pipeline completed successfully!
Finished: SUCCESS
```

## 9. Result

Successfully created and executed a Jenkins multi-stage pipeline for a Python Flask application. The pipeline checked out the source code, verified the required application and test files, and prepared the deployment directory.

## 10. Conclusion

This exercise demonstrated how Jenkins Pipeline automates sequential stages in a CI/CD workflow. It introduced source code checkout, build verification, test-file verification, and deployment preparation using a declarative Jenkinsfile.

**Note:** This simplified pipeline verifies the presence of the test file but does not execute the Python unit tests, install Flask dependencies, or deploy a running Flask application.
