pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB-CRAD')pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB-CRAD')
        IMAGE_NAME = 'abrar33001/todo-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/abrarulhaqhaq04-stack/Devops-capstone.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:/Program Files/Python313/python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% -t %IMAGE_NAME%:latest ."
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
        IMAGE_NAME = 'abrar33001/todo-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/abrarulhaqhaq04-stack/Devops-capstone.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:/Program Files/Python313/python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% -t %IMAGE_NAME%:latest ."
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
