#!/usr/bin/env python3
"""
Air-Gapped Vector Retrieval-Augmented Generation (RAG) Engine
Part of AutoSafe-Review (Tata TechPulse CS4)
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import json
import numpy as np
from typing import List, Dict, Any, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AutomotiveRAGEngine:
    """
    100% Air-Gapped Semantic Vector Knowledge Base for MISRA C:2012, CERT-C, and ISO 26262.
    Guarantees zero external network dependencies and precise rule grounding.
    """

    def __init__(self, rules_dir: Optional[str] = None):
        if rules_dir is None:
            # Default to Input_Data/rules relative to project root
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            rules_dir = os.path.join(base_dir, "Input_Data", "rules")
        
        self.rules_dir = rules_dir
        self.documents: List[Dict[str, Any]] = []
        self.corpus_texts: List[str] = []
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.tfidf_matrix = None
        
        self.load_knowledge_base()

    def load_knowledge_base(self):
        """Loads and indexes all automotive compliance and safety rules."""
        self.documents = []
        self.corpus_texts = []
        
        rule_files = [
            ("misra_c_2012_rules.json", "MISRA C:2012"),
            ("cert_c_security_rules.json", "SEI CERT C"),
            ("iso_26262_guidelines.json", "ISO 26262")
        ]
        
        for fname, standard_name in rule_files:
            fpath = os.path.join(self.rules_dir, fname)
            if not os.path.exists(fpath):
                continue
            
            with open(fpath, "r", encoding="utf-8") as fp:
                entries = json.load(fp)
                for entry in entries:
                    rule_id = entry.get("rule_id") or entry.get("guideline_id", "GENERIC")
                    headline = entry.get("headline") or entry.get("recommendation", "")
                    desc = entry.get("description", "")
                    rationale = entry.get("automotive_rationale", "")
                    asil = entry.get("asil_level_impact") or entry.get("asil_level", "")
                    cwe = entry.get("cwe_mapping", "")
                    compliant = entry.get("compliant_example", "")
                    non_compliant = entry.get("non_compliant_example", "")
                    
                    # Synthesize dense semantic representation
                    searchable_content = (
                        f"{rule_id} {standard_name} {headline}\n"
                        f"Description: {desc}\n"
                        f"Automotive Safety Rationale: {rationale}\n"
                        f"ASIL Impact: {asil}\n"
                        f"CWE Vulnerability: {cwe}\n"
                        f"Non-Compliant Pattern: {non_compliant}\n"
                        f"Compliant Solution: {compliant}"
                    )
                    
                    self.documents.append({
                        "rule_id": rule_id,
                        "standard": standard_name,
                        "severity": entry.get("severity", "Required"),
                        "headline": headline,
                        "description": desc,
                        "automotive_rationale": rationale,
                        "asil_level_impact": asil,
                        "cwe_mapping": cwe,
                        "compliant_example": compliant,
                        "non_compliant_example": non_compliant,
                        "full_text": searchable_content
                    })
                    self.corpus_texts.append(searchable_content)

        # Build local semantic vector index
        if self.corpus_texts:
            self.vectorizer = TfidfVectorizer(
                ngram_range=(1, 3),
                sublinear_tf=True,
                stop_words="english",
                token_pattern=r'(?u)\b[a-zA-Z0-9_\-\.:]+\b'
            )
            self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus_texts)
            print(f"[RAG Engine] Successfully indexed {len(self.documents)} safety rules.")

    def query(self, query_text: str, top_k: int = 3, filter_standard: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieves top-k most relevant rules for a given code snippet, diagnostic message, or query.
        """
        if not self.vectorizer or self.tfidf_matrix is None:
            return []

        query_vec = self.vectorizer.transform([query_text])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Rank by similarity score
        ranked_indices = np.argsort(similarities)[::-1]
        
        results = []
        for idx in ranked_indices:
            doc = self.documents[idx]
            score = float(similarities[idx])
            
            if filter_standard and doc["standard"].lower() != filter_standard.lower():
                continue
                
            doc_copy = dict(doc)
            doc_copy["similarity_score"] = round(score, 4)
            results.append(doc_copy)
            
            if len(results) >= top_k:
                break
                
        return results

    def format_grounding_context(self, retrieved_rules: List[Dict[str, Any]]) -> str:
        """
        Formats retrieved rules into an anti-hallucination context block for the LLM prompt.
        """
        if not retrieved_rules:
            return "No specific automotive rule retrieved."
            
        blocks = []
        for r in retrieved_rules:
            block = (
                f"### [OFFICIAL CITATION: {r['rule_id']} | {r['standard']} | Severity: {r['severity']}]\n"
                f"- Headline: {r['headline']}\n"
                f"- Rationale: {r['automotive_rationale']}\n"
                f"- ASIL Safety Impact: {r['asil_level_impact']}\n"
                f"- CWE Reference: {r['cwe_mapping']}\n"
                f"- Required Compliant Pattern:\n```c\n{r['compliant_example']}\n```\n"
            )
            blocks.append(block)
            
        return "\n".join(blocks)
