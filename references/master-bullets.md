# Master Bullet List - Ayush Mall

All available bullets from resume templates. When tailoring a resume, SELECT from this list rather than editing bullets. Only modify bullets if explicitly approved.

**Conventions:** No em dashes anywhere. Awaken AI project is mandatory in every resume. Corvic ingestion always uses the 50M+ version. Corvic evaluation framework is described by its four pillars (functionality, quality, security, performance). Keep specific orchestration/infra framework names out of bullet text; list them only in the Skills section.

---

## Corvic AI (Jun 2025 – Present)

**Title:** Machine Learning Engineer
**Company Description:** Intelligence Composition Platform turning heterogeneous enterprise data into deployable AI applications through agentic orchestration and multimodal retrieval.
**Hyperlink:** corvic.ai

### Available Bullets:

1. **Conversational Platform** ⭐ STRONGEST
   > Delivered a conversational platform in production, enabling non-technical users to build and query million-scale knowledge graphs through natural language, with vector search and multi-tool LLM agent orchestration.

2. **Multi-cloud Ingestion (50M+)** ⭐ PREFERRED (always use this version)
   > Designed and delivered an end-to-end ingestion framework integrating multi-cloud object storage (S3, Azure Blob, GCS) with incremental loads and delta management, capable of processing 50M+ files in production.

3. **LLM Evaluation (4 pillars)**
   > Established an automated evaluation framework for the platform, benchmarking agent outputs across functionality, quality, security, and performance to enable systematic quality measurement across releases.

4. **LLM Augmentation**
   > Built a scalable LLM-augmentation feature enabling million-row scale data enrichment via user prompts (e.g., identifying sustainability keywords and assigning ESG scores), unlocking diverse downstream use cases.

5. **Forecasting**
   > Forecasted customer ingestion patterns using Silverkite (multi-seasonality, holidays) to optimize resource utilization by temporal workers, resulting in an 18% reduction in compute costs.

6. **Client Demo** (strong FDE/client-facing signal)
   > Engaged with a client to demonstrate the LLM-augmentation feature, tailoring it to their data workflow, showcasing its value for their use case and driving deal conversion.

7. **ESG Scoping** (rarely used)
   > Scoped ESG compliance applications by prototyping LLM-based entity retrieval, aligning platform capabilities with high-value regulatory use cases.

---

## Shell India Markets Pvt. Ltd (Oct 2021 – Sept 2024)

**Title:** Data Engineer
**Company Description:** Shipping and Maritime: Key contributor to project centralizing emission data management and analytics using the Azure tech stack, automating reporting for compliance, and enabling sustainable decision-making through PowerBI.

### Available Bullets:

1. **Data Pipelines (with $80K)** ⭐ PREFERRED
   > Engineered and deployed data pipelines using ADF, Databricks, ADLS, and SQL to integrate 5 diverse sources, collaborating with 8 cross-functional teams to automate emission reporting, achieving 97.85% reduction in turnaround and $80,000 in annual operational savings.

   *Note: This combined bullet folds in the $80K savings. Do not also use a separate $80K bullet in the same resume (avoids double-counting).*

2. **Data Pipelines (no $80K)** (use only if pairing with a different Shell savings bullet)
   > Engineered and deployed data pipelines using ADF, Databricks, ADLS, and SQL to integrate 5 diverse sources, collaborating with 8 cross-functional teams to automate emission reporting, achieving 97.85% reduction in turnaround.

3. **DBSCAN Clustering**
   > Designed a DBSCAN-based clustering framework utilizing metrics like AER and EEOI to group voyages into efficiency tiers, enabling ranked emission-performance profiling.

4. **ADF Solution Template ($65K)**
   > Developed an ADF solution template in an individual initiative submitted to the organization's Continuous Improvement (CI) program, saving ~$65,000 annually in FTE costs from a single data solution use case.

