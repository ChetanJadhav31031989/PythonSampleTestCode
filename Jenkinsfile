/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('script') {
            steps {
                sh 'python Sample_Codes.py'
            }
        }
    }
}
