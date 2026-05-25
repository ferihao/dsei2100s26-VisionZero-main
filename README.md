# Project Peer and Self Evaluation Form
**DSE I2100-2ST: Applied Machine Learning and Data Mining — Spring 2026**
**Due: Tuesday, May 26, 2026, midnight**

---

## How to Complete This Form

**Fill out every section directly in this document.** Type your answers where indicated. When you are done, submit the completed file as a Brightspace Assignment (file upload or paste into the text box — either is accepted).

**Keep your GitHub repository open the entire time you fill this out.** Every rating you give must be grounded in specific, verifiable evidence from the repository. Vague impressions are not sufficient. Before assigning a score, locate a commit hash, PR number, or Issue number that supports it.

**Be calibrated, not generous.** The purpose of this evaluation is to give the instructor an accurate picture of each person's contribution — including your own. Inflated ratings that are not supported by GitHub evidence will be detected and will reflect poorly on your judgment, not just your honesty. Ask yourself: *"If an outside observer — someone who has never met any of us — looked at the GitHub repository and read this evaluation, would they find my ratings credible?"* That is the standard.

**Rating scale used throughout this form:**

| Score | Label | What it means |
|-------|-------|----------------|
| 5 | Much more than expected | Consistently exceeded what was asked; drove outcomes, unblocked others, materially raised the project's quality |
| 4 | Somewhat more than expected | Regularly went beyond the minimum; volunteered for harder tasks; proactively identified and solved problems |
| 3 | As expected — the neutral baseline | Completed assigned work at expected quality and on time; communicated reliably; held their weight |
| 2 | Somewhat less than expected | Delivered less than assigned or at lower quality; required significant prompting; inconsistent communication |
| 1 | Much less than expected | Failed to complete key tasks; was unreachable for extended periods; output was absent or unusable |

> **3 is not a bad score.** It means the person did what was expected. It is the correct score for a solid, reliable contributor. Reserve 4 and 5 for contributions that genuinely went beyond what was required. Reserve 1 and 2 for genuine shortfalls. A form where everyone receives 5/5/5/5/5 will be treated as an uncalibrated submission.

**Confidentiality:** Your individual ratings are visible only to the instructor. They will never be shared with your teammates in any identified form.

**Penalty:** Failure to submit by the deadline results in a **5-point deduction** from your individual project grade.

---

## Section 1: Your Identity and Role

**Your full name:** *Feriha Ozturk*

**Your GitHub username:** *ferihao*

**Your team name / number:** *dsei2100s26-VisionZero*

**Your declared primary role** — mark one with an X:

- [ ] **Infrastructure / DevOps** — Repository setup, data pipeline, environment reproducibility
- [ X] **Experimentation** — Model training, hyperparameter tuning, algorithm comparison, evaluation
- [ ] **Documentation / Analysis** — Report writing, literature review, visualizations, error analysis, notebook narration
- [ X] **Data Engineering** — Data preprocessing, feature engineering, validation splits, data quality checks

*Your role is used to contextualize ratings. A documentation contributor is not penalized for fewer code commits; an experimentation contributor is not penalized for fewer Wiki entries. Rate yourself and teammates relative to their declared role.*

---

## Section 2: Team Member Ratings

This section has **four member blocks** — one for yourself and one for each teammate. Your team has at most 4 members.

- **If your team has 4 members:** complete all four blocks (Member A = you; Members B, C, D = teammates).
- **If your team has 3 members:** complete blocks A, B, C. **Delete block D entirely before submitting.**
- **If your team has 2 members:** complete blocks A and B. **Delete blocks C and D entirely before submitting.**

Each block uses the same five dimensions. The anchor descriptions are repeated in each block for convenience.

---

### Member A — SELF-RATING

*Rate yourself honestly. Self-ratings are never shared with your teammates. They are used by the instructor for calibration — to detect overconfidence or underconfidence patterns — and may inform an individual meeting.*