5. **C-Suite Presentation**
   > Articulated portfolio objectives and strategic goals to a C-suite executive by presenting a business value review, securing resource allocation that supported 4 key initiatives throughout the fiscal year.

6. **KPI Scoring System**
   > Designed a KPI scoring system with Power BI and SharePoint, collaborating with 5 GMs & the SVP, saving 40 hrs quarterly for top-tier leadership by streamlining performance reporting.

7. **Knowledge Sharing Team**
   > Led Knowledge Sharing Team of the Logistics Portfolio, disseminating domain knowledge across 18 natural teams.

---

## Aegis Soft Solutions Pvt. Ltd (May 2020 – Aug 2021)

**Title:** Co-founder
**Company Description:** Co-founded a technology consulting firm delivering digitization and analytics-driven business solutions for small and mid-sized enterprises across multiple industries.

### Available Bullets:

1. **Analytics Platform**
   > Architected and deployed a unified business analytics platform integrating automation, data processing, and visualization layers to streamline operational workflows.

2. **Supply Chain Digitization**
   > Digitized key supply-chain processes in the textile domain, improving raw-to-product turnaround by 27% and enabling faster, data-driven decision-making through real-time KPI tracking.

3. **Interactive Dashboards**
   > Built and hosted interactive dashboards with ApexCharts, REST APIs, Redis, and PostgreSQL for cross-functional visibility into sales, operations, and finance performance.

4. **Client Engagements** (strong FDE/client-facing signal)
   > Led end-to-end client engagements from pitching and scoping to sub-goaling, and progress tracking, ensuring alignment with business objectives and on-time delivery of solutions.

---

## Education

Fixed on every resume version, all templates. Do not vary GPA or dates.

1. **Master's in Data Science (MSDS)** | University of Washington, Seattle | Sept 2024 -- Mar 2026
   > Coursework focused on statistical modeling, experiment design, and ML | GPA: 3.9/4.0

2. **Bachelor of Technology** | Amity University, Mumbai | Mar 2017 -- Jun 2021
   > Major: Computer Science & Engineering | Minor: Photography | GPA: 9.26/10.0

### LaTeX Formatted (Copy-Paste Ready)

```latex
\subsection{Master's in Data Science (MSDS) | University of Washington, Seattle \hfill
\textit{Sept 2024 -- Mar 2026}}
Coursework focused on statistical modeling, experiment design, and ML\ $|$\ GPA: 3.9/4.0

\subsection{Bachelor of Technology | Amity University, Mumbai \hfill
\textit{Mar 2017 -- Jun 2021}}
Major: Computer Science \& Engineering\ $|$\ Minor: Photography\ $|$\ GPA: 9.26/10.0
```

---

## Projects

Select 3 most relevant projects per resume. **Awaken AI is MANDATORY in every resume version.**

### Available Projects:

1. **Awaken AI - EEG Clinical Prognostics Pipeline** ⭐ MANDATORY (UW MSDS Capstone, Jan 2026 – Mar 2026)
   - **Shows:** Signal processing pipeline, MNE-Python, ICA, P300 ERP, PSD, ITPC, clinical/healthcare data
   - **Link:** https://github.com/ayushmall0710/awaken-ai
   > Built the first open-source, multi-paradigm EEG pipeline running oddball (P300/ERPs), language-tracking (ITPC/Morlet wavelets), and command-following (ERD + SVM classifier) on standard 19-channel ICU EEG, processing 9+ brain injury patients from raw EDF to automated HTML clinical report via a single CLI suite.

2. **FeedForward - Databricks Hackathon 1st Place** (Nov 2024)
   - **Shows:** Databricks, Spark, MLflow, Unity Catalog, ML forecasting, award, social impact
   - **Link:** https://github.com/ayushmall0710/databricks-hackathon
   > Built an end-to-end data platform on Databricks with ETL using Spark and Databricks Jobs. Developed ML forecasting models with MLflow covering 150+ countries for risk prediction, utilizing Unity Catalog for data governance and RBAC.

