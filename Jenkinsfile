pipeline {
    agent any
    stages {
        stage('Construir y levantar contenedores') {
            steps {
                sh 'docker compose up --build --abort-on-container-exit'
            }
        }
        stage('Ejecutar operacion de ejemplo') {
            steps {
                sh 'docker compose run --rm app python app.py'
            }
        }
    }
}