**Full name:** *Feriha Ozturk*
**GitHub username:** *ferihao*
**Declared role:** *Experimentation and Data Engineering*

---

#### A1 — Contributing to the Team's Work

*Did you complete your fair share of tasks at acceptable quality and on time?*

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took on more than your share; delivered high-quality work ahead of schedule; your contributions materially shaped the final product |
| 4 | Regularly completed assigned work with above-average quality; occasionally volunteered for tasks beyond your scope |
| 3 | Completed your assigned tasks at expected quality and on time; held your weight |
| 2 | Sometimes missed deadlines or delivered incomplete work; needed reminders to finish tasks |
| 1 | Failed to complete assigned tasks; your absence required teammates to absorb your work |

**Your rating (1–5):** *4*

**GitHub evidence** — cite 1–2 specific artifacts (commit hash, PR number, or Issue number) that support this rating:
*I maintained the highest commit volume on the team spanning from March through May 25. I implemented an SVM model (commit 83cf998), as well as multiple iterations of XGBoost (commits af4fd6d and f25be93) on May 11. Additionally, I delivered an XGBoost interpretability and fairness analysis on May 19 (commit 956e816), taking on modeling tasks that went significantly beyond my declared Data Engineering role.*

---

#### A2 — Interacting with Teammates

*Did you communicate reliably and constructively throughout the project?*

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Communicated proactively at all times; always responded quickly; your communication style made the team more effective |
| 4 | Responded reliably to messages; attended meetings; gave and received feedback constructively |
| 3 | Communicated at a reasonable pace; attended most meetings; engaged constructively when addressed |
| 2 | Sometimes slow to respond; occasionally missed meetings without notice; communication was passive or inconsistent |
| 1 | Was largely unreachable; missed multiple meetings without explanation; caused coordination failures |

**Your rating (1–5):** *4*

**GitHub evidence** — meeting transcript commit, issue comment thread, PR review, or note "coordination happened off-platform" with a brief description:
*I communicated and coordinated with the team off-platform via Discord. I remained consistently engaged throughout the entire project, staying active right up to the submission deadline, as demonstrated by my final README update on May 25 (commit 457bcb6).*

---

#### A3 — Keeping the Team on Track

*Did you help the team stay organized and meet its deadlines?*

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took a leadership role in planning; drove meeting agendas; tracked open issues proactively; anticipated blockers before they became problems |
| 4 | Helped plan work; updated GitHub Issues and the Project Board regularly; flagged blockers promptly |
| 3 | Updated your own assigned issues; attended planning discussions; met your self-imposed deadlines |
| 2 | Rarely updated GitHub Issues; missed internal deadlines; needed reminders to track your own work |
| 1 | Did not contribute to planning; left issues stale; your disorganization slowed the team |

**Your rating (1–5):** *4*

**GitHub evidence** — Issue link, Project Board activity, or Wiki meeting note:
*We usually talked over the Discord and made sure that everyone was on the track. I wrote some meeting notes on Wiki: https://github.com/DataScienceAndEngineering/dsei2100s26-VisionZero/wiki*

---

#### A4 — Expecting Quality

*Did you hold yourself and your teammates to high standards?*

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Proactively identified quality problems; gave substantive code reviews; raised concerns about correctness or rigor without being asked |
| 4 | Gave substantive PR reviews with specific feedback; flagged potential data leakage or evaluation errors |
| 3 | Reviewed PRs when asked; verified your own code worked before submitting; asked questions when something seemed wrong |
| 2 | Rubber-stamped PRs without reading them; submitted code without testing; overlooked problems others had to catch |
| 1 | Did not review others' work; submitted broken or untested code; showed no concern for project quality |

**Your rating (1–5):** *4*

**GitHub evidence** — PR review link or Issue comment identifying a quality concern:
*I focused on iterative refinement rather than single-pass submissions, actively improving the XGBoost model through versions 2 and 3 on May 11 (commits af4fd6d and f25be93). My XGBoost interpretability and fairness analysis on May 19 (commit 956e816) demonstrates a high quality standard that evaluates the model beyond just accuracy numbers.*

