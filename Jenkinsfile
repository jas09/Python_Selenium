pipeline {
    agent any

    environment {
        JIRA_SITE = 'azharullamohammed2.atlassian.net'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/jas09/Python_Selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {

                bat '''
                python -m pytest ^
                -n 3 ^
                --headless ^
                --alluredir=allure-results ^
                --json-report ^
                --json-report-file=report.json ^
                -v
                '''
            }
        }

        stage('Read Test Metrics') {
            steps {
                script {

                    if (fileExists('report.json')) {

                        def report = readJSON file: 'report.json'

                        env.TOTAL_TESTS  = "${report.summary.total ?: 0}"
                        env.PASSED_TESTS = "${report.summary.passed ?: 0}"
                        env.FAILED_TESTS = "${report.summary.failed ?: 0}"
                        env.SKIPPED_TESTS = "${report.summary.skipped ?: 0}"

                        echo """
=========================
TEST EXECUTION SUMMARY
=========================
Total   : ${env.TOTAL_TESTS}
Passed  : ${env.PASSED_TESTS}
Failed  : ${env.FAILED_TESTS}
Skipped : ${env.SKIPPED_TESTS}
=========================
"""
                    }
                }
            }
        }
    }

    post {
        always {
            allure([
                results: [[path: 'allure-results']]
            ])

            archiveArtifacts(
                artifacts: 'allure-results/**/*',
                allowEmptyArchive: true
            )

            echo """
====================================
BUILD SUMMARY
====================================
Total Tests : ${env.TOTAL_TESTS}
Passed      : ${env.PASSED_TESTS}
Failed      : ${env.FAILED_TESTS}
Skipped     : ${env.SKIPPED_TESTS}
====================================

Jenkins:
${env.BUILD_URL}

Allure:
${env.BUILD_URL}allure
"""
        }

        success {
    script {

        def jiraComment = """
Build #${env.BUILD_NUMBER} Completed Successfully

Passed : ${env.PASSED_TESTS}
Failed : ${env.FAILED_TESTS}
Skipped : ${env.SKIPPED_TESTS}
Total   : ${env.TOTAL_TESTS}

Jenkins:
${env.BUILD_URL}

Allure:
${env.BUILD_URL}allure
"""

        withCredentials([
            usernamePassword(
                credentialsId: 'jira-api-creds',
                usernameVariable: 'JIRA_USER',
                passwordVariable: 'JIRA_TOKEN'
            )
        ]) {

            echo "JIRA_SITE = ${JIRA_SITE}"
            echo "JIRA_ISSUE = ${env.JIRA_ISSUE}"

            powershell """

            \$pair = "\$env:JIRA_USER:\$env:JIRA_TOKEN"
            \$bytes = [System.Text.Encoding]::UTF8.GetBytes(\$pair)
            \$base64 = [System.Convert]::ToBase64String(\$bytes)

            \$headers = @{
                Authorization = "Basic \$base64"
                Accept = "application/json"
                "Content-Type" = "application/json"
            }

            Write-Host "=========================================="
            Write-Host "DEBUG START"
            Write-Host "=========================================="

            Write-Host "JIRA_SITE:"
            Write-Host "${JIRA_SITE}"

            Write-Host "JIRA_ISSUE:"
            Write-Host "${env.JIRA_ISSUE}"

            Write-Host "TARGET URL:"
            Write-Host "https://${JIRA_SITE}/rest/api/3/issue/${env.JIRA_ISSUE}/comment"

            \$body = @{
                body = @{
                    type = "doc"
                    version = 1
                    content = @(
                        @{
                            type = "paragraph"
                            content = @(
                                @{
                                    type = "text"
                                    text = @'
${jiraComment}
'@
                                }
                            )
                        }
                    )
                }
            } | ConvertTo-Json -Depth 20

            Write-Host "REQUEST BODY:"
            Write-Host \$body

            Write-Host "=========================================="
            Write-Host "DEBUG END"
            Write-Host "=========================================="

            Invoke-RestMethod `
                -Uri "https://${JIRA_SITE}/rest/api/3/issue/${env.JIRA_ISSUE}/comment" `
                -Method POST `
                -Headers \$headers `
                -Body \$body

            """
        }
    }
}
    }
}