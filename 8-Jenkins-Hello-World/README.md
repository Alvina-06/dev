# Assignment 8: Creating a Hello World Jenkins Job

## Aim
To create and execute a Freestyle Jenkins job that retrieves a shell script from GitHub and displays `Hello, Jenkins!` in the console output.

## Tools Used
- Jenkins
- Git and GitHub
- Shell scripting
- Docker

## GitHub Repository
Repository: [Devops](https://github.com/Alvina-06/dev.git)

The repository contains the `hello-world.sh` script:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

## Procedure
1. Created the `hello-world.sh` shell script.
2. Initialized Git and committed the script to the repository.
3. Pushed the script to GitHub.
4. Created a Freestyle project named `HelloWorld` in Jenkins.
5. Configured Source Code Management to use the GitHub repository and the `main` branch.
6. Added an Execute shell build step to run the script.
7. Saved the job and clicked **Build Now**.
8. Verified the console output and confirmed that the build completed successfully.

## Output

The Jenkins console displayed:

```text
Hello, Jenkins!
Finished: SUCCESS
```

![Jenkins Job Output](jenkinsjob.png)

## Result
Successfully created and executed a Hello World Jenkins Freestyle job using a shell script stored in GitHub.