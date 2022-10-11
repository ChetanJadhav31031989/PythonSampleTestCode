/* Requires the Docker Pipeline plugin */
pipeline {
    agent any

    stages {

        stage('Checkout') { // Checkout (git clone ...) the projects repository
        steps {
        checkout scm
        }}

        stage('build') {
            steps {
                sh "set PATH=C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\;"
                sh 'set PATH=C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;'
                sh 'python --version'
            }
        }

    }
}
