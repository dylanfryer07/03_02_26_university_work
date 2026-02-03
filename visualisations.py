import plotly.express as px
import pandas as pd
df = pd.read_csv("Group Activity-20260203\Dataset for data cleaning activity\Forward_Feast_Survey.csv")
def visualise_age(df):
    fig_age = px.histogram(df, x="Age", nbins=20, title="Age Distribution of Survey Respondents")
    fig_age.show()
def visualise_education(df):
    fig_education = px.histogram(df, x="Education Level", title="Education Level Distribution")
    fig_education.show()
def visualise_region(df):
    fig_region = px.histogram(df, x="Region", title="Geographical Distribution of Respondents")
    fig_region.show()
def visualise_gender(df):
    fig_gender = px.histogram(df, x="Gender", title="Gender Distribution of Respondents")
    fig_gender.show()
# Complete the function name below
visualise_age(df)
visualise_education(df)
visualise_region(df)
visualise_gender(df)