---

#### A5 — Knowledge, Skills, and Abilities (KSAs)

*Did you apply technical skills relevant to your declared role?*

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Brought specialized skills that solved problems the team could not have solved otherwise; taught others; elevated the project's technical quality |
| 4 | Applied course skills (scikit-learn pipelines, evaluation metrics, feature engineering, reproducibility practices) with confidence and accuracy |
| 3 | Applied the required ML/data science skills adequately for your role; learned what was needed when gaps appeared |
| 2 | Had consistent gaps in skills relevant to your role; required significant help from teammates on core tasks |
| 1 | Was unable to perform the technical tasks your role required; contributed little in your area |

**Your rating (1–5):** *5*

**GitHub evidence** — commit, notebook, or PR demonstrating technical contribution:
*While my official role was Data Engineering, I autonomously implemented multiple ML algorithm families, iterated on hyperparameters, and produced a full SHAP-based interpretability analysis with a fairness evaluation. These specific tasks included the SVM model on May 11 (commit 83cf998), XGBoost v3 on May 11 (commit f25be93), and the XGBoost interpretability analysis on May 19 (commit 956e816). These contributions provided specialized technical skills the team needed to succeed.*

---

#### A — Open-Ended Self-Reflection

**Describe the single most impactful contribution you made to the project. Be specific — name a commit, PR, notebook, or decision:**
*My standout artifact is adding interpretability for the XGBoost model alongside a fairness analysis on May 19 (commit 956e816). Integrating fairness evaluation pushed the work substantially beyond the core expectations of the Data Engineering role and stands out as one of my strongest technical deliverables in the project*

**Describe one thing you would do differently if the project started over:**
*I would improve the clarity of my commit hygiene. For example, on May 5, I used a single period as a commit message, which briefly made it difficult to track what was being changed. Clearer messaging throughout would make an already strong contribution record much easier for an outside evaluator to verify.*

---

---

### Member B — TEAMMATE RATING

*Rate this teammate as an outside observer would — based on what is visible in the repository, not on friendship or general impressions.*

**Teammate full name:** *Qazim Pali*
**Teammate GitHub username:** *XimiPali*
**Teammate's declared role:** *Infrastructure / DevOps*

*Evaluate this teammate relative to their declared role before assigning KSA scores.*

---

#### B1 — Contributing to the Team's Work

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took on more than their share; delivered high-quality work ahead of schedule; their contributions materially shaped the final product |
| 4 | Regularly completed assigned work with above-average quality; occasionally volunteered for tasks beyond their scope |
| 3 | Completed their assigned tasks at expected quality and on time; held their weight |
| 2 | Sometimes missed deadlines or delivered incomplete work; needed reminders to finish tasks |
| 1 | Failed to complete assigned tasks; their absence required teammates to absorb their work |

**Rating (1–5):** *4*

**GitHub evidence** — cite 1–2 specific artifacts:
*Qazim handled the foundational repository setup using the Cookiecutter framework on March 16 (commit b4045f1). He also contributed heavily to the modeling side by adding interpretability, fairness analysis, and a limitations discussion to our Logistic Regression baseline on May 18 (commit d2eb6efd).*

---

#### B2 — Interacting with Teammates

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Communicated proactively at all times; always responded quickly; their style made the team more effective |
| 4 | Responded reliably to messages; attended meetings; gave and received feedback constructively |
| 3 | Communicated at a reasonable pace; attended most meetings; engaged constructively when addressed |
| 2 | Sometimes slow to respond; occasionally missed meetings without notice; communication was passive or inconsistent |
| 1 | Was largely unreachable; missed multiple meetings without explanation; caused coordination failures |

**Rating (1–5):** *4*

