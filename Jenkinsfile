pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB-CRAD')
        IMAGE_NAME = 'abrar33001/todo-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/abrarulhaqhaq04-stack/Devops-capstone.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'cd app && "C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'cd app && "C:/Program Files/Python313/python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    docker --version
                    cd app
                    docker build -t abrar33001/todo-api:27 -t abrar33001/todo-api:latest .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin'
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                bat "docker push %IMAGE_NAME%:latest"
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }

        success {
            echo 'Pipeline succeeded! Image pushed to Docker Hub.'
        }

        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}

