pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // keep your working credential id
                git branch: 'main',
                    credentialsId: '20d31f06-5f46-47df-a097-5540f2ffb48d',
                    url: 'https://github.com/jas09/Python_Selenium.git'
            }
        }

        stage('Setup') {
            steps {
                // ensure pip installs into the same python used by Jenkins agent
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                //python -m pip install pytest allure-pytest
            }
        }

        stage('Build & Test') {
            steps {
                dir('D:\\Projects\\Python_Selenium'){
                // Write Allure *results* to allure-results (not allure-report)
                //pytest -n 2 smoke --browser_name Firefox --html=reports/report.html
                //bat 'pytest -n 2 --url_key=MOBILE_SHOP --alluredir=allure-results'
                //bat 'python -m pytest -n 2 tests/test_sortingTables.py --url_key=GREENKART --alluredir=allure-results'
                bat 'python -m pytest tests/test_sortingTables.py --url_key=GREENKART --browser_name=chrome --alluredir=allure-results'
                //bat 'python -m pytest --alluredir=allure-results'
            }
        }

        stage('Debug: show Allure result files') {
            steps {
                // Quick check what exists
                bat 'echo Workspace: %cd%'
                bat 'if exist allure-results ( echo "allure-results FOUND" & dir /b /s allure-results ) else ( echo "NO allure-results folder" )'
                bat 'if exist allure-report ( echo "allure-report FOUND" & dir /b /s allure-report ) else ( echo "NO allure-report folder" )'
            }
        }

        stage('Generate Allure HTML (optional)') {
            steps {
                // Optional explicit generation - plugin can also generate automatically
                // If Allure CLI tool is installed as a tool in Jenkins, plugin might call it; otherwise specify full path.
                // This will fail if allure-results is missing, but we already debugged above.
                bat '%JENKINS_HOME%\\tools\\ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation\\Allure-2.34.1\\bin\\allure.bat generate allure-results -o allure-report --clean || echo "allure generate failed or no results"'
            }
        }

    } // stages

    post {
        always {
            // Publish via Allure plugin (must be installed)
            allure results: [[path: 'allure-results']]

            // Fallback: publish generated HTML if it exists
            publishHTML (target: [
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure HTML Report',
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
    }
}
