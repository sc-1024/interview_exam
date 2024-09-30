pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'test-docker-compose-ci', url: 'https://github.com/sc-1024/interview_exam.git'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dockerImage.inside {
                        sh '''
                            cd api_automation/star_wars
                            poetry run pytest -v
                        '''
                    }
                }
            }
        }
    }
}