pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python -m py_compile mathutils.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest --junit-xml test-reports/results.xml test_math_utils.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
