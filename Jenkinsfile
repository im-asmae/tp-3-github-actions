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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Run des tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                    python -m pytest -v --cov=app --cov-report=term-missing --cov-fail-under=98
                '''
            }
        }
    }

    post {
        always {
            // Nettoie l'environnement virtuel à la fin du build
            sh 'rm -rf venv'
        }
    }
}