**GitHub evidence:**
*Our primary communication was off-platform via Discord. Qazim was highly active during our planning phases and maintained a consistent commit history parallel to the rest of the team, ensuring there were never any coordination bottlenecks.*

---

#### B3 — Keeping the Team on Track

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took a leadership role in planning; drove meeting agendas; tracked open issues proactively; anticipated blockers |
| 4 | Helped plan work; updated GitHub Issues and the Project Board regularly; flagged blockers promptly |
| 3 | Updated their own assigned issues; attended planning discussions; met their self-imposed deadlines |
| 2 | Rarely updated GitHub Issues; missed internal deadlines; needed reminders to track their own work |
| 1 | Did not contribute to planning; left issues stale; their disorganization slowed the team |

**Rating (1–5):** *3*

**GitHub evidence:**
*His prompt repository initialization (commit b4045f1) allowed the whole team to start working immediately. Similarly, his work on cleaning the dataset by April 24 (commit 3f48adc) was the critical step that cleared the way for all downstream modeling tasks.*

---

#### B4 — Expecting Quality

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Proactively identified quality problems; gave substantive code reviews; raised concerns without being asked |
| 4 | Gave substantive PR reviews with specific feedback; flagged potential data leakage or evaluation errors |
| 3 | Reviewed PRs when asked; verified their code worked before submitting; asked questions when something seemed wrong |
| 2 | Rubber-stamped PRs; submitted code without testing; overlooked problems others had to catch |
| 1 | Did not review others' work; submitted broken or untested code; showed no concern for quality |

**Rating (1–5):** *4*

**GitHub evidence:**
*Qazim demonstrated a strong commitment to quality, particularly by ensuring our Logistic Regression model included thorough interpretability and fairness evaluations rather than just outputting basic predictive results (commit d2eb6efd).*

---

#### B5 — Knowledge, Skills, and Abilities (KSAs)

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Brought specialized skills that solved problems the team could not have solved otherwise; taught others |
| 4 | Applied course skills with confidence and accuracy relative to their declared role |
| 3 | Applied required skills adequately for their role; learned what was needed when gaps appeared |
| 2 | Had consistent skill gaps in their role area; required significant help from teammates |
| 1 | Was unable to perform technical tasks their role required; contributed little in their area |

**Rating (1–5):** *4*

**GitHub evidence:**
*He successfully applied skills across the entire project pipeline. He cleaned our dataset (commit 3f48adc) and built our baseline Logistic Regression model (commit 013d87f), proving his technical capability spanned from EDA and scaffolding to fairness analysis.*

---

#### B — Open-Ended Reflection

**Describe one specific contribution this teammate made that had a clear, positive impact on the project (name the artifact):**
*Qazim’s Exploratory Data Analysis (EDA) laid the foundation for our modeling by identifying key crash patterns and injury distributions, which directly informed our Random Forest feature selection. Additionally, he established and managed our GitHub repository. His robust version control and structured codebase ensured seamless team collaboration and streamlined the entire project lifecycle.*

**If applicable, describe one area where their contribution fell short of what was needed. Skip this if it genuinely does not apply — do not invent criticism, but do not omit real gaps out of politeness:**
*(type here)*

---

---

### Member C — TEAMMATE RATING

*If your team has only 2 members, delete this entire block before submitting.*

**Teammate full name:** *Tahir Zogaj*
**Teammate GitHub username:** *TahirZogaj*
**Teammate's declared role:** *Documentation / Analysis*

---

#### C1 — Contributing to the Team's Work

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took on more than their share; delivered high-quality work ahead of schedule; their contributions materially shaped the final product |
| 4 | Regularly completed assigned work with above-average quality; occasionally volunteered for tasks beyond their scope |
| 3 | Completed their assigned tasks at expected quality and on time; held their weight |
| 2 | Sometimes missed deadlines or delivered incomplete work; needed reminders to finish tasks |
| 1 | Failed to complete assigned tasks; their absence required teammates to absorb their work |

**Rating (1–5):** *4*

