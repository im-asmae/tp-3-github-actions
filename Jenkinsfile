pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello depuis un pipeline déclaratif'
            }
        }

        stage('Infos environnement') {
            steps {
                echo "Nom du noeud Jenkins: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }

        stage('Install requirements') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Run des tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest
                    python -m pytest -v --cov=app --cov-report=term-missing --cov-fail-under=98
                '''
            }
        }
    }

    post {
        always {
            bat 'if exist venv rmdir /s /q venv'
        }
    }
}