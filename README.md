# CI/CD Pipeline Visualization

```mermaid
graph TD
   %% Define Styles
   classDef lint fill:#f9f,stroke:#333,stroke-width:2px;
   classDef sec fill:#ffcccc,stroke:#333,stroke-width:2px;
   classDef build fill:#cce5ff,stroke:#333,stroke-width:2px;
   classDef deploy fill:#ccffcc,stroke:#333,stroke-width:2px;
   classDef notify fill:#e0e0e0,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;

   Start((Start)) --> Checkout[1. Checkout Code]
  
   subgraph "Phase 1: Code Quality & Setup"
       Checkout --> PySetup[2. Setup Python & Ruff]
       PySetup --> JavaSetup[3. Setup Java 11]
       JavaSetup --> MavenLint[4. Maven Checkstyle]
   end

   subgraph "Phase 2: Security Checks (SAST/SCA)"
       MavenLint --> CodeQL[5. CodeQL Analysis]
       CodeQL --> OWASP[6. OWASP Dependency Check]
   end

   subgraph "Phase 3: Build & Test"
       OWASP --> UnitTest[7. Unit Tests]
       UnitTest --> JavaBuild[8. Build JAR]
       JavaBuild --> DockerSetup[9. Setup Docker Buildx]
       DockerSetup --> DockerLogin[Login to DockerHub]
       DockerLogin --> DockerBuild[Build Docker Image]
   end

   subgraph "Phase 4: Container Security"
       DockerBuild --> TrivyScan[10. Trivy Vulnerability Scan]
       TrivyScan --> UploadSarif[Upload Security Results]
   end

   subgraph "Phase 5: Release"
       UploadSarif --> PushImage[11. Push to DockerHub]
   end
  
   PushImage --> Notify[12. Notify Slack/Chat]
  
   %% Error Handling Path
   TrivyScan -.->|Fail?| Notify
   DockerBuild -.->|Fail?| Notify
  
   class PySetup,JavaSetup,MavenLint lint;
   class CodeQL,OWASP,TrivyScan sec;
   class JavaBuild,DockerBuild,DockerLogin build;
   class PushImage deploy;
   class Notify notify;
