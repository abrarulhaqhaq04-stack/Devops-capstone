pipeline {
    agent any

    environment {
        IMAGE = "abrar33001/todo-api"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    cd app
                    "C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    cd app
                    "C:/Program Files/Python313/python.exe" -m pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker --version
                    cd app
                    docker build -t %IMAGE%:%BUILD_NUMBER% -t %IMAGE%:latest .
                '''
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'DOCKERHUB-CRAD',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat '''
                    docker push %IMAGE%:%BUILD_NUMBER%
                    docker push %IMAGE%:latest
                '''
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }

        success {
            echo 'Pipeline completed successfully!'
            echo 'Docker image pushed to Docker Hub.'
        }

        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}

