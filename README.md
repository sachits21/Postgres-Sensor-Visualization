# Ark Biotech - Data Systems Internship Project - Submission README

This repository contains my submission for the Ark Biotech Data Systems Internship Project. Below is a summary of the key tasks outlined in the provided README:

## Project Tasks

1. **Technical Setup:**
   - The project structure includes a `src` directory with the `ark_app` package, a `Dockerfile`, `compose.yaml`, `local.env`, and `pyproject.toml`.
   
2. **Database Access:**
   - The database credentials are provided via environment variables in `local.env`.

3. **Database Schema:**
   - The database includes tables such as `CM_HAM_DO_AI1/Temp_value`, `CM_HAM_PH_AI1/pH_value`, `CM_PID_DO/Process_DO`, and `CM_PRESSURE/Output`.

4. **Web Dashboard:**
   - The task involves creating a web-based dashboard to visualize real-time process data.
   - The dashboard should serve interactive plots for Temperature, pH, Dissolved Oxygen, and Pressure over time.

5. **Evaluation Criteria:**
   - Successful package installation.
   - A functional dashboard accessible at http://localhost:8000/.
   - Compliance with MVP specifications.
   - Code quality in terms of PEP8, type annotations, configuration handling, logging, and documentation.

6. **Running the Code:**
   - The code is executed using `docker compose up` with the dashboard accessible at http://localhost:8000/.

7. **Submission:**
   - The Python wheel file (`.whl`) is generated using `docker compose run app python -m build`.
   - Submission is done through the provided [Google Form](https://forms.gle/cbRsUXBGDiXTAUc88) by the specified deadline.

8. **Confidentiality Notice:**
   - A reminder to keep the project and dataset confidential and refrain from sharing on public platforms.

## Project Completion

I have fulfilled the outlined tasks, and the provided documentation includes details on project execution, evaluation criteria, running the code, and the submission process.

