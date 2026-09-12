pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB-CRAD')
        IMAGE_NAME = 'abrar33001/todo-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        PATH = "C:\\Users\\abrar ul haq\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
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
            docker build -t %IMAGE_NAME%:%IMAGE_TAG% -t %IMAGE_NAME%:latest .
        '''
    }
}stage('Push to Docker Hub') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'DOCKERHUB-CRAD',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {
            bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
            bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
            bat 'docker push %IMAGE_NAME%:latest'
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
}
