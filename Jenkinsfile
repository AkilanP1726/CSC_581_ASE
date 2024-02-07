pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 -m py_compile mathutils.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junit-xml test-reports/results.xml test_math_utils.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    emailext (attachLog: true, body: '$DEFAULT_CONTENT', replyTo: '$DEFAULT_REPLYTO', subject: '$DEFAULT_SUBJECT', to: 'akilanp17@gmail.com')
                }
            }
        }
    }
}