3. **ESG NLP** (Oct 2024 – Feb 2025)
   - **Shows:** NLP, BERT, RAG, sustainability/ESG domain
   > Conducted research on automating ESG metric quantification using NLP, integrating BERT and RAG frameworks for enhanced contextual analysis and KPI identification to improve ESG reporting transparency and efficiency.

4. **PET/MRI Reconstruction** (Jan 2025 – Apr 2025)
   - **Shows:** CNNs, diffusion models, deep learning, research, healthcare/medical AI. Use for research-leaning / CV-heavy roles.
   - **Link:** https://github.com/aaditya0106/mri-to-pet-image-synthesis
   > Conducted research to synthesize PET images from MRI scans using CNNs and diffusion-based stochastic models. Offers non-invasive, cost-effective alternatives to PET imaging for use in neurology, oncology, and precision medicine.

5. **Deepfake Detection - IEEE Published** (Published Feb 2024)
   - **Shows:** GANs, adversarial training, computer vision, publication record. Use for research-leaning / CV-heavy roles.
   - **Link:** https://ieeexplore.ieee.org/document/10486289
   > Investigated GAN-based detection methods for identifying deepfake manipulations in visual media, designing and training a discriminator-generator adversarial framework to distinguish authentic content from AI-generated forgeries. Published in IEEE Conference Proceedings (DOI: 10.1109).

6. **Orcasound / Underwater Acoustic Monitoring** (Apr 2025 – Jun 2025)
   - **Shows:** Data pipelines, eScience collaboration, marine conservation, sustainability
   - **Link:** https://github.com/orcasound
   > Collaborated with the eScience Institute to build scalable data pipelines for marine noise monitoring in the Puget Sound. Project supports marine conservation efforts and long-term ecological research through ambient sound analysis.

7. **AGTT - Automated Guitar Tablature Transcription** (Jan 2021 – Apr 2021)
   - **Shows:** CNNs, TensorFlow, audio processing, model training from scratch, end-to-end ML
   - **Link:** https://github.com/ayushmall0710/AGTT
   > Built and trained a Convolutional Neural Network from scratch to transcribe audio clips into guitar tablature, achieving 88.71% accuracy. Deployed the model end-to-end with a REST API for real-time inference.

8. **UW MSDS Alumni Employment Data Initiative** (Jan 2026 – Mar 2026)
   - **Shows:** Data governance, stakeholder management, team leadership, MS365/Power Platform automation, KPI design, data modeling. Use for consulting/data-governance/BA-flavored roles.
   - **No link** (internal SharePoint engagement, no public repo)
   > Consolidated 5 years of historical employment survey data into a unified model for the program, launching standardized intake for future collection. Built an automated SharePoint pipeline and Power BI dashboards, leading a team of 6 and partnering with the Program Director and Career Advisory team on a roadmap through 2027.

---

## Skills Sections

### ML Engineer / FDE Base (current active base)
```
Core Competencies: Machine Learning, NLP, Agentic Systems, Retrieval-Augmented Generation (RAG), LLM Evaluation & Deployment, Distributed Computing, Data Engineering, ETL, Statistical Modeling, Cloud Data Infrastructure
Languages and Frameworks: Python, SQL, protobuf, Pydantic, LangGraph, LiteLLM, Polars, PySpark, Scikit-learn, PyTorch
Platforms & Tools: Databricks (FS, Notebooks, Catalog, Jobs), Hugging Face Transformers, Temporal.io, Apache Iceberg, DuckDB, SQL Server, Docker, Git, CI/CD, Microsoft Azure (ADF, ADLS), AWS, GCP, Vertex AI, vector search, MCP
```

