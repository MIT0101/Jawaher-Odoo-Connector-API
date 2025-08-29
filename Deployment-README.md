## Deployment info

### Steps to deploy the application

1. navigate to web deployment directory.

    ```bash
    cd /var/www/
    ```

2. clone the repository , example dir name : `Jawaher-Odoo-Connector-API`

    ```bash
    git clone <repository_url>
    ```

3. Navigate to the project directory
, assume the directory name is `Jawaher-Odoo-Connector-API`

    ```bash
    cd <project_directory>
    ```

4. Create a virtual environment called `.venv`:

    ```bash
    sudo python3 -m venv .venv
    ```

5. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

6. Upgrade pip to the latest version:

    ```bash
    sudo python3 -m pip install --upgrade pip
    ```

7. install dependencies for building some python packages:

    ```bash
    sudo apt install -y \
        pkg-config \
        python3-dev
    ```
8. install api requirements (Linux/Mac):
   ```bash
   pip install -r requirements/api-requirements-linux.txt
   ```

9. Configure the environment variables by creating a `.env` file in the root directory of the project. copy it from
   `.env.example` and add the following environment variables to the `.env` file:

    ```bash
    cp .env.example .env
    ```

10. set the correct values in the `.env` file:
    use system paths for ODOO_REPO_PATH because odoo enterprise is installed via apt package manager.

    ```java
    ODOO_REPO_PATH = /usr/lib/python3/dist-packages  
    ODOO_CONFIG_PATH = /etc/odoo/odoo.conf  
    ODOO_DB_NAME = YourDBName
    ODOO_PYTHON_SITE_PACKAGES_PATH = /usr/lib/python3/dist-packages
    ```

11. deactivate the virtual environment:

    ```bash
    deactivate
    ```

12. update project directory permissions to match running odoo user (odoo):

    ```bash
    sudo chown -R odoo:odoo /var/www/Jawaher-Odoo-Connector-API/
    ```

    ```bash
    sudo chmod -R 775 awaher-Odoo-Connector-API
    ```

13. You can test run the application manually by activating the virtual environment and running uvicorn:

    ```bash
    sudo -u odoo /var/www/Jawaher-Odoo-Connector-API/.venv/bin/uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
    ```

14. Create a systemd service file for the FastAPI application:

    ```bash
    sudo vim /etc/systemd/system/odoo-connector-api.service
    ```

    Add the following content to the file:
    
    ```ini
    [Unit]
    Description = Jawaher Odoo Connector FastAPI
    After = network.target
    
    [Service]
    Type = simple
    User = odoo
    Group = odoo
    WorkingDirectory = /var/www/Jawaher-Odoo-Connector-API
    ExecStart = /var/www/Jawaher-Odoo-Connector-API/.venv/bin/uvicorn src.main:app --host 0.0.0.0 --port 8000
    Restart = always
    RestartSec = 5
    StandardOutput = append:/var/log/jawaher-api.log
    StandardError = append:/var/log/jawaher-api.log
    
    [Install]
    WantedBy = multi-user.target
    ```

15. Reload systemd to apply the changes:

    ```bash
    sudo systemctl daemon-reload
    ```

16. Start and enable the service to run on boot:

    ```bash
    sudo systemctl start odoo-connector-api
    ```

    ```bash
    sudo systemctl enable odoo-connector-api
    ```
