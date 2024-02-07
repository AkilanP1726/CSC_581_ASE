pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'python -m py_compile math_utils.py'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest --junit-xml test-reports/results.xml test_math_utils.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
