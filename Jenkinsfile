pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/satwi26/mlops_assignment.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                bat 'python src\\train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-app:latest .'
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                minikube image load mlops-app:latest
                kubectl apply -f kubernetes/deployment.yaml
                kubectl apply -f kubernetes/service.yaml
                '''
            }
        }
    }
}