### NLP/Data Science Focus
```
Core Competencies: Machine Learning, NLP, Agentic Systems, Retrieval-Augmented Generation (RAG), LLM Evaluation & Deployment, Statistical Modeling, Distributed Computing, Data Engineering, ETL, Computer Vision, Cloud Data Infrastructure
Languages and Frameworks: Python, SQL, protobuf, Pydantic, LangGraph, LiteLLM, Polars, PySpark, Scikit-learn, PyTorch, TensorFlow
Platforms & Tools: Databricks (FS, Notebooks, Catalog, Jobs), Hugging Face Transformers, Temporal.io, Apache Iceberg, DuckDB, Docker, Microsoft Azure (ADF, ADLS), AWS, GCP, Vertex AI, Tableau, Git, CICD, vector search, MCP
```

### DE/Solution Architect Focus
```
Core Competencies: Data Engineering, ETL, Distributed Computing, Cloud Data Infrastructure, Machine Learning, NLP, Agentic Systems, Retrieval-Augmented Generation (RAG), LLM Evaluation & Deployment, Statistical Modeling
Languages and Frameworks: Python, SQL, protobuf, Pydantic, LangGraph, LiteLLM, PySpark, Polars, Scikit-learn, PyTorch, Object-Relational Modeling
Platforms & Tools: Databricks (FS, Notebooks, Catalog, Jobs), Apache Iceberg, Temporal.io, DuckDB, SQL Server, Docker, Microsoft Azure (ADF, ADLS), AWS, GCP, Vertex AI, Tableau, Git, CICD, RESTful Web Services
```

*Retired skills (no longer used, do not list): BAML, mQuery, QlikSense, MapReduce.*

---

## Summary Statement Variants

1. **ML Engineer / FDE (current base):**
   > ML Engineer with 4+ years of experience building and deploying production AI systems across enterprise environments. Currently developing agentic LLM applications and delivering AI infrastructure solutions at a GenAI startup.

2. **Default/DS:**
   > Data Scientist with 4+ years of experience designing data systems and driving actionable insights. Currently contributing to an agentic data platform start-up.

3. **DE Focus:**
   > Data Scientist with 4+ years of experience designing data systems, and driving actionable insight generation. Supporting GenAI-native data platform development.

4. **Enterprise Data / Governance Consulting Focus:**
   > 4+ years of experience engineering enterprise data solutions and partnering with cross-functional stakeholders to drive data-informed decision-making. Currently developing agentic AI infrastructure at a GenAI startup.

*Note: Summary no longer references "pursuing an MS" since the degree is complete (graduated March 2026).*

---

## Quick Reference: Metrics

| Source | Metric | Context |
|--------|--------|---------|
| Corvic | 50M+ files | Ingestion framework scale |
| Corvic | million-scale | Knowledge graph query scale |
| Corvic | 18% reduction | Compute cost savings from forecasting |
| Corvic | 1M+ rows | LLM augmentation scale |
| Shell | 97.85% reduction | Reporting turnaround time |
| Shell | $80,000/year | Operational cost savings (folded into pipeline bullet) |
| Shell | $65,000/year | CI program FTE savings |
| Shell | 8 teams | Cross-functional collaboration |
| Shell | 18 teams | Knowledge sharing reach |
| Shell | 5 sources | Data integration scope |
| Aegis | 27% improvement | Supply chain turnaround |
| FeedForward | 150+ countries | Dataset coverage (not "serving") |
| AGTT | 88.71% accuracy | Tablature transcription |

---

## LaTeX Formatted Bullets (Copy-Paste Ready)

### Corvic AI Bullets

