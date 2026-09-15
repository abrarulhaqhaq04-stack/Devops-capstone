pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB-CRAD')
        IMAGE_NAME = 'abrar33001/todo-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        PATH = "C:\\Users\\abrar ul haq\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                dir('app') {
                    bat '"C:/Program Files/Python313/python.exe" -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('app') {
                    bat '"C:/Program Files/Python313/python.exe" -m pytest'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% -t %IMAGE_NAME%:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat 'echo|set /p="%DOCKERHUB_CREDENTIALS_PSW%"| docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin'
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
                bat "docker push %IMAGE_NAME%:latest"
            }
        }
    }

    post {
        always {
            bat(script: 'docker logout', returnStatus: true)
        }
        success {
            echo 'Pipeline succeeded! Image pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
