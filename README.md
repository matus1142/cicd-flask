GitHub Actions for CI, and Vercel for deployment.

### Step 1: Set Up Your Flask Project

1. **Create a New Python Project**:
   ```bash
   mkdir my-hobby-project
   cd my-hobby-project
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install Flask pytest
   ```

2. **Create a Simple Flask App**:
   Create a file named `app.py`:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Add a Simple Test**:
   Create a folder named `tests` and add a file named `test_app.py`:
   ```python
   from app import app

   def test_hello():
       client = app.test_client()
       response = client.get('/')
       assert response.data == b'Hello, World!'
       assert response.status_code == 200
   ```

4. **Update `requirements.txt` for Testing**:
   Create a `requirements.txt` file:
   ```plaintext
   Flask
   pytest
   ```

### Step 2: Set Up GitHub Actions for CI

1. **Create a `.github/workflows/ci.yml` File**:
   Create the directory and file:
   ```bash
   mkdir -p .github/workflows
   touch .github/workflows/ci.yml
   ```

   Add the following code to `ci.yml`:
   ```yaml
   name: CI

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.8'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         - name: Run tests
           run: pytest
   ```

### Step 3: Set Up Deployment with Vercel

1. **Create a Vercel Account**: Sign up at [Vercel](https://vercel.com).

2. **Install Vercel CLI** (optional for command line deployment):
   ```bash
   npm install -g vercel
   ```

3. **Deploy Your Project**:
   Run the following command in your project folder:
   ```bash
   vercel
   ```

4. **Configure Automatic Deployments**:
   - In your Vercel project settings, link your GitHub repository.
   - Vercel will automatically deploy your project every time you push to the main branch.

### Final Steps

1. **Commit Your Code**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Observe CI/CD in Action**:
   - Push changes to your repository. GitHub Actions will run your tests.
   - If all tests pass, Vercel will automatically deploy your application.

### Conclusion

Now you have a basic CI/CD pipeline for a Flask project using Python! This setup allows you to test your application automatically and deploy it with every push to the main branch. Feel free to enhance it with more features, such as environment variables or more complex testing scenarios. Happy coding!