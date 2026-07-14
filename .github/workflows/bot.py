name: Run Python Bot

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 * * * *' # يعمل تلقائياً كل ساعة (يمكنك تعديل وقت الجدولة)

jobs:
  run-python:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install playwright requests
          playwright install-deps
          playwright install

      - name: Run Python Script
        run: python bot.py
        env:
          SESSION_DATA: ${{ secrets.SESSION_DATA }}

