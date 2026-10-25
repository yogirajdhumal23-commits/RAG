# Citizen Scheme Navigator

A small Streamlit app that helps citizens shortlist Indian public schemes using age,
highest education completed, and annual family income. It includes an initial index
for the National Scholarship Portal's college scholarship, PMKVY skill training, and
the Startup India Seed Fund Scheme.

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

## Important limitations

This is an initial screening aid, not an eligibility determination or an application
portal. Scheme criteria and documents can vary by year, state, category, course, batch,
and applicant circumstances. The app only rejects a profile when a listed criterion
can be checked from the supplied age, education, or income. It identifies unmodeled
requirements and links to the official sources; applicants should confirm the current
notice and exact mandatory documents before applying.

The app processes the entered details in the current session only and does not store
or transmit them.
