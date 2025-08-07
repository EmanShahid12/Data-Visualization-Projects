import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Experience': [1, 2, 3, 4, 5],
    'Salary': [30000, 35000, 40000, 45000, 50000],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR']
})
fig = px.scatter(df, x='Experience', y='Salary', color='Department',
                 title='Interactive Scatter Plot: Experience vs Salary')
fig.show()
