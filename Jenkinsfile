pipeline{

    agent{
        label "jenkins-agent"
    }
    environment{
        DOCKER_USER="mado445555"
        DOCKER_PASS="dockerhub"
        RELEASE_GEN="1.0.0"
        RELEASE_ECHO="1.0.0"
        ECHO_IMAGE="${DOCKER_USER}+"/"+"pr3echojenkins""
        GEN_IMAGE="${DOCKER_USER}+"/"+"pr3genjenkins""

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
                
                    git branch: "main", credentialsId: "git-pr3-token" , url: "https://github.com/Mado445/pr3images"
            }

        }
        
        stage("Sonar analysis"){
            steps{
                script{
                    
                    def scannerHome = tool 'sonar-scanner'
                    echo "Scanner home = ${scannerHome}"
                    withSonarQubeEnv(credentialsId: "jenkiins-sonarqube-token"){
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=pr3 -Dsonar.sources=."
                    }
                }
            }

        }

        stage ("Sonar Quality report "){
            steps{
                script{
                    waitForQualityGate abortPipline: false, credentialsId: 'jenkiins-sonarqube-token'
                }
            }
        }

        stage("docker create+push image"){
            steps{
                script{
                    docker.withRegistry('',DOCKER_PASS){
                        DOCKER_IMAGE_ECHO=docker.build("${ECHO_IMAGE}","./pr3echo")
                        DOCKER_IMAGE_GEN=docker.build("${GEN_IMAGE}","./pr3gen")
                    }
                    docker.withRegistry('',DOCKER_PASS){
                        DOCKER_IMAGE_ECHO.push("${RELEASE_ECHO}")
                        DOCKER_IMAGE_ECHO.push('latest')

                        DOCKER_IMAGE_GEN.push("${RELEASE_GEN}")
                        DOCKER_IMAGE_GEN.push('latest')
                    }

                }

            }

        }



    }




















}