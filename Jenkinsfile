/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {

        stage('Checkout') { // Checkout (git clone ...) the projects repository
        steps {
        checkout scm
        }

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
