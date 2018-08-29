pipeline {
  agent any
  stages {
    stage('ssh') {
      steps {
        sshagent(['be16d4a5-ed50-4fcc-8639-c3768e8f375a']) {
          sh 'ssh maverick@192.168.1.70'
        }
      }
    }
  }
}
