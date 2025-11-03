pipeline {
  agent any
  environment {
    DOCKER_HUB_CREDENTIALS = 'docker-hub-cred' // will set later in Jenkins
    DOCKER_HUB_REPO = 'YOUR_DOCKERHUB_USERNAME/mlops-iris' // change this
  }
  stages {
    stage('Checkout'){ steps{ checkout scm } }
    stage('Train'){ steps{ sh 'python3 -m pip install -r requirements.txt'; sh 'python3 train_model.py' } }
    stage('Docker Build & Push'){ steps{
      script{
        docker.withRegistry('', DOCKER_HUB_CREDENTIALS){
          def img = docker.build("${env.DOCKER_HUB_REPO}:${env.BUILD_NUMBER}")
          img.push()
          img.push('latest')
        }
      }
    } }
  }
}