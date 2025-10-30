pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
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
        bat 'minikube image load mlops-app:latest'
        bat 'kubectl apply -f kubernetes\\deployment.yaml'
        bat 'kubectl apply -f kubernetes\\service.yaml'
      }
    }
  }
}
