import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize an empty DataFrame or load existing data
try:
    expenses = pd.read_csv('expenses.csv')
except FileNotFoundError:
    expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Function to add a new expense
def add_expense(date, category, amount):
    new_expense = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount]})
    return expenses.append(new_expense, ignore_index=True)

# Streamlit app layout
st.title('Expense Tracker')

st.header('Add a new expense')
with st.form(key='expense_form'):
    date = st.date_input('Date')
    category = st.selectbox('Category', ['Food', 'Transport', 'Bills', 'Entertainment', 'Other'])
    amount = st.number_input('Amount', min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label='Add Expense')

if submit_button:
    expenses = add_expense(date, category, amount)
    expenses.to_csv('expenses.csv', index=False)
    st.success('Expense added successfully!')

# Display expenses
st.header('Expenses')
st.write(expenses)

# Visualizations
st.header('Visualizations')

# Pie chart for expense distribution by category
fig1, ax1 = plt.subplots()
category_distribution = expenses.groupby('Category')['Amount'].sum()
ax1.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%')
ax1.set_title('Expenses by Category')
st.pyplot(fig1)

# Bar chart for expenses over time
fig2, ax2 = plt.subplots()
expenses['Date'] = pd.to_datetime(expenses['Date'])
expenses_by_date = expenses.groupby('Date')['Amount'].sum()
ax2.bar(expenses_by_date.index, expenses_by_date)
ax2.set_title('Expenses Over Time')
ax2.set_xlabel('Date')
ax2.set_ylabel('Amount')
st.pyplot(fig2)

# Line chart for monthly expenses
fig3, ax3 = plt.subplots()
expenses['Month'] = expenses['Date'].dt.to_period('M')
monthly_expenses = expenses.groupby('Month')['Amount'].sum()
ax3.plot(monthly_expenses.index.astype(str), monthly_expenses)
ax3.set_title('Monthly Expenses')
ax3.set_xlabel('Month')
ax3.set_ylabel('Amount')
st.pyplot(fig3)

