pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Install Python environment') {
            steps {
                script {
                    sh """
                        if [ -d "\$HOME/.pyenv" ]; then
                            echo "Python is already exists!!!"
                        else
                            echo "Installing pyenv ..."
                            curl https://pyenv.run | bash
                            export PATH="\$HOME/.pyenv/bin:\$PATH"
                            eval "\$(pyenv init --path)"
                            eval "\$(pyenv init -)"
                            pyenv install ${PYTHON_VERSION}
                            pyenv global ${PYTHON_VERSION}
                        fi
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"
                    """
                }
            }
        }

        stage("Create of Python virtual environment") {
            steps{
                script {
                    sh """
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"
                        if [ ! -d "\${VENV_DIR}" ]; then
                            echo "Create virtual environment"
                            python3 -m venv \${VENV_DIR}
                        else
                            echo "Virtual environment already exists!!!"
                        fi
                    """
                }
            }
        }

        stage("Execute test cases on the activated venv and installed dependencies.") {
            steps{
                script {
                    sh """
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"
                        . \${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest --maxfail=1 --disable-warnings -q lesson_30/Tests/test_suite_homework_30.py
                    """
                }
            }
        }

        stage('Publish results') {
            steps {
                junit '**/test-reports/*.xml'
            }
        }
    }
}