```latex
% 1. Conversational Platform (STRONGEST)
\item \textbf{Delivered a conversational platform in production}, enabling non-technical users to build and query \textbf{million-scale knowledge graphs} through natural language, with vector search and multi-tool LLM agent orchestration.

% 2. Multi-cloud Ingestion (50M+) - PREFERRED
\item \textbf{Designed and delivered an end-to-end ingestion framework} integrating multi-cloud object storage (S3, Azure Blob, GCS) with incremental loads and delta management, \textbf{capable of processing 50M+} files in production.

% 3. LLM Evaluation (4 pillars)
\item \textbf{Established an automated evaluation framework} for the platform, benchmarking agent outputs across \textbf{functionality, quality, security, and performance} to enable systematic quality measurement across releases.

% 4. LLM Augmentation
\item \textbf{Built a scalable LLM-augmentation feature} enabling million-row scale data enrichment via user prompts (e.g., identifying sustainability keywords and assigning ESG scores), unlocking diverse downstream use cases.

% 5. Forecasting
\item \textbf{Forecasted customer ingestion patterns} using \textbf{Silverkite} (multi-seasonality, holidays) to optimize resource utilization by temporal workers, resulting in an \textbf{18\% reduction} in compute costs.

% 6. Client Demo
\item \textbf{Engaged with a client to demonstrate the LLM-augmentation feature}, tailoring it to their data workflow, showcasing its value for their use case and driving deal conversion.

% 7. ESG Scoping (rarely used)
\item \textbf{Scoped ESG compliance applications} by prototyping LLM-based entity retrieval, aligning platform capabilities with high-value regulatory use cases.
```

### Shell Bullets

```latex
% 1. Data Pipelines (with $80K) - PREFERRED
\item \textbf{Engineered and deployed data pipelines} using ADF, Databricks, ADLS, and SQL to integrate 5 diverse sources, collaborating with 8 cross-functional teams to automate emission reporting, achieving \textbf{97.85\% reduction} in turnaround and \textbf{\$80,000} in annual operational savings.

% 2. Data Pipelines (no $80K)
\item \textbf{Engineered and deployed data pipelines} using ADF, Databricks, ADLS, and SQL to integrate 5 diverse sources, collaborating with 8 cross-functional teams to automate emission reporting, achieving \textbf{97.85\% reduction} in turnaround.

% 3. DBSCAN Clustering
\item \textbf{Designed a DBSCAN-based clustering framework} utilizing metrics like AER and EEOI to group voyages into efficiency tiers, enabling ranked emission-performance profiling.

% 4. ADF Solution Template ($65K)
\item \textbf{Developed an ADF solution template} in an individual initiative submitted to the organization's Continuous Improvement (CI) program, saving \textbf{$\sim$\$65,000 annually} in FTE costs from a single data solution use case.

% 5. C-Suite Presentation
\item \textbf{Articulated portfolio objectives and strategic goals} to a C-suite executive by presenting a business value review, securing resource allocation that \textbf{supported 4 key initiatives} throughout the fiscal year.

% 6. KPI Scoring System
\item \textbf{Designed a KPI scoring system} with Power BI and SharePoint, collaborating with 5 GMs \& the SVP, saving \textbf{40 hrs quarterly for top-tier leadership} by streamlining performance reporting.

% 7. Knowledge Sharing Team
\item \textbf{Led Knowledge Sharing Team} of the Logistics Portfolio, disseminating domain knowledge across 18 natural teams.
```

### Aegis Bullets

```latex
% 1. Analytics Platform
\item \textbf{Architected and deployed a unified business analytics platform} integrating automation, data processing, and visualization layers to streamline operational workflows.

% 2. Supply Chain Digitization
\item \textbf{Digitized key supply-chain processes} in the textile domain, \textbf{improving raw-to-product turnaround by 27\%} and enabling faster, data-driven decision-making through real-time KPI tracking.

% 3. Interactive Dashboards
\item \textbf{Built and hosted interactive dashboards} with ApexCharts, REST APIs, Redis, and PostgreSQL for cross-functional visibility into sales, operations, and finance performance.

% 4. Client Engagements
\item \textbf{Led end-to-end client engagements} from pitching and scoping to sub-goaling, and progress tracking, ensuring alignment with business objectives and on-time delivery of solutions.
```

