pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // 檢出指定的分支
                git branch: 'test-docker-compose-ci', url: 'https://github.com/sc-1024/interview_exam.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // 假設你使用 Python 並且需要安裝依賴項
                sh '''
                    cd api_automation/star_wars
                    poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // 直接在 Jenkins 節點上運行測試
                sh '''
                    cd api_automation/star_wars
                    poetry run pytest -v
                '''
            }
        }
    }
}
