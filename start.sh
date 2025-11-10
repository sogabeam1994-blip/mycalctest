#!/bin/bash
# Start FastAPI in background
uvicorn Backend:app --host 0.0.0.0 --port 8000 &

# Start Streamlit
streamlit run FrontEnd.py --server.port 80 --server.address 0.0.0.0