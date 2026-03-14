---
name: authority-researcher
description: Searches the internet for authorities, domain experts, scientific papers, and credible sources to validate information. Use this skill when you have doubts, need to validate a specific subject, or want to fact-check information to prevent hallucinations.
---

# Authority Researcher

## Overview
This skill mandates the AI to rigorously validate information by searching the internet for authoritative sources such as domain experts, renowned companies, scientific papers, and books. It ensures high-quality, grounded, and factual responses, significantly reducing the risk of hallucinations.

## Usage Guidelines

When you are asked to validate a subject, answer a complex domain-specific question, or whenever you have doubts about a fact, you MUST invoke the internet search tools (e.g., `google_web_search`, `web_fetch`) using the following strategies:

1.  **Search for Experts & Scientific Literature:** Use search queries that look for academic papers, reputable journals, expert opinions, and official company documentation.
    *   Examples: "[Topic] scientific paper", "[Topic] domain experts consensus", "[Topic] official documentation site:.edu OR site:.gov".

2.  **Evaluate Authority:** Assess the credibility of the sources found. Prefer peer-reviewed papers, well-known industry leaders, established institutions, and recognized books over generic blogs.

3.  **Synthesize Findings & Cite Sources:** After researching, you MUST structure your response to explicitly show the references used. This is CRITICAL to ensure you are not hallucinating. You MUST provide:

    **Format A: Detailed Description**
    *   **Description:** A comprehensive explanation of the subject based on the authoritative sources found.
    *   **Verified References:** A bulleted list of all the sources, papers, experts, and books used to compile the description. Include URLs, titles, and authors to allow for manual verification.

    **Format B: Confidence Score**
    *   **Score:** A confidence score out of 10 (e.g., 9.5/10) regarding the factual accuracy of the information provided.
    *   **Reasoning:** A detailed justification for the score, explaining why the sources give this level of confidence.
    *   **Verified References:** A comprehensive list of all authoritative references utilized, including direct links or citations to the specific information being validated.

## Fact-Checking Methodology
*   Always cross-reference multiple authoritative sources. If experts disagree, mention the consensus or the leading perspectives.
*   Do not rely on your internal training data alone for verifiable facts; always ground your answers with live search results when using this skill.