**GitHub evidence:**
*Tahir delivered highly substantive analytical work, specifically the refined Random Forest notebook on May 5 (commit b6c1d57) and the comprehensive RF SHAP Ablation analysis on May 19 (commit 018ae74). His technical depth, combined with our ongoing off-platform code reviews, really strengthened the project's overall narrative.*

---

#### C2 — Interacting with Teammates

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Communicated proactively at all times; always responded quickly; their style made the team more effective |
| 4 | Responded reliably to messages; attended meetings; gave and received feedback constructively |
| 3 | Communicated at a reasonable pace; attended most meetings; engaged constructively when addressed |
| 2 | Sometimes slow to respond; occasionally missed meetings without notice; passive or inconsistent |
| 1 | Was largely unreachable; missed multiple meetings without explanation; caused coordination failures |

**Rating (1–5):** *3*

**GitHub evidence:**
*While we coordinated primarily on Discord, Tahir showed proactive communication and team leadership by organizing and proposing our final role distribution structure on May 25.*

---

#### C3 — Keeping the Team on Track

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Took a leadership role in planning; drove meeting agendas; tracked open issues proactively; anticipated blockers |
| 4 | Helped plan work; updated GitHub Issues and the Project Board regularly; flagged blockers promptly |
| 3 | Updated their own assigned issues; attended planning discussions; met their self-imposed deadlines |
| 2 | Rarely updated GitHub Issues; missed internal deadlines; needed reminders to track their own work |
| 1 | Did not contribute to planning; left issues stale; their disorganization slowed the team |

**Rating (1–5):** *4*

**GitHub evidence:**
*Tahir took the initiative to organize our team structure on Discord and successfully delivered his key notebooks right on schedule during our final sprint, particularly the RF SHAP ablation on May 19 (commit 018ae74).*

---

#### C4 — Expecting Quality

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Proactively identified quality problems; gave substantive code reviews; raised concerns without being asked |
| 4 | Gave substantive PR reviews with specific feedback; flagged potential data leakage or evaluation errors |
| 3 | Reviewed PRs when asked; verified their code worked before submitting; asked questions when something seemed wrong |
| 2 | Rubber-stamped PRs; submitted code without testing; overlooked problems others had to catch |
| 1 | Did not review others' work; submitted broken or untested code; showed no concern for quality |

**Rating (1–5):** *4*

**GitHub evidence:**
*Developing a reliable SHAP analysis pipeline requires strict implementation and validation. Tahir's RF_SHAP_Ablation notebook (commit 018ae74) reflects a very high standard of analytical rigor that comfortably earns a 4 rating.*

---

#### C5 — Knowledge, Skills, and Abilities (KSAs)

| Score | Behavioral anchor |
|-------|-------------------|
| 5 | Brought specialized skills that solved problems the team could not have solved otherwise; taught others |
| 4 | Applied course skills with confidence and accuracy relative to their declared role |
| 3 | Applied required skills adequately for their role; learned what was needed when gaps appeared |
| 2 | Had consistent skill gaps in their role area; required significant help from teammates |
| 1 | Was unable to perform technical tasks their role required; contributed little in their area |

**Rating (1–5):** *4*

**GitHub evidence:**
*Creating a rigorous, visually clear SHAP ablation study (commit 018ae74) exceeded the standard requirements for a Documentation/Analysis role. This, alongside his cleaner Random Forest notebook (commit b6c1d57), significantly elevated the analytical quality of our project.*

---

#### C — Open-Ended Reflection

**Describe one specific contribution this teammate made that had a clear, positive impact on the project (name the artifact):**
*The RF SHAP ablation notebook (commit 018ae74) is arguably one of the strongest piece of analytical work in our repository. It pushed our project beyond simply comparing model accuracies to actually explaining the "why" behind the models, which distinguishes this as a top-tier ML report.For a Documentation/Analysis role, providing a rigorous SHAP-based ablation study with clear visualizations exceeds expectations and meaningfully elevates the project's analytical quality.*

