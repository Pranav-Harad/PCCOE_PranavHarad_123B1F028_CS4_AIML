#!/usr/bin/env python3
"""
Generates printable PDFs for Student Declaration and AI Tool Usage Declaration.
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_declaration_pdfs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=14, leading=17, alignment=1, textColor=colors.HexColor('#002B49'))
    subtitle_style = ParagraphStyle('Sub', fontName='Helvetica-Bold', fontSize=10, leading=13, alignment=1, textColor=colors.HexColor('#1E293B'))
    section_style = ParagraphStyle('Sec', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=colors.HexColor('#002B49'), spaceBefore=8, spaceAfter=4)
    body_style = ParagraphStyle('Body', fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor('#1E293B'))
    bullet_style = ParagraphStyle('Bul', parent=body_style, leftIndent=15, firstLineIndent=-10, spaceAfter=4)
    cell_style = ParagraphStyle('Cell', fontName='Helvetica', fontSize=8, leading=10.5, textColor=colors.HexColor('#1E293B'))
    cell_bold = ParagraphStyle('CellB', parent=cell_style, fontName='Helvetica-Bold')

    # 1. Student Declaration PDF
    doc1 = SimpleDocTemplate(os.path.join(base_dir, "Student_Declaration_Signed.pdf"), pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    story1 = [
        Paragraph("TATA TECHNOLOGIES LTD. - TECH PULSE FY-26", subtitle_style),
        Paragraph("STUDENT DECLARATION", title_style),
        Spacer(1, 8),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002B49'), spaceAfter=12),
        Paragraph("<b>Student Name:</b> Pranav Ravindra Harad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>PRN:</b> 123B1F028", body_style),
        Paragraph("<b>Institute:</b> Pimpri Chinchwad College of Engineering (PCCOE), Pune", body_style),
        Paragraph("<b>Programme / Batch:</b> B.Tech Artificial Intelligence & Machine Learning / TechPulse FY-26", body_style),
        Paragraph("<b>Case Study ID:</b> CS4 (Secure Code Debugging and Review Assistant)", body_style),
        Paragraph("<b>Project Title:</b> AutoSafe-Review: Air-Gapped, AST-Aware Hybrid Diagnostic & MISRA/ISO 26262 ECU Code Review Assistant", body_style),
        Spacer(1, 12),
        Paragraph("Declarations Confirmed by Candidate:", section_style),
        Paragraph("☑ <b>Originality of Work:</b> I confirm that the submitted project and its implementation represent my own original work.", bullet_style),
        Paragraph("☑ <b>Citation of Resources:</b> I have cited all external code, datasets, reference models, and standard documents (MISRA C:2012, SEI CERT C, ISO 26262:2018).", bullet_style),
        Paragraph("☑ <b>No Fabrication of Results:</b> I have not fabricated or manipulated any benchmark metrics or evaluation results. All quantitative metrics are generated via reproducible evaluation scripts (run_evaluation.py).", bullet_style),
        Paragraph("☑ <b>Accurate Attribution:</b> I have accurately stated all individual contributions and technical approaches.", bullet_style),
        Paragraph("☑ <b>Declaration of AI Tools:</b> I have declared all AI tools, coding assistants, and local pre-trained models used in this project.", bullet_style),
        Paragraph("☑ <b>Technical Understanding:</b> I understand and can explain, justify, and defend every part of the submitted implementation, architecture, and code during faculty and industry evaluation.", bullet_style),
        Spacer(1, 30),
        Table([
            [Paragraph("<b>Student Signature:</b> ___________________________", body_style), Paragraph("<b>Date:</b> October 9, 2026", body_style)],
            [Paragraph("<b>Name:</b> Pranav Ravindra Harad", body_style), Paragraph("<b>PRN:</b> 123B1F028", body_style)]
        ], colWidths=[260, 260], style=[('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('TOPPADDING', (0,0), (-1,-1), 8)])
    ]
    doc1.build(story1)

    # 2. AI Tool Usage Declaration PDF
    doc2 = SimpleDocTemplate(os.path.join(base_dir, "AI_Tool_Usage_Declaration.pdf"), pagesize=letter, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    story2 = [
        Paragraph("TATA TECHNOLOGIES LTD. - TECH PULSE FY-26", subtitle_style),
        Paragraph("AI-TOOL USAGE DECLARATION", title_style),
        Spacer(1, 8),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002B49'), spaceAfter=12),
        Paragraph("<b>Student Name:</b> Pranav Ravindra Harad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>PRN:</b> 123B1F028", body_style),
        Paragraph("<b>Institute:</b> Pimpri Chinchwad College of Engineering (PCCOE), Pune", body_style),
        Paragraph("<b>Case Study ID:</b> CS4 (Secure Code Debugging and Review Assistant)", body_style),
        Spacer(1, 10),
        Paragraph("Declared AI Tools and Pre-Trained Models:", section_style),
        Table([
            [Paragraph("<b>AI Tool / Model</b>", cell_bold), Paragraph("<b>Version / Provider</b>", cell_bold), Paragraph("<b>Purpose</b>", cell_bold), Paragraph("<b>Artifact Affected</b>", cell_bold), Paragraph("<b>Verified (Y/N)</b>", cell_bold)],
            [Paragraph("Antigravity Assistant", cell_style), Paragraph("Google DeepMind Agent", cell_style), Paragraph("Architecture design, code scaffolding, test scripts", cell_style), Paragraph("Code/backend/, app.py, utils/", cell_style), Paragraph("Y", cell_style)],
            [Paragraph("Qwen2.5-Coder", cell_style), Paragraph("7B-Instruct (Local 4-bit)", cell_style), Paragraph("Local offline code review, root-cause & fix synthesis", cell_style), Paragraph("Model_Prompts_Config/, local_llm.py", cell_style), Paragraph("Y", cell_style)],
            [Paragraph("BAAI/bge-small-en-v1.5", cell_style), Paragraph("HuggingFace / Sklearn", cell_style), Paragraph("Semantic Vector RAG over MISRA/CERT rules", cell_style), Paragraph("Code/backend/rag_engine.py", cell_style), Paragraph("Y", cell_style)]
        ], colWidths=[110, 110, 140, 120, 50], style=[
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4)
        ]),
        Spacer(1, 14),
        Paragraph("<b>Student Confirmation:</b> I confirm that all code logic, deterministic static analysis algorithms, AST chunking rules, and evaluation scripts have been verified and executed locally by me. No proprietary automotive source code was transmitted over external networks.", body_style),
        Spacer(1, 30),
        Table([
            [Paragraph("<b>Student Signature:</b> ___________________________", body_style), Paragraph("<b>Date:</b> October 9, 2026", body_style)],
            [Paragraph("<b>Name:</b> Pranav Ravindra Harad", body_style), Paragraph("<b>PRN:</b> 123B1F028", body_style)]
        ], colWidths=[260, 260], style=[('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('TOPPADDING', (0,0), (-1,-1), 8)])
    ]
    doc2.build(story2)
    print("[SUCCESS] Generated Student_Declaration_Signed.pdf and AI_Tool_Usage_Declaration.pdf!")

if __name__ == "__main__":
    generate_declaration_pdfs()
