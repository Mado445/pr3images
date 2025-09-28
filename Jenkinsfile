pipeline{

    agent{
        label "jenkins-agent"
    }

    tools{

    }

    stages{

        stage("Clean workspace as a fresh"){
            steps{
                script{
                    cleanWs()
                }
            }
        }

        stage("checkout for SCM"){
            steps{
                script(
                    git branch: "main", credentialsId: "git-pr3-token" , url: "https://github.com/Mado445/pr3images"
                )
            }

        }
        
        stage("Sonar analysis"){
            steps{
                script{
                    withSonarWubeEnv(credentialsId: "jenkiins-sonarqube-token"){
                        sh "sonar-scanner -Dsonar.projectKey=pr3 -Dsonar.sources=."
                    }
                }
            }

        }

        stage ("Sonar Quality report "){
            steps{
                script{
                    waitForQualityGate abortPipiline: false, credentialsId: 'jenkiins-sonarqube-token'
                }
            }
        }





    }




















}