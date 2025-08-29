# Jawaher Odoo Connector API
FastAPI project
## How to run the API
1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment called `.venv`:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```
5. Upgrade pip to the latest version:
   ```bash
   python -m pip install --upgrade pip
   ```
6. Install the required packages:
for Linux/Mac:
   ```bash
   pip install -r requirements/api-requirements-linux.txt
   ```
for Windows:
   ```bash
    pip install -r requirements/api-requirements-windows.txt
    ```
7. Configure the environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables to the `.env` file:
     ```
     ODOO_REPO_PATH=your_odoo_repo_full_path
     ODOO_CONFIG_PATH=your_odoo_config_full_path
     ODOO_DB_NAME=your_odoo_database_name
     ODOO_PYTHON_SITE_PACKAGES_PATH= your_python_site_packages_path_which_odoo_use
     ```
   - Replace `your_odoo_repo_full_path`, `your_odoo_config_full_path` and `your_odoo_database_name` with the actual values.
   - Example:
     ```
     ODOO_REPO_PATH=/path/to/odoo/repo
     ODOO_CONFIG_PATH=/path/to/odoo/config
     ODOO_DB_NAME=odoo_db_name
     ODOO_PYTHON_SITE_PACKAGES_PATH = E:\odoo-18-dev\.venv\Lib\site-packages
     ```
    - you can make `/usr/lib/python3/dist-packages` as ODOO_REPO_PATH if odoo enterprise is installed via apt package manager (because the python site packages path will contain odoo and odoo-enterprise packages).
    - You can make `ODOO_REPO_PATH` and `ODOO_PYTHON_SITE_PACKAGES_PATH` the same if odoo enterprise is installed.
8. Run the API server:
Navigate to the project directory and run:
   ```bash
   uvicorn src.main:app --host localhost --port 8000 --reload
   ```
   or use gunicorn with uvicorn workers:
   ```bash
    gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind localhost:8000 --reload
    ```

## API Documentation
The API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs) when the server is running , or you can access the interactive API documentation at [http://localhost:8000/scalar_docs](http://localhost:8000/scalar_docs).