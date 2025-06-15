import re
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.sidebar.title("Upload File")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["log"])

st.title("File Upload App")

if uploaded_file is not None:
    st.success("File successfully uploaded!")

    log_pattern = re.compile(r'(?P<timestamp>[\d\-:, ]+) - (?P<level>\w+) - (?P<message>.+)')

    log_counts = Counter()
    errors = []
    infos=[]
    debugs=[]
    content=uploaded_file.read().decode("utf-8")


    for line in content.splitlines():
        match = log_pattern.match(line)

        if match:
            data = match.groupdict()
            timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
            level = data['level']
            message = data['message']

            log_counts[level] += 1
            if level == 'ERROR':
                errors.append((timestamp, message))
            elif level == 'INFO':
                infos.append((timestamp, message))
            elif level=='DEBUG':
                debugs.append((timestamp, message))


    st.subheader(f"Errors found: {len(errors)}")

    n=0
    for error in errors:
        n+=1
        st.write(f"Error {n}: {error[1]}")

    n=0

    st.subheader(f"Info found: {len(infos)}")
    for info in infos:
        n+=1
        st.write(f"Info {n}: {info[1]}")

    n=0
    st.subheader(f"Debug found: {len(debugs)}")
    for debug in debugs:
        n+=1
        st.write(f"Debug {n}: {debug[1]}")

    st.text_area("Log file Content", content, height=300)

else:
    st.info("Please upload a file to proceed.")
