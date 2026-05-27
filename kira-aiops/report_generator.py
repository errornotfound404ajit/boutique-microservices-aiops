from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_incident_report(content):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"reports/incident_{timestamp}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "KIRA AI Incident Report",
        styles["Title"]
    )

    story.append(title)

    story.append(
        Spacer(1, 20)
    )

    body = Paragraph(
        content.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    story.append(body)

    doc.build(story)

    return filename