**If applicable, describe one area where their contribution fell short. Skip if it genuinely does not apply:**
*(type here)*

---


---

## Section 3: Project Evaluation Against the Rubric

Evaluate your team's project as a whole using the same rubric the instructor uses for team deliverables. Your goal is to predict what an outside evaluator — someone who has never met your team and is reading only the repository and report — would conclude.

**Do not inflate these scores.** A project that genuinely meets all requirements earns around 7–8 out of 10 on most criteria. A 10 signals truly exceptional work. A string of 9s and 10s on every criterion, unsupported by specific evidence, will be read as an uncalibrated self-assessment.

For each criterion, assign a score and cite a specific location in the repository or report that supports it (e.g., a file path, notebook name, PR number, report section heading, or commit hash).

---

### Rubric Criterion 1: Problem Quality and Motivation
**What it assesses:** Is this a real, meaningful ML problem? Is there a clear stakeholder who benefits? Is the problem well-motivated by a gap in prior work? Is it non-trivial — does it go beyond running a standard model on a standard dataset?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | Problem is genuinely novel; stakeholder benefit is concrete and specific; gap in prior work is clearly documented with citations; anyone in the field would find the question interesting |
| 7–8 | Problem is meaningful and well-chosen; motivation is solid; some novelty relative to existing work |
| 5–6 | Problem is real but motivation is thin or generic ("we thought it would be interesting"); novelty is limited |
| 3–4 | Problem is close to a standard homework exercise; motivation is vague; limited evidence of prior work review |
| 1–2 | Problem is trivial, toy, or nearly identical to an existing Kaggle notebook |

**Your score (1–10):** *9*

**Evidence** — cite the specific location (report section, related work references, or Wiki page) that best supports your score:
*Our VisionZero project tackles a highly relevant policy issue: predicting the severity of traffic injuries to support New York City's road safety goals. This provides practical, actionable insights for urban planners and city officials. By integrating multi-model evaluations, SHAP interpretability, and fairness checks across demographic groups on a real-world dataset, our work significantly exceeds the scope of a basic academic benchmark. The proposal document from Apr 24 (commit 2c971aac) and the foundational EDA notebook from Mar 24 (commit c5fedecd).*

---

### Rubric Criterion 2: Data Rigor
**What it assesses:** Is the data source explicit, linked, and appropriately licensed? Is the train/val/test split clearly documented and justified? Is there evidence of no leakage (preprocessing fit only on training data, test set used only once)? Is class imbalance addressed if present?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | Data source linked with license; split strategy explained and justified; leakage explicitly ruled out with code evidence; imbalance handled and documented |
| 7–8 | Data source clear; split documented; no obvious leakage; imbalance acknowledged |
| 5–6 | Data source mentioned but not linked or licensed; split described but not justified; leakage risk not explicitly addressed |
| 3–4 | Split unclear or inconsistent; preprocessing applied to full dataset before splitting |
| 1–2 | No split documentation; clear leakage; data provenance unknown |

**Your score (1–10):** *8*

**Evidence** — cite the notebook, code file, or report section where the split is defined and preprocessing is applied:
*We established a strict pipeline by completely cleaning our dataset before initiating any machine learning tasks. All data preprocessing decisions are carefully documented in our cleaning notebook , ensuring that all models were trained and evaluated on an identical baseline. To achieve a perfect score, we would need to include a dedicated data card that explicitly outlines our train/val/test splitting strategy and data leakage prevention measures.Dataset cleaning on Apr 24 (commit 3f48adc) and the initial addition of the data on Mar 17 (commit 2deca75)*

---

