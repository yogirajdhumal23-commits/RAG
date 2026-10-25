from dataclasses import dataclass
from typing import Optional

import streamlit as st


@dataclass(frozen=True)
class Scheme:
    name: str
    short_name: str
    audience: str
    audience_hi: str
    benefit: str
    benefit_hi: str
    source_name: str
    source_url: str
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    education_min: Optional[int] = None
    income_max: Optional[int] = None
    education_rule: str = ""
    income_rule: str = ""
    age_rule: str = ""
    extra_eligibility: tuple[str, ...] = ()
    documents: tuple[str, ...] = ()
    document_note: str = ""
    screening_note: str = ""


EDUCATION_LEVELS = [
    "No formal schooling",
    "Primary school",
    "Middle school",
    "Class 10",
    "Class 12",
    "Diploma / ITI",
    "Undergraduate",
    "Postgraduate",
]
EDUCATION_RANK = {level: rank for rank, level in enumerate(EDUCATION_LEVELS)}

SCHEMES = [
    Scheme(
        name="Central Sector Scheme of Scholarship for College and University Students",
        short_name="NSP — College and University Scholarship (CSSS)",
        audience="Class 12 graduates pursuing regular college or university studies",
        audience_hi="12वीं पास विद्यार्थी जो नियमित कॉलेज या यूनिवर्सिटी में पढ़ रहे हैं",
        benefit=(
            "Merit-based financial help for eligible college students. The amount depends "
            "on the study level and current scheme rules."
        ),
        benefit_hi=(
            "योग्य कॉलेज विद्यार्थियों को पढ़ाई के लिए छात्रवृत्ति मिल सकती है। "
            "राशि कक्षा/पढ़ाई के स्तर और मौजूदा नियमों पर निर्भर करती है।"
        ),
        source_name="National Scholarship Portal",
        source_url="https://scholarships.gov.in/",
        education_min=EDUCATION_RANK["Class 12"],
        income_max=450_000,
        education_rule="Class 12 pass and enrolled in a regular college/university course.",
        income_rule="Family income must be within the scheme's annual limit of ₹4.5 lakh.",
        extra_eligibility=(
            "Selection also depends on the prescribed Class 12 merit/board criteria.",
            "Course, renewal, and other-scholarship rules apply; check the current notice.",
        ),
        documents=(
            "NSP One Time Registration (OTR) number",
            "Class 12 marksheet",
            "Family income certificate",
            "Aadhaar details or the identity document accepted by the portal",
            "Bank account details in the student's name",
            "Current college admission/enrolment proof",
        ),
        document_note=(
            "Prepare these for the application. The portal/institute may request additional "
            "proof, and the exact list can change by academic year."
        ),
        screening_note=(
            "This is only an initial screen: the app cannot check your board merit rank, "
            "enrolment status, renewal status, or other scholarship rules."
        ),
    ),
    Scheme(
        name="Pradhan Mantri Kaushal Vikas Yojana (PMKVY)",
        short_name="PMKVY — Skill training",
        audience="People seeking short-term skill training or recognition of prior learning",
        audience_hi="कम समय का कौशल प्रशिक्षण या पहले से सीखे कौशल की पहचान चाहने वाले लोग",
        benefit=(
            "Approved training and assessment intended to help build job skills. Course "
            "availability, assessment, and any candidate benefits depend on the batch."
        ),
        benefit_hi=(
            "मंज़ूरशुदा प्रशिक्षण से काम के कौशल सीखने और उनकी जाँच कराने का मौका मिलता है। "
            "कोर्स और सुविधाएँ बैच के अनुसार बदल सकती हैं।"
        ),
        source_name="Ministry of Skill Development and Entrepreneurship",
        source_url="https://www.msde.gov.in/en/schemes-initiatives/pmkvy",
        age_rule="Age limits are set by the applicable course/batch; there is no single age test here.",
        education_rule="Education requirements depend on the selected course and qualification.",
        income_rule="No universal family-income cut-off is applied by this navigator.",
        documents=(
            "Identity proof accepted by the training centre",
            "Education certificate, if required for the chosen course",
            "Address/contact details requested during enrolment",
        ),
        document_note=(
            "This is a preparation list, not a universal mandatory-document list. Ask the "
            "approved training centre for the current batch's exact requirements."
        ),
        screening_note=(
            "Your profile does not rule the scheme out on these three details alone. "
            "Course, age, location, and batch eligibility still need checking."
        ),
    ),
    Scheme(
        name="Startup India Seed Fund Scheme (SISFS)",
        short_name="Startup India — Seed Fund",
        audience="Early-stage startups applying through an approved incubator",
        audience_hi="मंज़ूरशुदा इनक्यूबेटर के ज़रिए आवेदन करने वाले शुरुआती स्टार्टअप",
        benefit=(
            "Eligible startups may receive up to ₹20 lakh as a grant for proof of concept, "
            "prototype development, or product trials, and up to ₹50 lakh through debt or "
            "convertible instruments for market entry or scaling."
        ),
        benefit_hi=(
            "योग्य नए कारोबार को शुरुआती नमूना बनाने या उत्पाद आज़माने के लिए ₹20 लाख तक "
            "अनुदान मिल सकता है। बाज़ार में आगे बढ़ने के लिए ₹50 लाख तक कर्ज़ या "
            "बदल सकने वाले निवेश का विकल्प हो सकता है।"
        ),
        source_name="Startup India Seed Fund Scheme",
        source_url="https://seedfund.startupindia.gov.in/",
        extra_eligibility=(
            "The applicant must be an eligible startup; individual age, education, and family "
            "income do not establish startup eligibility.",
            "Startup recognition, incorporation date, Indian promoter ownership, prior support, "
            "and incubator selection rules must be checked in the current guidelines.",
        ),
        documents=(
            "Startup incorporation and recognition documents",
            "Founder/promoter identity and ownership details",
            "Pitch deck and business plan",
            "Prototype, product, or proof-of-concept evidence",
            "Financial statements and details of prior public funding, if applicable",
        ),
        document_note=(
            "These are preparation items, not a guaranteed mandatory list. The selected "
            "incubator sets the application evidence and may request more."
        ),
        screening_note=(
            "Your age, education, and family income are not enough to decide this scheme. "
            "This is shown for startup founders to review the separate business criteria."
        ),
    ),
]


