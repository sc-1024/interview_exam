pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'test-docker-compose-ci', url: 'https://github.com/sc-1024/interview_exam.git'
            }
        }

        stage('Install Python3 and Poetry') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip

                    curl -sSL https://install.python-poetry.org | python3 -

                    export PATH="$HOME/.local/bin:$PATH"

                    poetry --version

                    cd api_automation/star_wars
                    poetry install --no-root

                    poetry run pytest -v
                '''
            }
        }
    }
}