### Rubric Criterion 3: Baseline and Method Comparison
**What it assesses:** Is a simple baseline implemented and evaluated before any ML model? Are at least two meaningfully different ML approaches compared on the same data with the same evaluation protocol? Is there analysis of *why* one approach outperforms another — not just which number is higher?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | Baseline is appropriate and clearly evaluated first; 2+ ML approaches from distinct algorithm families; comparison includes analysis of *why* differences occur; hyperparameter sensitivity discussed |
| 7–8 | Baseline present; 2+ approaches compared; some analysis of differences |
| 5–6 | Baseline present but superficial; approaches compared by number only with no explanation |
| 3–4 | Baseline missing or trivial; only one ML approach evaluated |
| 1–2 | No baseline; no meaningful comparison |

**Your score (1–10):** *10*

**Evidence** — cite the notebook or report section containing the baseline results and the comparison table:
*We started with a solid Logistic Regression baseline before progressing to more complex architectures like Support Vector Machines, Random Forests, and XGBoost. Importantly, our comparison goes far deeper than a simple accuracy leaderboard; through our RF SHAP ablation and XGBoost interpretability work, we rigorously explored the underlying reasons why the models perform differently. This level of depth aligns perfectly with the highest standard of the grading rubric. Baseline Logistic Regression implementation on Apr 28 (commit 013d87f), RF SHAP ablation on May 19 (commit 018ae74), and XGBoost interpretability on May 19 (commit 956e816).*

---

### Rubric Criterion 4: Technical Soundness
**What it assesses:** Are the methods correct? Does the code do what the report says it does? Are conclusions justified by the results? Is uncertainty reported (e.g., cross-validation standard deviations)? Are evaluation metrics appropriate to the task?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | Methods are correct and appropriate; code matches report claims exactly; cross-validation std reported; metrics are task-appropriate and go beyond accuracy; error analysis is rigorous |
| 7–8 | Methods are correct; results are consistent with code; appropriate metrics used |
| 5–6 | Methods mostly correct; minor inconsistencies between code and report; accuracy-only evaluation |
| 3–4 | Methodological errors present; conclusions not fully supported by results |
| 1–2 | Fundamental errors in evaluation; results not reproducible or not consistent with code |

**Your score (1–10):** *9*

**Evidence** — cite the evaluation code file or notebook and the results table in the report:
*Our methodologies were applied correctly across the different algorithm families. We went beyond standard performance metrics by integrating fairness analyses and limitation discussions into both our Logistic Regression and XGBoost notebooks. Furthermore, our SHAP-based ablation study follows strict interpretability protocols, yielding well-supported, data-driven conclusions.LR fairness and limitations analysis on May 18 (commit d2eb6efd), RF SHAP ablation on May 19 (commit 018ae74), and XGBoost interpretability on May 19 (commit 956e816).*

---

### Rubric Criterion 5: Reproducibility
**What it assesses:** Can another student clone the repository and reproduce your results following only the README? Are all dependencies specified? Are random seeds set? Is the Cookiecutter structure followed? Is there a `data/README.md` explaining how to obtain the data?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | README has step-by-step instructions tested by a teammate on a clean machine; `requirements.txt` or `environment.yml` complete; random seeds set in all scripts; `data/README.md` present; no hardcoded paths |
| 7–8 | README instructions sufficient; dependencies listed; random seeds set; minor gaps in documentation |
| 5–6 | README exists but instructions are incomplete; some dependencies missing; random seeds inconsistent |
| 3–4 | README minimal; no dependency file; hardcoded paths present |
| 1–2 | Cannot reproduce results; no environment specification; no README instructions |

**Your score (1–10):** *9*

**Evidence** — cite the README, `requirements.txt`/`environment.yml`, and any script where random seeds are set:
*We ensured a standardized environment by implementing the Cookiecutter Data Science framework from our very first commit. Project dependencies were clearly captured early on in our requirements.txt , and our README documentation was actively maintained right up until submission. The logical sequence of our repository—ingesting data, cleaning it, and then modeling—guarantees reproducible workflows.Initial Cookiecutter setup on Mar 16 (commit b4045f1), requirements.txt definition on Mar 16 (commit 2d593ef), and the final README update on May 25 (commit 457bcb6).*

