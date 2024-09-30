pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'test-docker-compose-ci', url: 'https://github.com/sc-1024/interview_exam.git'
            }
        }

        stage('Install Python3') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                    curl -sSL https://install.python-poetry.org | python3 -
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd api_automation/star_wars
                    python3 -m pip install poetry
                    poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    cd api_automation/star_wars
                    poetry run pytest -v
                '''
            }
        }
    }
}
