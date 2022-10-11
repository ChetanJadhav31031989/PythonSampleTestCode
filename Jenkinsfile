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
                bat "set PATH=C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\;"
                bat 'set PATH=C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\;'
                bat 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python310\\python.exe --version'
            }
        }

    }
}