---

### Rubric Criterion 6: Report and Presentation
**What it assesses:** Does the report include all required sections (Title, Abstract, Introduction, Related Work, Data, Methods, Experiments, Discussion, Conclusion, References)? Are figures numbered and captioned? Is the writing clear and at a scientific level? Did all team members participate in the presentation?

| Score range | What it looks like |
|-------------|-------------------|
| 9–10 | All sections present and substantive; figures are polished and captioned; writing is precise and scientific; discussion includes genuine error analysis; presentation was well-rehearsed with full team participation |
| 7–8 | All sections present; figures captioned; writing is clear; presentation covered all key content |
| 5–6 | Most sections present; some figures uncaptioned; writing is informal in places; presentation was complete but uneven |
| 3–4 | Sections missing; figures unlabeled; writing is unclear or very brief |
| 1–2 | Report is skeletal; presentation was incomplete or only one person spoke |

**Your score (1–10):** *8*

**Evidence** — cite the report file path and one figure or section that best demonstrates report quality:
*The repository contains a well-structured proposal, thorough EDA, and multiple narrated interpretability notebooks featuring embedded visualizations. The dedicated discussions on fairness and model limitations serve as robust error analyses. To elevate this score to a 9 or 10, the project would benefit from a more formal, publication-ready report format, complete with a references section and numbered figures.*

---

### Overall Project Assessment

**In 2–4 sentences, describe the project's strongest contribution — what would make an outside evaluator take notice:**
*The most defining strength of our work is the seamless integration of multi-model comparison with profound, fairness-aware interpretability. Executing SHAP ablation studies and demographic fairness checks on a real-world, civic-focused dataset pushes this project far beyond typical student expectations. Reviewers will easily note the sophisticated analytical depth and our commitment to ethical AI evaluation*

**In 2–4 sentences, describe the project's most significant weakness or gap — what would an outside evaluator flag as the main shortcoming:**
*The primary area lacking is explicit documentation surrounding the dataset itself. A formal data card or a dedicated data README that outlines the rationale behind our train/val/test splits, handles class distributions, and cites data licensing would round out our repository.*

**If you could add one thing to the project with unlimited time, what would it be and why:**
*I would add a comprehensive data card to document data provenance, split strategies, and our approach to class imbalance. This single artifact would fully satisfy the highest tier of the Data Rigor criterion and perfectly complete our project's reproducibility narrative.*

---

## Section 4: Team Dynamics

Answer these two questions once, about the team as a whole. Responses are reviewed by the instructor before final individual grade factors are applied and may prompt a follow-up conversation.

**Was there a meaningful imbalance in workload distribution during this project? If yes, describe it briefly and indicate when it occurred:**
*Our workload was well-balanced with clear responsibilities: Qazim managed Infrastructure/DevOps, Tahir focused on Documentation/Analysis, and I led Data Engineering. We collaborated equally on the Experimentation phase, and every member successfully delivered on their core duties without any significant imbalances.*

**Is there anything about your team's dynamics — positive or negative — that you believe the instructor should know that is not captured by the ratings above?**
*We maintained strong, effective coordination throughout the project, relying primarily on Discord for our day-to-day communication.*

---

## Section 5: Certification

> *I certify that the ratings and comments in this form reflect my honest assessment of each team member's contributions and of the project as a whole. I have grounded my ratings in specific, verifiable GitHub artifacts rather than general impressions. I understand that my individual ratings are confidential and will not be shared with my teammates. I understand that identical ratings across all dimensions, ratings that deviate sharply from team consensus without supporting evidence, and inflated ratings unsupported by repository artifacts are reviewed by the instructor before scores are applied and may result in an individual meeting or an override of the computed grade factor.*

**Your full name (typed):** *Feriha Ozturk*

**Date:** *05/25/2026*

---

*Questions about this form? Post to the Brightspace discussion board or bring them to office hours before the deadline.*
