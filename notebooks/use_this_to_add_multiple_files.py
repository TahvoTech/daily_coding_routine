import os

topics = [
    "Hello World",
    "Variables and Data Types",
    "Basic Arithmetic Operations",
    "Conditional Statements",
    "Loops (for, while)",
    "Functions",
    "Lists",
    "Dictionaries",
    "File IO",
    "String Manipulation",
    "Data Cleaning",
    "Sales Forecasting",
    "Customer Segmentation",
    "Sentiment Analysis",
    "Churn Prediction",
    "Recommendation System",
    "Time Series Analysis",
    "Anomaly Detection",
    "Chatbot Development",
    "Image Classification",
    "Text Summarization",
    "Market Basket Analysis",
    "Fraud Detection",
    "Inventory Management",
    "Customer Lifetime Value",
    "AB Testing",
    "Speech Recognition",
    "Optical Character Recognition (OCR)",
    "Data Visualization",
    "Automated Reporting"
]

# Create notebooks directory if it doesn't exist
if not os.path.exists('notebooks'):
    os.makedirs('notebooks')

# Create Jupyter Notebook files with numbered topics
for i, topic in enumerate(topics, start=1):
    filename = f"notebooks/{i:02d}_{topic.replace(' ', '_').replace('(', '').replace(')', '')}.ipynb"
    with open(filename, 'w') as f:
        f.write('{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 2\n}')

print("Jupyter Notebook files created successfully.")