def assess_scheme(scheme: Scheme, age: int, education: str, income: int) -> tuple[str, list[str]]:
    failed: list[str] = []
    if scheme.age_min is not None and age < scheme.age_min:
        failed.append(f"Age must be at least {scheme.age_min}.")
    if scheme.age_max is not None and age > scheme.age_max:
        failed.append(f"Age must be no more than {scheme.age_max}.")
    if scheme.education_min is not None:
        if EDUCATION_RANK[education] < scheme.education_min:
            failed.append("The selected education level is below the scheme's stated minimum.")
    if scheme.income_max is not None and income > scheme.income_max:
        failed.append(f"Annual family income is above ₹{scheme.income_max:,}.")

    if failed:
        return "Does not match the entered details", failed
    if scheme.extra_eligibility or scheme.screening_note:
        return "Potential match — verify remaining rules", []
    return "Matches the entered details", []


def render_scheme(scheme: Scheme, age: int, education: str, income: int, language: str) -> None:
    status, failed = assess_scheme(scheme, age, education, income)
    with st.container(border=True):
        st.subheader(scheme.short_name)
        st.caption(f"**Initial screen:** {status}")
        if failed:
            for reason in failed:
                st.write(f"- {reason}")

        if language == "हिन्दी":
            st.write(f"**किसके लिए:** {scheme.audience_hi}")
            st.write(f"**फ़ायदा, आसान भाषा में:** {scheme.benefit_hi}")
            st.info(
                "सरल हिंदी: यह सिर्फ शुरुआती जाँच है। आवेदन से पहले आधिकारिक वेबसाइट पर "
                "नियम, पात्रता और दस्तावेज़ ज़रूर जाँचें।"
            )
        else:
            st.write(f"**Who it is for:** {scheme.audience}")
            st.write(f"**Benefit, in simple terms:** {scheme.benefit}")
            st.info(
                "Simple English: This is only a first check. Confirm the current rules, "
                "eligibility, and documents on the official website before applying."
            )

        with st.expander("Eligibility checks"):
            if scheme.age_rule:
                st.write(f"- **Age:** {scheme.age_rule}")
            if scheme.education_rule:
                st.write(f"- **Education:** {scheme.education_rule}")
            if scheme.income_rule:
                st.write(f"- **Family income:** {scheme.income_rule}")
            for item in scheme.extra_eligibility:
                st.write(f"- {item}")
            if scheme.screening_note:
                st.caption(scheme.screening_note)

        with st.expander("Document checklist"):
            for document in scheme.documents:
                st.checkbox(document, key=f"{scheme.short_name}:{document}")
            st.caption(scheme.document_note)

        st.link_button(f"Open official source: {scheme.source_name}", scheme.source_url)


def main() -> None:
    st.set_page_config(page_title="Citizen Scheme Navigator", page_icon="🇮🇳", layout="wide")
    st.title("Citizen Scheme Navigator")
    st.write(
        "Find schemes worth checking using your age, education, and annual family income. "
        "The results are a first-step guide, not an eligibility decision."
    )

    with st.sidebar:
        st.header("Your details")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=22, step=1)
        education = st.selectbox("Highest education completed", EDUCATION_LEVELS)
        income = st.number_input(
            "Annual family income (₹)",
            min_value=0,
            max_value=100_000_000,
            value=300_000,
            step=10_000,
            help="Enter total family income for one year, in rupees.",
        )
        language = st.selectbox("Explanation language", ["English", "हिन्दी"])

    st.subheader("Schemes to explore")
    st.caption(
        "Only criteria that can be checked from these three answers are used to rule out a "
        "scheme. None of these listed schemes has one universal individual-age cut-off that "
        "can safely be applied here; course/batch or startup-specific rules are shown separately. "
        "A possible match is not guaranteed eligibility."
    )
    for scheme in SCHEMES:
        render_scheme(scheme, int(age), education, int(income), language)

    st.warning(
        "Scheme rules, open application dates, benefits, and required documents can change. "
        "This app does not collect or save the details entered here. Always follow the latest "
        "official notice and contact the scheme authority or training centre if unsure."
    )


if __name__ == "__main__":
    main()
