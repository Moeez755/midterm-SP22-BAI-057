pipeline {
    agent any

    environment {
        STUDENT_ID     = 'SP22-BAI-057'
        DOCKER_IMAGE   = 'midterm-sp22-bai-057'
        CONTAINER_NAME = 'midterm-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --quiet --upgrade pip
                    pip install --quiet -r requirements.txt pytest httpx
                '''
            }
        }

        stage('Generate Dataset') {
            steps {
                sh '''
                    . venv/bin/activate
                    python generate_dataset.py
                    wc -l dataset/train.csv
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    . venv/bin/activate
                    GIT_COMMIT=${GIT_COMMIT} BUILD_COMMIT=${GIT_COMMIT} python train.py
                    cat artifacts/metrics.json
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} -t ${DOCKER_IMAGE}:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} 2>/dev/null || true
                    docker rm   ${CONTAINER_NAME} 2>/dev/null || true
                    docker run -d --name ${CONTAINER_NAME} --restart unless-stopped -p 8000:8000 ${DOCKER_IMAGE}:latest
                    sleep 5
                    curl -fsS http://localhost:8000/health
                    echo ""
                    curl -s  http://localhost:8000/metrics
                '''
            }
        }
    }

    post {
        success {
            emailext(
                subject: "[${STUDENT_ID}] Jenkins Build #${BUILD_NUMBER} SUCCESS",
                body: """Student Reg No: ${STUDENT_ID}
Build:   ${BUILD_NUMBER}
Commit:  ${env.GIT_COMMIT}
Metrics: http://16.170.210.121:8000/metrics
Health:  http://16.170.210.121:8000/health
Job:     ${env.BUILD_URL}
""",
                to: 'qasimalik@gmail.com'
            )
        }
        failure {
            emailext(
                subject: "[${STUDENT_ID}] Jenkins Build #${BUILD_NUMBER} FAILED",
                body: "Build failed. See ${env.BUILD_URL}console",
                to: 'qasimalik@gmail.com'
            )
        }
    }
}
