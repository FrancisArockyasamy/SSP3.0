# SSP3.0
Steps to configure the environment:

    Step 1:
        linux: python3 -m venv venv
        windows: python -m venv venv

    Step 2:
        linux: source venv/bin/activate
        windows: venv\Scripts\activate.bat
        
    Step 3:
        pip install -r requirements.txt

    Step 4:
        uvicorn main:app --reload