### Projects (LaTeX Formatted)

```latex
% MANDATORY: Awaken AI
\subsection{Awaken AI -- EEG Clinical Prognostics Pipeline (UW MSDS Capstone)%
\href{https://github.com/ayushmall0710/awaken-ai}{~\faExternalLink*} \hfill \textit{Jan 2026 -- Mar 2026}}
Built the first open-source, multi-paradigm EEG pipeline running oddball (P300/ERPs), language-tracking (ITPC/Morlet wavelets), and command-following (ERD + SVM classifier) on standard 19-channel ICU EEG, processing 9+ brain injury patients from raw EDF to automated HTML clinical report via a single CLI suite.

% FeedForward (Databricks Hackathon)
\subsection{FeedForward: Global Malnutrition Monitoring (Databricks$\times$UW Hackathon, 1st Place)%
\href{https://github.com/ayushmall0710/databricks-hackathon}{~\faExternalLink*} \hfill \textit{Nov 2024}}
Built an end-to-end data platform on Databricks with ETL using Spark and Databricks Jobs. Developed ML forecasting models with MLflow covering 150+ countries for risk prediction, utilizing Unity Catalog for data governance and RBAC.

% ESG NLP
\subsection{Environmental, Social, and Governance (ESG) Metric Quantification Using NLP \hfill \textit{Oct 2024 -- Feb 2025}}
Conducted research on automating ESG metric quantification using NLP, integrating BERT and RAG frameworks for enhanced contextual analysis and KPI identification to improve ESG reporting transparency and efficiency.

% PET/MRI Reconstruction (research/CV-heavy roles)
\subsection{PET Reconstruction from MRI Using CNN and Diffusion Frameworks%
\href{https://github.com/aaditya0106/mri-to-pet-image-synthesis}{~\faExternalLink*} \hfill \textit{Jan 2025 -- Apr 2025}}
Conducted research to synthesize PET images from MRI scans using CNNs and diffusion-based stochastic models. Offers non-invasive, cost-effective alternatives to PET imaging for use in neurology, oncology, and precision medicine.

% Deepfake Detection (research/CV-heavy roles)
\subsection{Deepfake Face Swapping Detection Using Generative Adversarial Networks%
\href{https://ieeexplore.ieee.org/document/10486289}{~\faExternalLink*} \hfill \textit{Published Feb 2024}}
Investigated GAN-based detection methods for identifying deepfake manipulations in visual media, designing and training a discriminator-generator adversarial framework to distinguish authentic content from AI-generated forgeries. Published in IEEE Conference Proceedings (DOI: 10.1109).

% Orcasound
\subsection{Underwater Acoustic Monitoring for Marine Conservation (Orcasound Project)%
\href{https://github.com/orcasound}{~\faExternalLink*} \hfill \textit{Apr 2025 -- Jun 2025}}
Collaborated with the eScience Institute to build scalable data pipelines for marine noise monitoring in the Puget Sound. Project supports marine conservation efforts and long-term ecological research through ambient sound analysis.

% AGTT
\subsection{Automated Guitar Tablature Transcription (AGTT)%
\href{https://github.com/ayushmall0710/AGTT}{~\faExternalLink*} \hfill \textit{Jan 2021 -- Apr 2021}}
Built and trained a Convolutional Neural Network from scratch to transcribe audio clips into guitar tablature, achieving 88.71\% accuracy. Deployed the model end-to-end with a REST API for real-time inference.

% UW MSDS Alumni Employment Data Initiative (no link)
\subsection{UW MSDS Alumni Employment Data Initiative \hfill \textit{Jan 2026 -- Mar 2026}}
Consolidated 5 years of historical employment survey data into a unified model for the program, launching standardized intake for future collection. Built an automated SharePoint pipeline and Power BI dashboards, leading a team of 6 and partnering with the Program Director and Career Advisory team on a roadmap through 2027.
```
