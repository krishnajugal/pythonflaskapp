pipeline {
  environment {
    registry = "jugalkrishna/flaskapp11"
    registryCredential = 'docker_id'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git branch: 'main', credentialsId: '208d3075-c6cb-4ec6-9f80-23a380986275', url: 'https://github.com/krishnajugal/pythonflaskapp'
      }
    }
    stage('Building image') {
      steps{
        script {
          sh 'docker build -t jugalkrishna/flaskapp11 ./front-end'
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
